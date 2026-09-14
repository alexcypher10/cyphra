from fastapi import FastAPI
from pydantic import BaseModel
from src.cyphra import *
from src.database import *

app = FastAPI()
bot = Chatbot("Cyphra")

class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat (request: ChatRequest):
    reply = bot.response(request.message)
    return{"reply": reply}