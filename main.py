from typing import List
from fastapi import FastAPI
from services import read
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import users
import os

app = FastAPI()

@app.get(path="/root", response_model=List[dict])
async def read_root():
    result = read.registre()
    return result