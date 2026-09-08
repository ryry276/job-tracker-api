from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Literal

app = FastAPI()

ApplicationStatus = Literal["applied", "interview", "rejected"]

class Application(BaseModel):
    id : int = Field(ge = 0)
    company: str
    role : str
    status : ApplicationStatus 


class UpdateApplication(BaseModel):
    company : Optional[str] = None
    role : Optional[str] = None
    status : ApplicationStatus | None = None

applications = []

@app.post("/applications",status_code = 201)
def create_application (application : Application):
    for current_application in applications:
        if current_application.id == application.id:
            raise HTTPException(
                status_code= 409,
                detail = "application already existed"
                )
    applications.append(application)
    return application

@app.get("/applications")
def get_applications(status : ApplicationStatus | None = None, company : str | None = None ):
    result = applications
    if status is not None:
        filtered = []
        for application in result:
            if application.status == status:
                filtered.append(application)
        result = filtered

    if company is not None:
        filtered = []
        for application in result:
            if application.company == company:
                filtered.append(application)
        result = filtered
        
    return result

   

@app.get("/applications/{application_id}")
def get_application_by_id(application_id : int):
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

@app.delete("/applications/{application_id}", status_code=204)
def delete_application(application_id : int):
    for application in applications:
        if application.id == application_id:
            applications.remove(application)
            return 

    raise HTTPException(
        status_code = 404,
        detail= "msg: application not found"
        )

