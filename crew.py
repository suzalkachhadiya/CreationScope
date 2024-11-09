from crewai import Crew,Process
from tasks import industry_company_research_from_web,ai_usecase_analysis#, company_analysis_from_website
from agents import research_agent, ai_usecase_agent#,scraper_agent

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[research_agent,ai_usecase_agent],
    tasks=[industry_company_research_from_web,ai_usecase_analysis],
    process=Process.sequential,

)

result=crew.kickoff(
    inputs={
        'company':'Pricol',
        # 'company_website':'https://www.amararaja.com/'
        }
    )
print(result)