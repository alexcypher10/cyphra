from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from src.cyphra import *
from src.database import *
from src.auth import *
from src.mail_service import *
from datetime import datetime, timezone



app = FastAPI()
bot = Chatbot("Cyphra")

#creates a chat request endpoint
class ChatRequest(BaseModel):
    message: str
    conversation_id: int | None = None

@app.get("/")
def read_ot() :
    return {"message": "Cyphra API is running"}


#gets user requests from the api chat endpoint
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


# gets history of a particular conversation pia the conversation id 
@app.get("/history/{conversation_id}")
def history(conversation_id: int, user_id: int = Depends(get_current_user) ):
    owner = get_conversation(conversation_id)

    if owner is None:
        raise HTTPException(status_code=401, detail="Converssation not found")

    if owner != user_id:
        raise HTTPException(status_code=401, detail="you do not have access to this converstion")

    
    messages = get_message(conversation_id)
    return {"messages": messages}


# controls registration request from users
class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str


@app.post("/register")
# registers new users and hashes passwords
def register(request: RegisterRequest):
    hashed = hash_password(request.password)
    user_id = create_user(request.username, request.email, hashed)

    code = generate_verification_code()
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=10)
    send_verification_code(user_id, code, expires_at)
    send_verification_email(request.email, code)

    return{
        "message": "Registration complete. check your email for verification code.",
        "user_id": user_id}


#controls login request from user
class loginRequest(BaseModel):
    username : str
    password : str


# verifies user login via JWT and database connection
@app.post("/login")
def login(request: loginRequest):
    user = get_user_by_username(request.username)
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

class verifyRequest(BaseModel) :
    username : str
    code : str

@app.post("/verify")
def verify (request: verifyRequest):
    user = get_user_by_username(request.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_id, password_hash, verification_code, code_expires_at, is_verified = user

    if is_verified:
        return {"message": "Account is already verified"}

    if verification_code is None or request.code != verification_code:
        raise HTTPException(status_code=400, detail="Invalid verification code")

    if code_expires_at is None or datetime.now(timezone.utc) > code_expires_at.replace(tzinfo=timezone.utc):
        raise HTTPException(status_code=400, detail="Verification code expired") 

    mark_user_verified(user_id)
    return {"message": "Account Verified sucessfully"}

