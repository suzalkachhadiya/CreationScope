from crewai_tools import SerperDevTool, SeleniumScrapingTool, WebsiteSearchTool
from dotenv import load_dotenv
import os

load_dotenv()
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

# Initialize the tool for internet searching capabilities
research_tool = SerperDevTool()

scrapper_tools = [
    SerperDevTool(),
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