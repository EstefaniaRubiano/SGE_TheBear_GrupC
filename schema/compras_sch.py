"""
Este archivo de envarga de transformar
los datos del parametro "pedido" (en formato
List) a formato diccionario.
"""

def schema_pedido(pedido) -> dict:
    send_pedido = {"id": pedido["id"],
                    "fecha": pedido["fecha"],
                    "precio_total": pedido["precio_total"],
                    "id_empleado": pedido["id_empleado"],
                    "id_producto": pedido["id_producto"],
                    "id_gastos": pedido["id_gastos"]
     }
    return send_pedido

"""
Esta función devuelve una lista que contiene 
un diccionario con la información de los pedidos.
"""
def schemas_pedidos(pedidos) -> list[dict]:
    return [schema_pedido(pedido) for k,pedido in pedidos.items()]

# -------------------------------------------------------------------------------------------------------------

"""
Este archivo de envarga de transformar
los datos del parametro "producto" (en formato
List) a formato diccionario.
"""
def schema_producto(producto) -> dict:
    send_producto = {"id": producto["id"],
                    "nombre": producto["nombre"],
                    "precio": producto["precio"],
                    "cantidad": producto["cantidad"],
                    "stock": producto["stock"]
     }
    return send_producto

"""
Esta función devuelve una lista que contiene 
un diccionario con la información de los productos.
"""
def schemas_productos(productos) -> list[dict]:
    return [schema_producto(producto) for k,producto in productos.items()]