def estados_paquetes(database : list[dict])->dict:
    '''
    Esta funcion recibe un database, y devuelve un diccionario, donde la clave es un string (que representa a los estados) y
    el valor es la cantidad de paquetes que recibió cada estado.
    estados_paquetes({}) == {}
    '''
    cantidades : dict = {}
    for fila in database:
        state : str = fila["State"]
        quantity : int = int(fila["Quantity"])
        if state not in cantidades:
            cantidades[state] = quantity
        else: cantidades[state] += quantity
    return cantidades

def estado_que_mas_recibio(cantidades_estados : dict)->list:
    '''
    Esta funcion recibe un diccionario, donde la clave es un string (que representa a los estados) y
    el valor es la cantidad de paquetes que recibió cada estado y devuelve una lista, donde estado es el estado que mas paquetes recibio y 
    valor es la cantidad de paquetes recibidos.
    La funcion calcula cual es el estado que mas paquetes recibió.
    '''
    estado : str = ""
    valor : int = 0
    for clave in cantidades_estados:
        if cantidades_estados[clave] > valor:
            valor = cantidades_estados[clave]
            estado = clave
    return [estado, valor]

