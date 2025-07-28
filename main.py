from fastapi import FastAPI #Import FastAPI framework

#Create an instance of FastAPI
app = FastAPI()


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
    question: str #Define a field for the question
    user_id: int #Define a field for the user ID

@app.post("/chatbot") #Define a route for the chatbot endpoint
async def chatbot_endpoint(requestBody: Chatbot):
    print(requestBody.question) #Print the question from the request body

    return {
        "data": {
            "response": "This is a response from the chatbot",
            "user_id": requestBody.question,},
            "status": "success",
            "message": "Chatbot response generated successfully"
    } #Return a JSON response with the chatbot's response and user ID
