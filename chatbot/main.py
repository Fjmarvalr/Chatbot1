from fastapi import FastAPI, Request
from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

app = FastAPI()
chat = ChatCohere()

@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    question = data.get("question", "")
    messages = [
        SystemMessage(content="Eres un experto en historia, politica y economia, solo das respuesta sobre situaciones actuales en el mundo, utilizando la historia y la información actual"),
        HumanMessage(content=question)
    ]
    response = chat.invoke(messages)
    return {
        "data": {
            "question": question,
            "response": response.content
        }
    }

