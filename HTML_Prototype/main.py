from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

fake_responses = {
    "1": "Responsible lending is about providing loans to consumers in a way that ensures they can meet the repayments without undue hardship.",
    "2": "Please ask your specific question about lending policies.",
    "3": "I can help you with your loan application. Please provide the details you need assistance with.",
    "default": "I'm not sure how to respond to that. Can you ask something else?"
}

@app.post("/chat")
async def chat(message: Message):
    user_message = message.message.strip().lower()
    response_message = fake_responses.get(user_message, fake_responses["default"])
    return {"response": response_message}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
