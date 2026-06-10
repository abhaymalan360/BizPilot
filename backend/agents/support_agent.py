from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

class SupportAgent:
    def __init__(self):
        self.name = "Support Agent"
        self.llm = ChatOpenAI(temperature=0.2, model_name="gpt-3.5-turbo")
        self.memory = []
        self.system_prompt = SystemMessage(content="You are the Support Agent for BizPilot. Your goal is to help users troubleshoot issues, answer technical questions, and log tickets if necessary. Be calm, methodical, and very concise.")
        
    async def generate_response(self, text: str) -> str:
        messages = [self.system_prompt] + self.memory + [HumanMessage(content=text)]
        response = self.llm(messages)
        
        self.memory.append(HumanMessage(content=text))
        self.memory.append(response)
        
        return response.content
