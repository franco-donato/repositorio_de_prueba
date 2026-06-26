def cuenta_cantidades_enteras(database : list[dict],clave1 : str, clave2 : str)->dict:
    '''
    Esta funcion recibe un database, y devuelve un diccionario, donde la clave es un string (que representa a la clave1) y
    el valor es la cantidad de clave2 que le corresponde a la clave1
    estados_paquetes({}) == {}
    '''
    cantidades = {}

    for fila in database:
        palabra : str = fila[clave1]
        cantidad : int = int(fila[clave2])

        if palabra not in cantidades:
            cantidades[palabra] = cantidad
        else:
            cantidades[palabra] += cantidad
            
    return cantidades

def cuenta_cantidades_float(database : list[dict],clave1 : str, clave2 : str)->dict:
    '''
    Esta funcion recibe un database, y devuelve un diccionario, donde la clave es un string (que representa a la clave1) y
    el valor es la cantidad de clave2 que le corresponde a la clave1
    estados_paquetes({}) == {}
    '''
    cantidades = {}

    for fila in database:
        palabra : str = fila[clave1]
        cantidad : float = float(fila[clave2])

        if palabra not in cantidades:
            cantidades[palabra] = cantidad
        else:
            cantidades[palabra] += cantidad
            
    return cantidades

