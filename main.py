from fastapi import FastAPI #Import FastAPI framework
from langchain_cohere import ChatCohere # ChatCohere intrz chatmodel
from dotenv import load_dotenv #Import load_dotenv to load environment variables

load_dotenv() #Load environment variables from a .env file

#Create an instance of FastAPI
app = FastAPI()

#instancia del model 
model= ChatCohere()

#Define un JSON responde 
JSON_RESPONSE = {
    "usuario": "Francisco",
    "email": 'fjrmar@gmail.com',
    "edad": "30",}

@app.get("/Datos") 
def get_data():
     response= JSON_RESPONSE #Define a function that returns the JSON response
     return {"data": response,
             "message": "Datos obtenidos correctamente"}


@app.get("/Hello-World") #Define a route for the root URL
def hello_world():
    return {"message": "Hello, Francisco!"} #Define a function that returns a JSON response with a greeting message

from fastapi import FastAPI #Import FastAPI framework
from pydantic import BaseModel #Import BaseModel from Pydantic for data validation

#Definie a Pydantic model for the request body
class Chatbot(BaseModel):
    question: str  # Add the question field to the model


@app.post("/chatbot") #Define a route for the chatbot endpoint
async def chatbot_endpoint(requestBody: Chatbot):
        
    question = requestBody.question #Extract the question from the request body
    response= model.invoke(question) #Invoke the ChatCohere model with the question

    return {
        "data": {
            "question": requestBody.question},
            "response": response.content #Return the chatbot's response 
    } #Return a JSON response with the chatbot's response and user ID

