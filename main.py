from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Application(BaseModel):
    id : int
    company: str
    role : str
    status : str

class UpdateApplication(BaseModel):
    company : Optional[str] = None
    role : Optional[str] = None
    status : Optional[str] = None

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

@app.patch("/applications/{application_id}")
def update_application(update : UpdateApplication, application_id : int):
    for application in applications:
        if application.id == application_id:
            data = update.model_dump(exclude_unset=True)
            for key, value in data.items():
                setattr(application,key,value)
            return application

    raise HTTPException(
            status_code = 404,
            detail = "msg: application not found"
        )