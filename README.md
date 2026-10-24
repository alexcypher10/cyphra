CYPHRA

Cyphra is an AI chatbot project built with python and designed to provide intelligent, conversational interactions while being extensible enough to grow into a powerful personal AI assistant.

EXPECTED FEATURES
AI-powered conversaations
Context-aware responses
User management
Persistent conversation storage
PostgreSQL database integration
API-based architecture
Fast and scalable backend
Environment-based configuration
Modular and maintainable codebase1
Ready for deployment

TECH STACK
Backend
  python
  flask

Database
  PostgreSQL

AI
  large language model(LLM)

Deployment Tools
  Git
  Github
  Railway
  python virtual Environment.

PROJECT STRUCTURE
    src/
        __init__.py
        cyphra.py
    main.py
    tests/
        __init__.py
    .env
    .gitignore
    requirements.txt
    README.md
    LICENSE

INSTALLATION
Clone the repository
git clone https://github.com/alexcypher10/cyphra.git

Navigate into the project
cd cyphra

Create a virtual environment
python -m venv venv

Activate the virtual environment
Windows powershell
    venv\scripts\Activate.ps1

Windows CMD
    venv\scripts\activate

Install dependencies
pip install -r requirements.txt

ENVIRONMENT VARIABLES
create a .env file root in the root directory:

DATABASE_URL=
AI_API_KEY=
SECRET_KEY=

.env is included in the gitignore
.env
venv/.
__pycache__/
*.pyc

DATABASE
Cyphra uses PostgreSQL for persistent data storage.
The database can be used be used to store information such as:
User account
Conversations
Messages
Conversation History
User preferences
Application data

RUNNING CYPHRA
Activate your virtual environment first:
venv\Scripts\activate
Then start the application:
python main.py
The flask development server should then start locally.

TESTING
Run the test suite with:

pytest

DEVELOPMENT WORKFLOW
A typical development workflow looks like:
write code - test locally - git add - git commit - git push - github - deployment 
Example
git add .
git commit -m "Notes"
git push origin main

FUTURE PLANS
Cyphra is designed to grow aover time.
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
Cypheruvic
Software ENgineering student & Python Developer
         