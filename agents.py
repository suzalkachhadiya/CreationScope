from crewai import Agent
from tools import research_tool, scrapper_tools, google_datasets_tools, github_datasets_tools, kaggle_datasets_tools
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                        verbose=True,
                        temperature=0.5,
                        google_api_key=os.getenv("GOOGLE_API_KEY"))
research_agent = Agent(
        role='Industry Research Specialist',
        goal='Conduct comprehensive research on {company} and its industry',
        memory=True,
        backstory="""You are an expert industry analyst with years of experience in 
        company research and market analysis. Your expertise lies in gathering and 
        synthesizing information from various sources to provide detailed insights.
        """,
        tools=research_tool,
        verbose=True,
        llm=llm,
        allow_delegation=True,
        max_retry_limit=1
    )

# scraper_agent = Agent(
#         role='Website Content Specialist',
#         goal='Extract comprehensive information of {company} from {company_website}',
#         memory=True,
#         backstory="""You are an expert in web scraping and content analysis, 
#         specialized in extracting and organizing corporate information from company 
#         websites. You understand website structures and can efficiently navigate 
#         through different sections to gather relevant information.""",
#         tools=scrapper_tools,
#         verbose=True,
#         llm=llm,
#         allow_delegation=False
#     )

ai_usecase_agent = Agent(
    role='AI Solutions Strategist',
    goal='Analyze industry standards and generate AI/ML use cases for {company}',
    memory=True,
    backstory="""You are an AI/ML solutions expert with deep experience in enterprise digital transformation. 
    Your expertise spans across GenAI, Large Language Models, and ML implementations across various industries. 
    You excel at identifying opportunities where AI can create business value and improve operational efficiency.""",
    tools=scrapper_tools,
    verbose=True,
    llm=llm,
    allow_delegation=True,
    max_retry_limit=1
)

resource_collector = Agent(
    role='Resource and Dataset Specialist',
    goal='Collect and curate relevant datasets and resources for AI use cases',
    backstory="""You are an expert in finding and evaluating datasets and technical resources. 
    You have extensive experience with data repositories, open-source projects, and AI resources. 
    You excel at matching business use cases with appropriate datasets and technical solutions.""",
    tools=research_tool+github_datasets_tools+google_datasets_tools+kaggle_datasets_tools,
    verbose=True,
    llm=llm,
    allow_delegation=False,
    max_retry_limit=1    
)