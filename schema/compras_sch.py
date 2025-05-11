def producto_schema(producto) -> dict:
    return {"producto": producto}

def productos_schema(productos) -> list[dict]:
    return [producto_schema(producto) for producto in productos]

def pedido_schema(pedido) -> dict:
    return {"pedido": pedido}

def pedidos_schema(pedidos) -> list[dict]:
    return [pedido_schema(pedido) for pedido in pedidos]