# Devuelve un diccionario con un único evento
def evento_schema(evento) -> dict:
    response = {"evento": evento}
    return response

# Devuelve una lista de diccionarios, cada uno con un evento
def eventos_schema(eventos) -> list[dict]:
    response = [evento_schema(evento) for evento in eventos]
    return response
