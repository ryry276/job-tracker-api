from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Applications(BaseModel):
    id : int
    company: str
    role : str
    status : str
