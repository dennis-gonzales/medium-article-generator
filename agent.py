from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import agent, load_tools, initialize_agent, AgentType

load_dotenv()

llm = ChatOpenAI(temperature=0.1)

tools = load_tools(["wikipedia", "llm-math"], llm=llm)

agent = initialize_agent(
    tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

print("Ask the AI complex questions.")
prompt = input("input: ")

agent.run(prompt)
