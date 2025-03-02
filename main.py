from typing import list
from fastapi import FastAPI
from services import read

app = FastASPI()

@app.get(path:"/root", response_model=List[dict])
async def read_root():
    result = read.registre()
    return result