def contar_envios(database : list[dict], estado : str)->dict:
    '''
    Estado: es un string que representa un Estado de USA.
    La función recibe un database y un Estado y devuelve las cantidades de cada tipo de envío que se hayan
    utilizado para transportar la mercadería al Estado seleccionado.
    Esta función se diseñó para mostrar las cantidades de cada tipo de envío a cada Estado. Es decir,
    muestra cuantos envíos se hicieron por Standar Class, cuantos por First Class, cuantos por Second
    Class y cuantos por Same Day.
    Ejemplos:
    test_contar_envios( ):
    test_contar_envios( ):
    test_contar_envios( ):
    '''
    cantidades : dict = {'Standard Class': 0, 'First Class': 0, 'Second Class': 0, 'Same Day': 0}

    
    for fila in database:

        ship_mode : str = fila["Ship Mode"]
        state : str = fila["State"]

        if estado == state:
            cantidades[ship_mode] +=1
        
        
    return cantidades

def lista_estados_disponibles(database : list[dict])->list[str]:
    '''
    La función recibe un database y devuelve que Estados están en el archivo.
    La función fue diseñada para obtener los Estados nombrados en la tabla de la 
    superstore.
    Ejemplos:
    test_lista_estados_disponibles( ):
    test_lista_estados_disponibles( ):
    test_lista_estados_disponibles( ):
    '''
    estados_disponibles : list[str] = []
    for fila in database:
        state : str = fila["State"]
        if state not in estados_disponibles:
            estados_disponibles.append(state)
    return estados_disponibles

def lat_lon_estado(database : list[dict],estado : str)->dict:
    '''
    La función recibe un database y un Estado y devuelve las coordenadas de el mismo.
    Diseñamos esta función para saber las latitudes y longitudes de cada Estado
    Ejemplos:
    test_lat_lon_estado( ):
    test_lat_lon_estado( ):
    test_lat_lon_estado( ):
    '''
    coordenadas : dict = {}
    for fila in database:
        state : str = fila["State"]
        
        if state == estado:
            longitud : float = float(fila["Longitude"])
            latitud : float = float(fila["Latitude"])
            
            coordenadas["lat"] = [latitud]
            coordenadas["lon"] = [longitud]
            break

    return coordenadas

