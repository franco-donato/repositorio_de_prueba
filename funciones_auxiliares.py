def funcion_auxiliar(database : list[dict],clave1 : str, clave2 : str)->dict:
    '''
    Esta funcion recibe un database, y devuelve un diccionario, donde la clave es un string (que representa a los estados) y
    el valor es la cantidad de paquetes que recibió cada estado.
    estados_paquetes({}) == {}
    '''
    cantidades : dict = {}
    for fila in database:

        palabra : str = fila[clave1]
        cantidad = fila[clave2]

        if palabra not in cantidades:
            cantidades[palabra] = cantidad
        else: cantidades[palabra] += cantidad

    return cantidades