from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import compras, gastos, evento, empleado
from models import Compras, Gastos, Evento, Empleado
import os


app = FastAPI()

#Servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

#Ruta para servir el main_page.html por defecto
@app.get("/")
async def root():
    return FileResponse("static/main_page.html")

app = FastAPI()

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

#Endpoint para los gastos:
@app.get("/gastos/", response_model= list[dict])
async def read_gasto(db: Session = Depends(get_db)):
    result = gastos.get_all_gasto(db)
    return result

@app.get("/gastos/{id}", response_model=dict)
async def read_gastos_id(id: int, db: Session = Depends(get_db)):
    result = gastos.get_gasto(id, db)
    return result

@app.post("/gastos/post", response_model=dict)
async def create_gastos(descripcion: str, categoria: str, importe: float, fecha: str, db: Session = Depends(get_db)):
    result = gastos.add_new_gasto(descripcion, categoria, importe, fecha, db)
    return result

@app.put("/gastos/put", response_model=dict)
async def update_gastos_categoria(id: int, nueva_categoria: str, db: Session = Depends(get_db)):
    result = gastos.update_gasto(id, nueva_categoria, db)
    return result

@app.delete("/gastos/delete", response_model=dict)
async def delete_gastos_id(id: int, db: Session = Depends(get_db)):
    result = gastos.delete_gasto(id, db)
    return result


# Endpoints para productos
@app.get("/productos/", response_model=list[dict])
async def read_productos(db: Session = Depends(get_db)):
    result = compras.get_all_productos(db)
    return result

@app.get("/productos/{id}", response_model=dict)
async def read_producto_id(id: int, db: Session = Depends(get_db)):
    result = compras.get_producto(id, db)
    return result

@app.post("/productos/post", response_model=dict)
async def create_producto(nombre: str, precio: float, cantidad: int, stock: int, db: Session = Depends(get_db)):
    result = compras.add_new_producto(nombre, precio, cantidad, stock, db)
    return result

@app.put("/productos/put", response_model=dict)
async def update_producto_nombre(id: int, nuevo_nombre: str, db: Session = Depends(get_db)):
    result = compras.producto(id, nuevo_nombre, db)
    return result

@app.delete("/productos/delete", response_model=dict)
async def delete_producto_id(id: int, db: Session = Depends(get_db)):
    result = compras.delete_producto(id, db)
    return result


# Endpoints para pedidos
@app.get("/pedidos/", response_model=list[dict])
async def read_pedidos(db: Session = Depends(get_db)):
    result = compras.get_all_pedidos(db)
    return result

@app.get("/pedidos/{id}", response_model=dict)
async def read_pedido_id(id: int, db: Session = Depends(get_db)):
    result = compras.get_pedido(id, db)
    return result

@app.post("/pedidos/post", response_model=dict)
async def create_pedido(fecha: str, precio_total: float, id_empleado: int, id_producto: int, db: Session = Depends(get_db)):
    result = compras.add_new_pedido(fecha, precio_total, id_empleado, id_producto, db)
    return result

@app.put("/pedidos/put", response_model=dict)
async def update_pedido_precio(id: int, nuevo_precio: float, db: Session = Depends(get_db)):
    result = compras.update_pedido(id, nuevo_precio, db)
    return result

@app.delete("/pedidos/delete", response_model=dict)
async def delete_pedido_id(id: int, db: Session = Depends(get_db)):
    result = compras.delete_pedido(id, db)
    return result




#Endpoints para empleados:
@app.get("/empleados/", response_model=list[dict])
async def read_empleados(db: Session = Depends(get_db)):
    result = empleado.get_all_empleados(db)
    return result

@app.get("/empleados/{id}", response_model=dict)
async def read_empleado_id(id: int, db: Session = Depends(get_db)):
    result = empleado.get_empleado(id, db)
    return result

@app.post("/empleados/post", response_model=dict)
async def create_empleado(nombre: str, puesto: str, email: str, telefono: str, db: Session = Depends(get_db)):
    result = empleado.add_new_empleado(nombre, puesto, email, telefono, db)
    return result

@app.put("/empleados/put", response_model=dict)
async def update_empleado_nombre(id: int, nuevo_nombre: str, db: Session = Depends(get_db)):
    result = empleado.update_empleado(id, nuevo_nombre, db)
    return result

@app.delete("/empleados/delete", response_model=dict)
async def delete_empleado_id(id: int, db: Session = Depends(get_db)):
    result = empleado.delete_empleado(id, db)
    return result

#Endpoints para eventos:
@app.get("/eventos/", response_model=list[dict])
async def read_eventos(db: Session = Depends(get_db)):
    result = evento.get_all_eventos(db)
    return result

@app.get("/eventos/{id}", response_model=dict)
async def read_evento_id(id: int, db: Session = Depends(get_db)):
    result = evento.get_evento(id, db)
    return result

@app.post("/eventos/post", response_model=dict)
async def create_evento(nombre: str, fecha: str, lugar: str, descripcion: str, responsable_id: int, db: Session = Depends(get_db)):
    result = evento.add_new_evento(nombre, fecha, lugar, descripcion, responsable_id, db)
    return result

@app.put("/eventos/put", response_model=dict)
async def update_evento_lugar(id: int, nuevo_lugar: str, db: Session = Depends(get_db)):
    result = evento.update_evento(id, nuevo_lugar, db)
    return result

@app.delete("/eventos/delete", response_model=dict)
async def delete_evento_id(id: int, db: Session = Depends(get_db)):
    result = evento.delete_evento(id, db)
    return result