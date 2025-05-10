"""
En este archivo se pone toda aquella logia que
permitirá trabajar con las consultas del
cliente para proporcionar una respuesta
al main.py.
"""
from schema.compras_sch import schemas_productos, schemas_pedidos
from sqlmodel import Session, select
from models.compras import Producto, Pedido

#Obtener todos los productos
def get_all_productos(db:Session):
    sql_read = select(Producto)
    productos = db.exec(sql_read).all()
    return schemas_productos(productos)

#Obtener todos los pedidos
def get_all_pedidos(db: Session):
    sql_read = select(Pedido)
    pedidos = db.exec(sql_read).all()
    return schemas_pedidos(pedidos)

#Obtener un producto por ID
def get_producto(producto_id: int, db: Session):
    try:
        statement = select(Pedido).where(Pedido.id == compra_id)
        result = db.exec(statement).one()
        return pedido_schema(result)
    except:
        return pedido_schema("Compra no encontrada")

#Obtener un pedido por ID
def get_compra(compra_id: int, db: Session):
    try:
        statement = select(Pedido).where(Pedido.id == compra_id)
        result = db.exec(statement).one()
        return pedido_schema(result)
    except:
        return pedido_schema("Compra no encontrada")

def add_new_compra(fecha: str, precio_total: float, id_empleado: int, id_producto: int, db: Session):
    db_pedido = Pedido(fecha=fecha, precio_total=precio_total, id_empleado=id_empleado, id_producto=id_producto)
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return pedido_schema("Compra añadida correctamente")

def update_compra(compra_id: int, nuevo_precio: float, db: Session):
    statement = select(Pedido).where(Pedido.id == compra_id)
    pedido = db.exec(statement).one()
    pedido.precio_total = nuevo_precio
    db.add(pedido)
    db.commit()
    return pedido_schema("Compra actualizada correctamente")

def delete_compra(compra_id: int, db: Session):
    try:
        statement = select(Pedido).where(Pedido.id == compra_id)
        pedido = db.exec(statement).one()
        db.delete(pedido)
        db.commit()
        return pedido_schema("Compra eliminada correctamente")
    except:
        return pedido_schema("Compra no encontrada")


