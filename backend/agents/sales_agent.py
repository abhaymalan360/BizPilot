from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

class SalesAgent:
    def __init__(self):
        self.name = "Sales Agent"
        self.llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
        self.memory = []
        self.system_prompt = SystemMessage(content="You are the Sales Agent for BizPilot. Your goal is to qualify leads, highlight product value, and guide the customer toward making a purchase. Be enthusiastic and helpful, but keep your responses very concise.")
        
    async def generate_response(self, text: str) -> str:
        messages = [self.system_prompt] + self.memory + [HumanMessage(content=text)]
        response = self.llm(messages)
        
        self.memory.append(HumanMessage(content=text))
        self.memory.append(response)
        
        return response.content
