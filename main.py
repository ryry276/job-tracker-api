from fastapi import FastAPI
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


