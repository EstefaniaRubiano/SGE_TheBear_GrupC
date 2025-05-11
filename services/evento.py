from sqlmodel import Session, select
from models.Evento import Evento
from schema.eventos_sch import evento_schema, eventos_schema

# Obtener todos los eventos
def get_all_eventos(db: Session):
    sql_read = select(Evento)
    eventos = db.exec(sql_read).all()
    return eventos_schema(eventos)

# Obtener un evento por ID
def get_evento(evento_id: int, db: Session):
    try:
        sql_read = select(Evento).where(Evento.id == evento_id)
        result = db.exec(sql_read).one()
        return evento_schema(result)
    except:
        return evento_schema("Evento no encontrado")

# Añadir nuevo evento
def add_new_evento(nombre: str, fecha: str, lugar: str, descripcion: str, responsable_id: int, db: Session):
    db_evento = Evento(nombre=nombre, fecha=fecha, lugar=lugar, descripcion=descripcion, responsable_id=responsable_id)
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return evento_schema("Evento añadido correctamente")

# Actualizar evento por ID
def update_evento(evento_id: int, nuevo_lugar: str, db: Session):
    sql_select = select(Evento).where(Evento.id == evento_id)
    evento_db = db.exec(sql_select).one()

    evento_db.lugar = nuevo_lugar
    db.add(evento_db)
    db.commit()
    return evento_schema("Evento actualizado correctamente")

# Eliminar evento por ID
def delete_evento(evento_id: int, db: Session):
    try:
        sql_select = select(Evento).where(Evento.id == evento_id)
        evento_db = db.exec(sql_select).one()
        db.delete(evento_db)
        db.commit()
        return evento_schema("Evento eliminado correctamente")
    except:
        return evento_schema("Evento no encontrado")