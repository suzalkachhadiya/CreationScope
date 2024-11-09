from crewai import Task
from agents import research_agent, ai_usecase_agent#, scraper_agent

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
            - Recent company developments and news
            - Key industry trends and trends affecting the company
            - complete insights of industry's future outlooks
            - List of products and services with description
            - key offerings and focus area of a company
            formatted as markdown
        """,
        output_file="outputs/market-research-report/Research-report-Pricol.md"
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

ai_usecase_analysis = Task(
    description="""
        1. Based on the industry research report, analyze current AI/ML adoption patterns
        - Review existing automation and AI implementations if exists
        - Identify industry-specific AI standards and best practices
        
        2. Generate specific use cases for AI/ML implementation
        - Propose GenAI applications for internal processes
        - Identify LLM opportunities for customer interaction
        - Suggest ML solutions for operational optimization
        
        3. Prioritize use cases based on:
        - {company}'s vision and operational needs
        - Expected ROI
        - Resource requirements
        - Risk assessment
        and list out those use cases
        """,
    agent=ai_usecase_agent,
    expected_output="""A detailed AI/ML/GenAI strategy report containing:
    - use case title
       * Objective/Use Case: description
       * AI Application: description
       * Cross-Functional Benefits: description
    Formatted as markdown with clear sections and subsections
    """,
    output_file="outputs/Use-Cases/AI-UseCase-Analysis-Pricol.md",
    dependencies=[industry_company_research_from_web]  # This task depends on the completion of industry research
)