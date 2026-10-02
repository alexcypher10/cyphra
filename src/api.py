from fastapi import FastAPI
from pydantic import BaseModel
from src.cyphra import *
from src.database import *

app = FastAPI()
bot = Chatbot("Cyphra")

class ChatRequest(BaseModel):
    message: str
    conversation_id: int | None = None

@app.get("/")
def read_root() :
    return {"message": "Cyphra API is running"}





@app.post("/chat")
def chat (request: ChatRequest):
    if request.conversation_id is None:
        exisiting_user = get_user_by_username("cypher")
        if exisiting_user:
            user_id = exisiting_user[0]
        else:
            user_id = create_user("cypher", "cypher@example.com")

        conversation_id = start_conversation(user_id)
    else:
        conversation_id =request.conversation_id
    save_message(conversation_id, "user", request.message)
    reply = bot.response(request.message)
    save_message(conversation_id, "bot", reply)
    return{
        "reply": reply,
        "conversation_id": conversation_id}