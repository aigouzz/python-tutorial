import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from tools import get_current_weather, get_exchange_rate
from langchain_openai import ChatOpenAI

load_dotenv()

@tool
def weather(location: str) -> str:
    """Get the current weather for a given location."""
    return get_current_weather(location)
def exchange_rate(input: str) -> str:
    """Get the exchange rate between two currencies. Input should be in the format 'BASE TARGET'."""
    base, target = input.split()
    return get_exchange_rate(base, target)

tools = [weather, exchange_rate]

llm = ChatOpenAI(model="deepseek-chat",api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com", temperature=0)

agent = create_agent(model=llm, tools=tools, system_prompt="You are a helpful assistant.when the user asks about currency conversion or exchange rate, use the exchange_rate tool. when the user asks about weather, use the weather tool.")

while True:
    query = input("Enter your query (or 'exit' to quit): ")
    if (query.lower() == 'exit'):
        break
    result = agent.invoke({"messages": [{"role": "user", "content": query}]})
    print(f"Agent response: {result}")