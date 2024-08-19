# python -m venv venv
# source venv/bin/activate  # On Windows: venv\Scripts\activate

# pip install fastapi uvicorn transformers pydantic


from fastapi import FastAPI
from app.routes import chat, auth  # Import routes for chat and authentication

app = FastAPI(
    title="ProChat - AI Chatbot",
    description="An AI-powered professional chatbot application.",
    version="1.0.0",
)

# Register routes
app.include_router(chat.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to ProChat - AI Chatbot!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



from fastapi import APIRouter, HTTPException
from app.services.nlp_service import get_bot_response

router = APIRouter()

@router.post("/chat")
def chat(message: str):
    if not message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    response = get_bot_response(message)
    return {"message": message, "response": response}


from transformers import pipeline

# Load a pre-trained model (e.g., GPT-2)
model = pipeline("text-generation", model="gpt2")

def get_bot_response(user_message: str) -> str:
    result = model(user_message, max_length=50, num_return_sequences=1)
    return result[0]['generated_text']


