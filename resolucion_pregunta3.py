#resolucion_pregunta3.py
def contar_envios(database, estado):
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
    cantidades = {'Standard Class': 0, 'First Class': 0, 'Second Class': 0, 'Same Day': 0}

    
    for clave in database:

        valores = database[clave]
        ship_mode = valores["Ship Mode"]
        state = valores["State"]

        if estado == state:
            cantidades[ship_mode] +=1
        
        
    return cantidades

def lista_estados_disponibles(database):
    '''
    La función recibe un database y devuelve que Estados están en el archivo.
    La función fue diseñada para obtener los Estados nombrados en la tabla de la 
    superstore.
    Ejemplos:
    test_lista_estados_disponibles( ):
    test_lista_estados_disponibles( ):
    test_lista_estados_disponibles( ):
    '''
    estados_disponibles= []
    for clave in database:
        fila = database[clave]
        state = fila["State"]
        if state not in estados_disponibles:
            estados_disponibles.append(state)
    return estados_disponibles

def lat_lon_estado(database,estado):
    '''
    La función recibe un database y un Estado y devuelve las coordenadas de el mismo.
    Diseñamos esta función para saber las latitudes y longitudes de cada Estado
    Ejemplos:
    test_lat_lon_estado( ):
    test_lat_lon_estado( ):
    test_lat_lon_estado( ):
    '''
    coordenadas ={}
    for clave in database:
        fila = database[clave]
        state = fila["State"]
        
        if state == estado:
            longitud = float(fila["Longitude"])
            latitud = float(fila["Latitude"])
            
            coordenadas["lat"] = [latitud]
            coordenadas["lon"] = [longitud]
            break

    return coordenadas
