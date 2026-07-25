# AI Chatbot (Angular + Python + OpenAI)

Full-stack chatbot with an Angular frontend and a FastAPI (Python) backend powered by OpenAI.

## Project structure

```
ai-chatbot/
├── backend/                 # FastAPI + OpenAI
│   └── app/
│       ├── main.py          # App entrypoint
│       ├── config.py        # Settings / env
│       ├── models/          # Pydantic request/response models
│       ├── routers/         # API routes
│       └── services/        # OpenAI integration
└── frontend/                # Angular chat UI
    └── src/app/
        ├── components/chat/ # Chat screen
        ├── services/        # HTTP client for backend
        └── models/          # TypeScript types
```

## Prerequisites

- Python 3.10+
- Node.js 18+ (recommended: `nvm use 20`)
- An [OpenAI API key](https://platform.openai.com/api-keys)

## Setup

### 1. Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and set OPENAI_API_KEY
uvicorn app.main:app --reload --port 8000
```

API docs: http://localhost:8000/docs

### 2. Frontend

```bash
cd frontend
# If needed: nvm use 20
npm install
npm start
```

App: http://localhost:4200

## API

| Method | Path         | Description              |
|--------|--------------|--------------------------|
| GET    | `/health`    | Health check             |
| POST   | `/api/chat`  | Send message, get reply  |

### Example request

```json
{
  "message": "Hello!",
  "history": [
    { "role": "user", "content": "Hi" },
    { "role": "assistant", "content": "Hello! How can I help?" }
  ]
}
```
