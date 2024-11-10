from crewai import Task
from agents import research_agent, ai_usecase_agent, resource_collector#, scraper_agent

industry_company_research_from_web = Task(
        description="""
        1. Research and analyze the industry that {company} operates in
        2. Analyze major trends and challenges in the industry
        3. Use SerperDevTool for broad industry overview as well as recent news and updates
        4. Research {company}'s key offerings and products or services
        5. Identify strategic focus areas and initiatives
        6. Analyze vision, mission, and corporate strategy
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
        output_file="outputs/market-research-report/Research-report-ultratech.md"
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
        1. Generate specific use cases for AI/ML/CV/GenAI implementation
        - Propose GenAI applications for internal processes if applicable
        - Identify LLM opportunities for customer interaction if applicable
        - Suggest ML solutions for operational optimization if applicable
        - Suggest Computer Vision solutions if applicable
        2. Prioritize use cases based on:
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
    output_file="outputs/Use-Cases/AI-UseCase-Analysis-ultratech.md",
    dependencies=[industry_company_research_from_web]  # This task depends on the completion of industry research
)

resource_collection_task = Task(
    description="""
    For AI use cases which is in the top one in priority list given in use case report:
    1. Identify required data types and characteristics
    2. Search for relevant datasets on:
        - Kaggle
        - HuggingFace
        - GitHub
    3. Evaluate dataset quality and relevance based on:
        - Data completeness
        - Licensing terms
    """,
    agent=resource_collector,
    expected_output="""A report containing:
    - dataset links and description
    Formatted as markdown with clear sections and subsections
    """,
    output_file="outputs/Datasets-links/datasets-for-ultratech.md",
    dependencies=[ai_usecase_analysis]
)