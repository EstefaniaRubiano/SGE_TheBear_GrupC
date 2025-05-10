"""
Este archivo de envarga de transformar
los datos del parametro "compra" (en formato
List) a formato diccionario.
"""

def schema(compra) -> dict:
    send_compra = {"id":compra["id"],
                   "descripcion":compra["proveedor"],
                   "categoria":compra["producto"],
                   "importe":compra["cantidad"],
                   "fecha": compra["fecha"]

                   }
    return send_compra

"""
Esta función devuelve una lista que contiene 
un diccionario con la información de las 
compras.
"""
def schemas(compras) -> list[dict]:
    return [schema(compra) for k,compra in compras.items()]