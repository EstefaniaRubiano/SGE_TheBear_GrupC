"""
Este archivo de envarga de transformar
los datos del parametro "gasto" (en formato
List) a formato diccionario.
"""

def schema_gasto(gasto) -> dict:
    send_gasto = {"id": gasto["id"],
                "descripcion": gasto["descripcion"],
                "categoria": gasto["categoria"],
                "importe": gasto["importe"],
                "fecha": gasto["fecha"]

                   }
    return send_gasto

"""
Esta función devuelve una lista que contiene 
un diccionario con la información de los 
gastos.
"""
def schemas_gastos(gastos) -> list[dict]:
    return [schema_gasto(gasto) for k,gasto in gastos.items()]
