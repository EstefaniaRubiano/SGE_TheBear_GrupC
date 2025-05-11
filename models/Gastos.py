from sqlmodel import SQLModel, Field

#Este modelo representa un gasto realizado por el restaurante.
#Incluye descripción, categoría, importe y fecha.
class Gasto(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    descripcion: str
    categoria: str
    importe: float
    fecha: str