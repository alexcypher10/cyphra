# Cyphra

Cyphra is an AI chatbot backend built with Python, FastAPI and PostgreSQL. It provides user accounts, email verification, JWT authentication and persistent conversation storage, and is designed to grow into a full AI assistant.

## Features

- User registration with bcrypt-hashed passwords
- Email verification codes
- JWT (Bearer token) authentication
- Persistent conversations and message history
- Per-user access control (users can only read their own conversations)
- Auto-generated interactive API docs

## Tech Stack

- **Backend:** Python, FastAPI, Uvicorn
- **Database:** PostgreSQL (psycopg2)
- **Auth:** bcrypt, PyJWT
- **Email:** smtplib (Gmail SMTP)
- **Tools:** Git, GitHub, Python virtual environment
- **Planned deployment:** Railway

## Project Structure

```
cyphra/
├── src/
│   ├── __init__.py
│   ├── api.py            # FastAPI routes
│   ├── auth.py           # JWT creation and verification
│   ├── cyphra.py         # Chatbot engine
│   ├── database.py       # PostgreSQL access functions
│   └── mail_service.py   # Verification code generation and email
├── tests/
│   └── __init__.py
├── main.py               # Terminal (CLI) interface
├── schema.sql            # Database schema
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation

```bash
git clone https://github.com/alexcypher10/cyphra.git
cd cyphra
python -m venv venv
```

Activate the virtual environment:

```bash
# Windows PowerShell
venv\Scripts\Activate.ps1

# Windows CMD
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root (see `.env.example`):

```
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432
JWT_SECRET=
GMAIL_ADDRESS=
APP_PASSWORD=
```

`APP_PASSWORD` is a Gmail App Password, not your normal Gmail password. `.env` is listed in `.gitignore` and must never be committed.

## Database Setup

1. Create a PostgreSQL database (for example `cyphra_db`).
2. Run `schema.sql` against it to create the `users`, `conversations` and `messages` tables.

## Running Cyphra

Start the API server:

```bash
uvicorn src.api:app --reload
```

The API runs at `http://127.0.0.1:8000`. Interactive documentation is at `http://127.0.0.1:8000/docs`.

To use the terminal version instead:

```bash
python main.py
```

## API Reference

All request and response bodies are JSON. Errors return `{"detail": "message"}`.

### Authentication flow

1. `POST /register` creates the account and emails a 6-digit code.
2. `POST /verify` confirms the code.
3. `POST /login` returns an `access_token`.
4. Send the token on protected routes: `Authorization: Bearer <access_token>`. Tokens expire after 1 hour.

### Endpoints

| Method | Path | Auth | Purpose |
|--------|------|------|---------|
| GET | `/` | No | Health check |
| POST | `/register` | No | Create an account |
| POST | `/verify` | No | Verify email with code |
| POST | `/login` | No | Get an access token |
| POST | `/chat` | Bearer | Send a message |
| GET | `/history/{conversation_id}` | Bearer | Get a conversation's messages |

**POST /register**
```json
{ "username": "alex", "email": "alex@example.com", "password": "secret123" }
```
Returns `{ "message": "...", "user_id": 1 }`. A 6-digit code is emailed (expires after 10 minutes).

**POST /verify**
```json
{ "username": "alex", "code": "483921" }
```
`code` must be sent as a **string**. Errors: `404` user not found, `400` invalid or expired code.

**POST /login**
```json
{ "username": "alex", "password": "secret123" }
```
Returns `{ "message": "...", "access_token": "eyJ...", "user_id": 1 }`. Error: `401` invalid username or password.

**POST /chat** (Bearer token required)
```json
{ "message": "hello", "conversation_id": null }
```
Omit `conversation_id` (or send `null`) to start a new conversation. Send an existing ID to continue one. Returns `{ "reply": "...", "conversation_id": 12 }`. Save the `conversation_id` and send it with the next message. Error: `401` missing or invalid token.

**GET /history/{conversation_id}** (Bearer token required)

Returns `{ "messages": [["user", "hello", "<timestamp>"], ["bot", "Hi...", "<timestamp>"]] }`, ordered oldest to newest. Errors: `401` bad token, `403` not your conversation, `404` conversation not found.

## Testing

```bash
pytest
```

## Roadmap

- Google sign-in (OAuth)
- LLM integration for real AI responses
- Long-term memory and user preferences
- Web frontend (HTML/CSS/JavaScript)
- Docker and deployment (Railway)
- Rate limiting and production hardening

## Goal

Cyphra is more than a chatbot. It's the foundation of an AI system built to evolve: one that understands users, maintains conversation context, works with stored data, and keeps gaining new capabilities.

## Author

Cypheruvic — Software Engineering student and Python developer
FUTURE PLANS
Cyphra is designed to grow over time.
planned improvments include:
    voice conversations
    image understanding
    file/document analysis
    improved long term memory
    personalized user profiles
    Authentication and authrization
    mobile application
    web interface
    real time conversations
    usage analytics
    more AI model integration

GOAL
The goal of Cyphra is to build a powerful, intelligent and extensible AI assistant that can understand users, maintain conversations context, interact with stored data, and continuosly gain new capabilities

it isn't just a chatbot 
    its the beginning of an AI system built to evolve.

AUTHOR
Cypher
Software ENgineering student & Python Developer
         