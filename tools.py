from crewai_tools import SerperDevTool, WebsiteSearchTool, SeleniumScrapingTool
from dotenv import load_dotenv
import os
import logging
from typing import Dict, Any
import time
from functools import lru_cache

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class OptimizedSerperTool(SerperDevTool):
    # def __init__(self):
        # super().__init__()
        # self.logger = logging.getLogger(__name__)
    _last_request_time = 0
    _min_request_interval = 1  # Minimum seconds between requests
        
    @lru_cache(maxsize=100)
    def cached_search(self, query: str) -> Dict[str, Any]:
        """Cached version of search to avoid duplicate requests"""
        return self.search(query)
    
    def search(self, query: str) -> Dict[str, Any]:
        """Rate-limited search with error handling"""
        # Rate limiting
        current_time = time.time()
        time_since_last_request = current_time - self._last_request_time
        if time_since_last_request < self._min_request_interval:
            time.sleep(self._min_request_interval - time_since_last_request)
        
        try:
            result = super().run(query)
            self.last_request_time = time.time()
            return result
        except Exception as e:
            self.logger.error(f"Search error for query '{query}': {str(e)}")
            # Return empty result instead of retrying
            return {"error": str(e), "results": []}

# Initialize tools with optimizations
load_dotenv()
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

research_tool = [OptimizedSerperTool()]

scrapper_tools = [
    OptimizedSerperTool(),
    WebsiteSearchTool(
        website="https://www.mckinsey.com/",
        config=dict(
            llm=dict(
                provider="google", 
                config=dict(
                    model="gemini-1.5-flash"
                ),
            ),
            embedder=dict(
                provider="google",
                config=dict(
                    model="models/embedding-001",
                    task_type="retrieval_document",
                ),
            ),
        )
    ),
    SeleniumScrapingTool(website_url="https://www.mckinsey.com/")
]

github_datasets_tools=[
    WebsiteSearchTool(
        website="https://github.com/search?q=datasets&type=repositories",
        config=dict(
            llm=dict(
                provider="google", 
                config=dict(
                    model="gemini-1.5-flash"
                ),
            ),
            embedder=dict(
                provider="google",
                config=dict(
                    model="models/embedding-001",
                    task_type="retrieval_document",
                ),
            ),
        )
    ),
    SeleniumScrapingTool(website_url="https://github.com/search?q=datasets&type=repositories")
]

kaggle_datasets_tools=[
    SerperDevTool(),
    WebsiteSearchTool(
        website="https://www.kaggle.com/datasets",
        config=dict(
            llm=dict(
                provider="google", 
                config=dict(
                    model="gemini-1.5-flash"
                ),
            ),
            embedder=dict(
                provider="google",
                config=dict(
                    model="models/embedding-001",
                    task_type="retrieval_document",
                ),
            ),
        )
    ),
    SeleniumScrapingTool(website_url="https://www.kaggle.com/datasets")
]

google_datasets_tools=[
    SerperDevTool(),
    WebsiteSearchTool(
        website="https://datasetsearch.research.google.com/",
        config=dict(
            llm=dict(
                provider="google", 
                config=dict(
                    model="gemini-1.5-flash"
                ),
            ),
            embedder=dict(
                provider="google",
                config=dict(
                    model="models/embedding-001",
                    task_type="retrieval_document",
                ),
            ),
        )
    ),
    SeleniumScrapingTool(website_url="https://datasetsearch.research.google.com/")
]