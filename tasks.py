from crewai import Task
from agents import research_agent#, scraper_agent

industry_company_research_from_web = Task(
        description="""
        1. Research and analyze the industry that {company} operates in
        2. Identify key industry segments and market positioning
        3. Analyze major trends and challenges in the industry
        4. Use SerperDevTool for broad industry overview as well as recent news and updates
        5. Research {company}'s key offerings and products
        6. Identify strategic focus areas and initiatives
        7. Analyze vision, mission, and corporate strategy
        """,
        agent=research_agent,
        expected_output="""A comprehensive report containing:
            - Company's current market position and market share
            - Recent company developments and news
            - Key industry trends and trends affecting the company
            - complete insights of industry's past, present and future outlooks
            - List of products and services with description
            - key offerings and focus area of a company
            formatted as markdown
        """,
        output_file="Research-report-{company}.md"
)

# company_analysis_from_website = Task(
#         description="""
#         1. Navigate to {company_website}
#         2. Research {company}'s key offerings and products
#         3. Identify strategic focus areas and initiatives
#         4. Analyze vision, mission, and corporate strategy
#         5. Use SeleniumScrapingTool, WebsiteSearchTool to extract detailed product information.
#         """,
#         agent=scraper_agent,
#         expected_output="""A detailed analysis including:
#             - Complete company overview, history and vision of company
#             - List of products and services with description
#             - key offerings and focus area of a company
#             formatted as markdown
#         """,
#         output_file="Research-report-{company}.md"
#     )