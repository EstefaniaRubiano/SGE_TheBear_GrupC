"""
Aquest arxiu s'encarrega de transformar
les dades del parametre "gastos" (en format
List) a un format diccionari.
"""

def schema(gastos) -> dict:
    send_gastos = {"id":gastos["id"]
                   }