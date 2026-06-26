def cuenta_cantidades_enteras(database : list[dict],clave1 : str, clave2 : str)->dict:
    '''
    Esta funcion recibe un database, y dos strings, el primero, clave1, 
    representa al titulo de una columna del dataset,
    el segundo, clave2, es un string numerable (entero) que representa
    a la columna del dataset a la cual se le suman las cantidades
    y devuelve un diccionario, donde la clave es un string (que representa a la clave1) y
    el valor es la cantidad de clave2 que le corresponde a la clave1
    estados_paquetes({},"State","Quantity") == {}
    estados_paquetes(ArchivoParaTesting.csv,"City","Quantity") == {"Henderson":5,"Los Angeles":24,"Fort Lauderdale":7}
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
    Esta funcion recibe un database, y dos strings, el primero, clave1, 
    representa al titulo de una columna del dataset,
    el segundo, clave2, es un string numerable (entero) que representa
    a la columna del dataset a la cual se le suman las cantidades
    y devuelve un diccionario, donde la clave es un string (que representa a la clave1) y
    el valor es la cantidad de clave2 que le corresponde a la clave1
    estados_paquetes({},"Ship Mode","Sales") == {}
    estados_paquetes(ArchivoParaTesting.csv,"Ship Mode","Sales") == {"Second Class": 1008.52,"Standard Class": 2088.1375}
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

def cuenta_cantidades_subcategorias(database : list[dict],categoria : str, clave1 : str, clave2 : str) -> dict:
    '''
    Esta funcion recibe un database, y tres strings, el primero, categoria, representa a una Categoria del database
    el segundo, clave1, representa al titulo de una columna del dataset (una subcategoria en este caso),
    el tercero, clave2, es un string numerable (entero) que representa
    a la columna del dataset a la cual se le suman las cantidades
    y devuelve un diccionario, donde la clave es un string (que representa a la clave1) y
    el valor es la cantidad de clave2 que le corresponde a la clave1
    estados_paquetes({},"Furniture","Sub-Category","Quantity") == {}
    estados_paquetes(ArchivoParaTesting.csv,"Furniture","Sub-Category","Quantity") == {"Bookcases": 2,"Chairs": 3,"Tables": 5,"Furnishings": 7}
    '''

    cantidades : dict = {}

    for fila in database:

        if categoria == fila["Category"]:

            palabra : str = fila[clave1]
            cantidad : int = int(fila[clave2])

            if palabra not in cantidades:
                cantidades[palabra] = cantidad
            else:
                cantidades[palabra] += cantidad

    return cantidades