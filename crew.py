from crewai import Crew,Process
from tasks import industry_company_research_from_web,ai_usecase_analysis, resource_collection_task#, company_analysis_from_website
from agents import research_agent, ai_usecase_agent, resource_collector#,scraper_agent

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[research_agent,ai_usecase_agent,resource_collector],
    tasks=[industry_company_research_from_web,ai_usecase_analysis,resource_collection_task],
    process=Process.sequential,

)

result=crew.kickoff(
    inputs={
        'company':'UltraTech Cement',
        }
    )
print(result)