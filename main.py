from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Application(BaseModel):
    id : int
    company: str
    role : str
    status : str

applications = []

@app.post("/applications",status_code = 201)
def create_application (application : Application):
    applications.append(application)
    return application

@app.get("/applications")
def get_all_application():
    return applications

@app.get("/applications/{application_id}")
def get_application(application_id : int):
    for application in applications:
        if application_id == application.id:
            return application

    raise HTTPException(
        status_code = 404,
        detail = "msg: application not found"
    )