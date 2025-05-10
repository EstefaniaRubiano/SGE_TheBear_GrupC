#Este archivo contiene los modelos relacionados con las compras.
#Incluye el modelo Producto y el modelo Pedido, que se relacionan entre sí.

from sqlmodel import SQLModel, Field

class Producto(SQLModel, table=True):
    #Representa un producto disponible para comprar
    id: int = Field(default=None, primary_key=True)
    nombre: str
    precio: float
    cantidad: int
    stock: int

class Pedido(SQLModel, table=True):
    #Representa una compra realizada por un empleado
    id: int = Field(default=None, primary_key=True)
    fecha: str
    precio_total: float
    id_empleado: int = Field(foreign_key="empleado.id")
    id_producto: int = Field(foreign_key="producto.id")