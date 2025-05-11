from sqlmodel import SQLModel, Field

# Este modelo representa a un empleado del restaurante
# Contiene información personal y de contacto
class Empleado(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str
    puesto: str
    email: str
    telefono: int
