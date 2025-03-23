from typing import List
from fastapi import FastAPI, Depends
from services import read
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import user
import os


# Crear l'aplicació FastAPI
app = FastAPI()

# 1. Carregar variables d'entorn
load_dotenv()

# 2. Configurar la connexió a PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL") # Obtenir la URL de connexió
engine = create_engine(DATABASE_URL) # Crear l'engine de connexió

# 3. Crear les taules a la base de dades
SQLModel.metadata.create_all(engine)

# 4. Dependència per obtenir la sessió de la base de dades
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

# 5. Endpoint per afegir usuaris
@app.get("/users/", response_model=list[dict])
def read_user(db:Session = Depends(get_db)):
    result = user.get_all_users(db)
    return result

# 6. Endpoint
@app.post("/users/", response_model=dict)
def create_user(name: str, email:str, db:Session = Depends(get_db)):
    result = user.add_new_user(name, email, db)
    return result

# 7. Endpoint per modificar alguna dada de l'usuari
@app.put("/update_user/", response_model=dict)
async def update_user(id:int,name:str, db:Session = Depends(get_db)):
    result = user.update_user(id, name, db)
    return result

# 8. Endpoint per eliminar un usuari
@app.delete("/user/delete/", response_model=dict)
async def delete_user(id:int, db:Session = Depends(get_db)):
    result = user.delete_user(id, db)
    return result



