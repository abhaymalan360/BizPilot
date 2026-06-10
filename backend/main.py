from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from orchestrator import Orchestrator
import json

app = FastAPI(title="BizPilot Orchestrator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

orchestrator = Orchestrator()

@app.get("/")
def read_root():
    return {"status": "BizPilot Orchestrator Online"}

from pydantic import BaseModel
class InitRequest(BaseModel):
    business_name: str
    tone: str
    industry: str

@app.post("/api/initialize")
def initialize_system(data: InitRequest):
    # Setup initial context
    orchestrator.sales_agent.system_prompt.content += f"\nBusiness Context: {data.business_name}, {data.industry}. Tone: {data.tone}."
    orchestrator.support_agent.system_prompt.content += f"\nBusiness Context: {data.business_name}, {data.industry}. Tone: {data.tone}."
    orchestrator.care_agent.system_prompt.content += f"\nBusiness Context: {data.business_name}, {data.industry}. Tone: {data.tone}."
    return {"status": "success", "message": "System initialized"}

@app.get("/api/analytics")
def get_analytics():
    return orchestrator.analytics

@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            
            user_text = message.get("text", "")
            
            # Route through the orchestrator
            response_data = await orchestrator.process_message(user_text)
            
            await websocket.send_text(json.dumps(response_data))
            
    except WebSocketDisconnect:
        print("Client disconnected")
