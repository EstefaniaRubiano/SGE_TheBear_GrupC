from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import users
import os

app = FastAPI()

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@app.get(path="/users/", response_model=List[dict])
def read_user(db:Session = Depends(get_db)):
    result = users.get_all_users(db)
    return result

@app.post("/users/", response_model=dict)
def create_user(name: str, email: str, db:Session = Depends(get_db)):
    result = users.add_new_user(name, email, db)
    return result

@app.put("/users/", response_model=dict)
async def update_user(id: int, email: str, db:Session = Depends(get_db)):
    result = users.update_user(id, email, db)
    return result
