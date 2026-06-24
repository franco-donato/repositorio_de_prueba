def ciudades(dataset):

    ciudades : list[str] = []

    for clave in dataset:
        fila = dataset[clave]
        ciudad = fila["City"]
        if ciudad not in ciudades:
            ciudades.append(ciudad)

    return ciudades


def ventas_ganancias(ciudad:str,database : dict)->tuple:
    '''
    ciudad: string
    ciudad: representa una ciudad de Estados Unidos
    La función toma una ciudad de USA y un database y devuelve una tupla con la 
    cantidad de ventas y sus respectivas ganancias.
    Esta función se diseñó para calcular las ventas destinadas a una ciudad
    específica y las ganancias que generaron las mismas.
    Ejemplos;
    test_ventas_ganancias( ):
    test_ventas_ganancias( ):
    test_ventas_ganancias( ):
    '''
    contador_quantity : int = 0
    ganancias : float = 0.0
    for clave_fila in database:
        fila : dict = database[clave_fila]
        if ciudad == fila["City"]:
            contador_quantity = contador_quantity + int(fila["Quantity"])
            ganancias += float(fila["Profit"])

    return (contador_quantity,round(ganancias,2))

