from sqlmodel import Session, select
from models.Empleado import Empleado
from schema.empleados_sch import empleado_schema, empleados_schema

# Obtener todos los empleados
def get_all_empleados(db: Session):
    sql_read = select(Empleado)
    empleados = db.exec(sql_read).all()
    return empleados_schema(empleados)

# Obtener un empleado por ID
def get_empleado(id: int, db: Session):
    try:
        sql_read = select(Empleado).where(Empleado.id == id)
        result = db.exec(sql_read).one()
        return empleado_schema(result)
    except:
        return empleado_schema(f"Empleado con ID {id} no existe")

# Añadir nuevo empleado
def add_new_empleado(nombre: str, puesto: str, email: str, telefono: str, db: Session):
    db_empleado = Empleado(nombre=nombre, puesto=puesto, email=email, telefono=telefono)
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return {"Empleado añadido correctamente"}

# Actualizar empleado por ID
def update_empleado(id: int, nuevo_nombre: str, db: Session):
    sql_select = select(Empleado).where(Empleado.id == id)
    empleado_db = db.exec(sql_select).one()

    empleado_db.nombre = nuevo_nombre
    db.add(empleado_db)
    db.commit()
    return empleado_schema("Empleado actualizado correctamente")

# Eliminar empleado por ID
def delete_empleado(id: int, db: Session):
    try:
        sql_select = select(Empleado).where(Empleado.id == id)
        empleado_db = db.exec(sql_select).one()
        db.delete(empleado_db)
        db.commit()
        return empleado_schema("Empleado eliminado correctamente")
    except:
        return empleado_schema("Empleado no existe")
