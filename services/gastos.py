"""
En este archivo se pone toda aquella logia que
permitirá trabajar con las consultas del
cliente para proporcionar una respuesta
al main.py.
"""
from schema.gastos_sch import gasto_schema, gastos_schema
from sqlmodel import Session, select
from models.Gastos import Gasto

#Obtener todos los gastos
def get_all_gasto(db:Session):
    sql_read = select(Gasto)
    gastos = db.exec(sql_read).all()
    return gastos_schema(gastos)

#Obtener un gasto por ID
def get_gasto(id: int, db: Session):
    try:
        statement = select(Gasto).where(Gasto.id == id)
        resultado = db.exec(statement).one()
        return gasto_schema(resultado)
    except:
        return gasto_schema("Gasto no encontrado")

#Añadir nuevo gasto
def add_new_gasto(descripcion: str, categoria: str, importe: float, fecha: str, db: Session):
    db_gasto = Gasto(descripcion=descripcion, categoria=categoria, importe=importe, fecha=fecha)
    db.add(db_gasto)
    db.commit()
    db.refresh(db_gasto)
    return gasto_schema("Gasto añadido correctamente")

#Actualizar gasto por ID
def update_gasto(gasto_id: int, nueva_categoria: str, db: Session):
    sql_select = select(Gasto).where(Gasto.id == gasto_id)
    gasto_db = db.exec(sql_select).one()

    gasto_db.categoria = nueva_categoria
    db.add(gasto_db)
    db.commit()
    return {"msg":"Gasto actualizado correctamente"}

#Eliminar gasto por ID
def delete_gasto(gasto_id: int, db: Session):
    try:
        sql_select = select(Gasto).where(Gasto.id == gasto_id)
        gasto_db = db.exec(sql_select).one()

        db.delete(gasto_db)
        db.commit()
        return {"msg":"Gasto eliminado correctamente"}
    except:
        return {"msg":"Gasto no existe"}