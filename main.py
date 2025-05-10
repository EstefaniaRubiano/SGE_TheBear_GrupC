from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import compras, gastos, evento, empleado
from models import compras, gastos, evento, empleado
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

@app.get("/gastos/", response_model= list[dict])
async def read_gasto(db: Session = Depends(get_db)):
    result = gastos.get_all_gasto(db)
    return result

@app.get("/compras/", response_model= list[dict])
async def read_gasto(db: Session = Depends(get_db)):
    result = gastos.get_all_gasto(db)
    return result