# Este archivo se encarga de tranformar los datos del parámetro eventos
# (en formato list) a un formato diccionario con los campos que queremos mostrar

def schema(evento) -> dict:
    send_evento = {
        "id": evento["id"],
        "nombre": evento["nombre"],
        "fecha": evento["fecha"],
        "lugar": evento["lugar"],
        "descripcion": evento["descripcion"],
        "responsable_id": evento["responsable_id"]
    }
    return send_evento

def schemas(eventos) -> list[dict]:
    return [schema(evento) for k, evento in eventos.items()]