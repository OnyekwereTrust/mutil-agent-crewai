from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv
import os
# Load variables from .env
load_dotenv()




marketer = Agent(
  role="Marketing Research Analyst",
  goal="Find out how big is a demand for my startup idea and suggest how to reach the target audience.",
  backstory="""You are an expert at understanding the market demand, target audience, and competition. This is crucial for 
		validating whether an idea fulfills a market need and has the potential to attract a wide audience. You are good at coming up
		with ideas on how to appeal to widest possible audience.
  """,
  verbose=True,
  allow_delegation=False,
  llm=model
)

business_consultant = Agent(
  role="Business Consultant",
  goal="Find out how to make my startup idea profitable and suggest a business model.",
  backstory="""You are an expert at understanding business models, revenue streams, and profitability. This is crucial for 
    validating whether an idea can be turned into a sustainable and profitable business. You are good at coming up
    with ideas on how to monetize a product or service.
  """,
  verbose=True,
  allow_delegation=False,
  llm=model
)


task1 = Task(
  description="""Analyze the market demand for a hiring platform that connects talents with companies.
  Write a well detailed report with descriptions of the target audience, their needs, and how to reach them.
  Include suggestions on marketing channels, messaging, and positioning strategies. 
  Provide a target audience persona and a list of potential competitors in the market.
  """,
  expected_output="""
  A detailed report with descriptions of the target audience, their needs, and how to reach them.
  Suggestions on marketing channels, messaging, and positioning strategies.
  A target audience persona and a list of potential competitors in the market.
  """,
  agent=marketer,
)

task2 = Task(
  description="""Analyze the business model for a hiring platform that connects talents with companies.
  Write a well detailed report with suggestions on how to make the platform profitable.
  """,
  expected_output="""
  A detailed report with suggestions on how to make the platform profitable.
  Suggestions on revenue streams, pricing strategies, and cost structures.
  A SWOT analysis and a list of potential risks and challenges.
  """,
  agent=business_consultant,
)

crew = Crew(
  agents=[marketer, business_consultant],
  tasks=[task1, task2],
  verbose=True,
  process=Process.sequential
)


result = crew.kickoff()

print("Final result:", result)








