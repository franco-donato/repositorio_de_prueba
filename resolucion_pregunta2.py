def estados_paquetes(database):
    cantidades = {}
    for clave in database:
        fila = database[clave]
        state = fila["State"]
        quantity = int(fila["Quantity"])
        if state not in cantidades:
            cantidades[state] = quantity
        else: cantidades[state] += quantity
    return cantidades

def estado_que_mas_recibio(cantidades_estados):
    estado = ""
    valor = 0
    for clave in cantidades_estados:
        if cantidades_estados[clave] > valor:
            valor = cantidades_estados[clave]
            estado = clave
    return [estado, valor]