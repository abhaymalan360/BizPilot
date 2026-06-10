import random
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from agents.sales_agent import SalesAgent
from agents.support_agent import SupportAgent
from agents.care_agent import CareAgent
import json
import os
from dotenv import load_dotenv

load_dotenv()

class Orchestrator:
    def __init__(self):
        self.sales_agent = SalesAgent()
        self.support_agent = SupportAgent()
        self.care_agent = CareAgent()
        
        # We use a router LLM to decide which agent to send the message to
        self.router_llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
        self.router_prompt = SystemMessage(content='''You are the Orchestrator Router for BizPilot.
Analyze the user's message and determine the intent, confidence score (0.0 to 1.0), and which agent should handle it.
The agents are:
- sales (handles purchase intent, pricing, upgrading)
- care (handles high frustration, anger, cancellation threats, churn risk)
- support (handles general inquiries, troubleshooting, technical questions)

Respond strictly in JSON format:
{
  "intent": "Brief description of intent",
  "confidence": 0.95,
  "agentType": "sales" | "care" | "support"
}
''')

        # Simple analytics tracking in-memory for the MVP dashboard
        self.analytics = {
            "sales": 0,
            "support": 0,
            "care": 0,
            "total": 0
        }

    async def process_message(self, user_text: str):
        # 1. Route the message
        messages = [self.router_prompt, HumanMessage(content=user_text)]
        try:
            route_response = self.router_llm(messages).content
            route_data = json.loads(route_response)
        except Exception as e:
            print(f"Routing error: {e}")
            route_data = {
                "intent": "Support Inquiry (Fallback)",
                "confidence": 0.8,
                "agentType": "support"
            }
            
        agent_type = route_data.get("agentType", "support")
        intent = route_data.get("intent", "General Inquiry")
        confidence = route_data.get("confidence", 0.9)
        
        # 2. Update analytics
        self.analytics["total"] += 1
        if agent_type in self.analytics:
            self.analytics[agent_type] += 1
            
        # 3. Get response from the selected agent
        agent_name = "Support Agent"
        response = ""
        
        if agent_type == "sales":
            agent_name = "Sales Agent"
            response = await self.sales_agent.generate_response(user_text)
        elif agent_type == "care":
            agent_name = "Care Agent"
            response = await self.care_agent.generate_response(user_text)
        else:
            agent_type = "support"
            agent_name = "Support Agent"
            response = await self.support_agent.generate_response(user_text)
            
        return {
            "intent": intent,
            "confidence": confidence,
            "agentType": agent_type,
            "agentName": agent_name,
            "response": response
        }
