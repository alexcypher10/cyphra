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
def read_ot() :
    return {"message": "Cyphra API is running"}


@app.post("/chat")
def chat (request: ChatRequest):
    if request.conversation_id is None:
        exisiting_user = get_user_by_username("cypher")
        if exisiting_user:
            user_id = exisiting_user[0]
        else:
            user_id = create_user("cypher", "cypher@example.com", hash_password("placeholder123"))

        conversation_id = start_conversation(user_id)
    else:
        conversation_id =request.conversation_id
    save_message(conversation_id, "user", request.message)
    reply = bot.response(request.message)
    save_message(conversation_id, "bot", reply)
    return{
        "reply": reply,
        "conversation_id": conversation_id}



@app.get("/history/{conversation_id}")
def history(conversation_id: int):
    messages = get_message(conversation_id)
    return {"messages": messages}



class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

@app.post("/register")
def register(request: RegisterRequest):
    hashed = hash_password(request.password)
    user_id = create_user(request.username, request.email, hashed)
    return{"message": "Registration complete. ", "user_id": user_id}
    
    