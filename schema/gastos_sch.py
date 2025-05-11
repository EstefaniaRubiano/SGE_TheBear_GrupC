def gasto_schema(gasto) -> dict:
    return {"gasto": gasto}

def gastos_schema(gastos) -> list[dict]:
    return [gasto_schema(gasto) for gasto in gastos]


