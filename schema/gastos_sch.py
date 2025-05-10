"""
Este archivo de envarga de transformar
los datos del parametro "gasto" (en formato
List) a formato diccionario.
"""

def schema(gasto) -> dict:
    send_gasto = {"id":gasto["id"],
                   "proveedor":gasto["proveedor"],
                   "producto":gasto["producto"],
                   "cantidad":gasto["cantidad"],
                   "precio": gasto["precio"],
                   "subtotal": gasto["subtotal"],
                   "fecha": gasto["fecha"],
                   "estado": gasto["estado"]
                   }
    return send_gasto

"""
Esta función devuelve una lista que contiene 
un diccionario con la información de los 
gastos.
"""
def schemas(gastos) -> list[dict]:
    return [schema(gasto) for k,gasto in gastos.items()]