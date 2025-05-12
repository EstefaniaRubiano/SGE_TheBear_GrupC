"""
En este archivo se pone toda aquella logia que
permitirá trabajar con las consultas del
cliente para proporcionar una respuesta
al main.py.
"""
from schema.compras_sch import productos_schema, producto_schema, pedidos_schema, pedido_schema
from sqlmodel import Session, select
from models.Compras import Producto, Pedido

#Obtener todos los productos
def get_all_productos(db:Session):
    sql_read = select(Producto)
    productos = db.exec(sql_read).all()
    return productos_schema(productos)

#Obtener todos los pedidos
def get_all_pedidos(db: Session):
    sql_read = select(Pedido)
    pedidos = db.exec(sql_read).all()
    return pedidos_schema(pedidos)

#Obtener un producto por ID
def get_producto(producto_id: int, db: Session):
    try:
        statement = select(Producto).where(Producto.id == producto_id)
        resultado = db.exec(statement).one()
        return producto_schema(resultado)
    except:
        return producto_schema("Producto no encontrado")

#Obtener un pedido por ID
def get_pedido(pedido_id: int, db: Session):
    try:
        statement = select(Pedido).where(Pedido.id == pedido_id)
        resultado = db.exec(statement).one()
        return pedido_schema(resultado)
    except:
        return pedido_schema("Compra no encontrada")

#Añadir nuevo producto
def add_new_producto(nombre: str, precio: float, cantidad: int, stock: int, db: Session):
    db_producto = Producto(nombre=nombre, precio=precio, cantidad=cantidad, stock=stock)
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return producto_schema("Producto añadido correctamente")

#Añadir nuevo pedido
def add_new_pedido(fecha: str, precio_total: float, id_empleado: int, db: Session):
    db_pedido = Pedido(fecha=fecha, precio_total=precio_total, id_empleado=id_empleado)
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return pedido_schema("Pedido añadido correctamente")

#Actualizar producto por ID
def producto(producto_id: int, nuevo_nombre: str, db: Session):
    sql_select = select(Producto).where(Producto.id == producto_id)
    producto_db = db.exec(sql_select).one()

    producto_db.nombre = nuevo_nombre
    db.add(producto_db)
    db.commit()
    return {"msg":"Producto actualizado correctamente"}

#Actualizar pedido por ID
def update_pedido(pedido_id: int, nuevo_precio: float, db: Session):
    sql_select = select(Pedido).where(Pedido.id == pedido_id)
    pedido_db = db.exec(sql_select).one()

    pedido_db.precio_total = nuevo_precio
    db.add(pedido_db)
    db.commit()
    return {"msg":"Pedido actualizado correctamente"}


#Eliminar producto por ID
def delete_producto(producto_id: int, db: Session):
    try:
        sql_select = select(Producto).where(Producto.id == producto_id)
        producto_db = db.exec(sql_select).one()

        db.delete(producto_db)
        db.commit()
        return {"msg":"Producto eliminado correctamente"}
    except:
        return {"msg":"Prodcuto no existe"}

#Eliminar pedido por ID
def delete_pedido(pedido_id: int, db: Session):
    try:
        sql_select = select(Pedido).where(Pedido.id == pedido_id)
        pedido_db = db.exec(sql_select).one()

        db.delete(pedido_db)
        db.commit()
        return {"msg":"Pedido eliminado correctamente"}
    except:
        return {"msg":"Pedido no existe"}