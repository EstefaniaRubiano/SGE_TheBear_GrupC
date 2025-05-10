from sqlmodel import SQLModel, Field

# Este modelo representa un evento organizado por el restaurante
# Incluye datos básicos del evento y el ID del responsable
class Evento(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre: str
    fecha: str
    lugar: str
    descripcion: str
    responsable_id: int = Field(foreign_key="empleado.id")