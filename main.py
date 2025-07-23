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