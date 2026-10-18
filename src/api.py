from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from src.cyphra import *
from src.database import *
from src.auth import *



app = FastAPI()
bot = Chatbot("Cyphra")

class ChatRequest(BaseModel):
    message: str
    conversation_id: int | None = None

@app.get("/")
def read_ot() :
    return {"message": "Cyphra API is running"}


@app.post("/chat")
def chat (request: ChatRequest, user_id: int = Depends(get_current_user)):
    if request.conversation_id is None:
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
    return{
        "message": "Registration complete. ",
        "user_id": user_id}

class loginRequest(BaseModel):
    username : str
    password : str

@app.post("/login")
def login(request: loginRequest):
    user= get_user_by_username(request.username)
    if not user:
        raise HTTPException(status_code=401, detail="imvalid username or password")

    user_id, hash_password = user

    if not check_password(request.password, hash_password):
        raise HTTPException(status_code=401, detail="imvalid username or password")
    token = create_access_token(user_id)

    return {
        "message": "login sucessfull",
        "access_token": token,
        "user_id": user_id}
 