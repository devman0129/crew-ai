from crewai import Agent, Task, Crew, Process
import os

os.environ["OPENAI_API_KEY"] = "<OPENAI API KEY>"


#Researcher Agent
researcher = Agent(
  role='Researcher',
  goal='Research new AI Insights',
  backstory='You are an AI research assistant',
  verbose=True,
  allow_delegation=False
)

#Writer Agent
writer = Agent(
  role='Writer',
  goal='write compelling and engaging blog posts about AI trends',
  backstory='You are an AI blog post writer who specializes in writing about AI tpics ',
  verbose=True,
  allow_delegation=False
)

#Create Task 1
task1 = Task(
  description='Investigate latest AI trends',
  agent=researcher
)

#Create Task 2
task2 = Task(
  description='Write a blog post on latest AI trends',
  agent=writer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

result = crew.kickoff()

print(result)