"""
En este archivo se pone toda aquella logia que
permitirá trabajar con las consultas del
cliente para proporcionar una respuesta
al main.py.
"""
from schema.gastos_sch import schemas_gastos
from sqlmodel import Session, select
from models.gastos import Gasto

def get_all_gasto(db:Session):
    sql_read = select(Gasto)
    gastos = db.exec(sql_read).all()
    return schemas_gastos(gastos)
