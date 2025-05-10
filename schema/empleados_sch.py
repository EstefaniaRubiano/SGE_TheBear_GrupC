# Este archivo se encarga de transformar los datos del parámetro empleado
# (en formato list) a un formato diccionario con los campos que queremos mostrar

def schema(empleado) -> dict:
    send_empleado = {
        "id": empleado["id"],
        "nombre": empleado["nombre"],
        "puesto": empleado["puesto"],
        "email": empleado["email"],
        "telefono": empleado["telefono"]
    }
    return send_empleado

def schemas(empleados) -> list[dict]:
    return [schema(empleado) for k, empleado in empleados.items()]