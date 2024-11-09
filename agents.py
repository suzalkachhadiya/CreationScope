from crewai import Agent
from tools import research_tool#, scrapper_tools
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
load_dotenv()

# print(type(scraper_agent))

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
        tools=[research_tool],
        verbose=True,
        llm=llm,
        allow_delegation=False
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

