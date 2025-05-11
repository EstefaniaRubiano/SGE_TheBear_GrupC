# Devuelve un diccionario con un único empleado
def empleado_schema(empleado) -> dict:
    response = {"empleado": empleado}
    return response

# Devuelve una lista de diccionarios, cada uno con un empleado
def empleados_schema(empleados) -> list[dict]:
    response = [empleado_schema(empleado) for empleado in empleados]
    return response
