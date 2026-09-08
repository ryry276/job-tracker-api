from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Literal
from routers import applications

app = FastAPI()
app.include_router(applications.router)