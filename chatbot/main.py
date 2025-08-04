from fastapi import FastAPI, Request
from langchain_core.messages import HumanMessage, SystemMessage
from config import model
from schemans import ChatRequest

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(request:ChatRequest):
    question = request.question
    user_id = request.user_id
    messages = [ 
        SystemMessage(content="Eres un experto en historia, politica y economia, solo das respuesta sobre situaciones actuales en el mundo, utilizando la historia y la información actual"),
        HumanMessage(content=question)
    ]
    response = model.invoke(messages)
    return {
        "data": {
            "question": question,
            "response": response.content
        }
    }

