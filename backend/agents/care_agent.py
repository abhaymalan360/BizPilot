from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

class CareAgent:
    def __init__(self):
        self.name = "Care Agent"
        self.llm = ChatOpenAI(temperature=0.5, model_name="gpt-3.5-turbo")
        self.memory = []
        self.system_prompt = SystemMessage(content="You are the Care Agent for BizPilot. You handle escalations, highly frustrated users, and retention. Your tone should be extremely empathetic, understanding, and accommodating. Offer solutions or compensation. Keep responses concise.")
        
    async def generate_response(self, text: str) -> str:
        messages = [self.system_prompt] + self.memory + [HumanMessage(content=text)]
        response = self.llm(messages)
        
        self.memory.append(HumanMessage(content=text))
        self.memory.append(response)
        
        return response.content
