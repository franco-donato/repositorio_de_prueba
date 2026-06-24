def ventas_ganancias(ciudad:str,data_base:dict)->tuple:
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
    test_ventas_ganabcias( ):
    '''
    contador_quantity : int = 0
    ganancias : int = 0
    for fila in data_base:
        if ciudad == data_base["City"]:
            contador_quantity += int(data_base["Quantity"])
            ganancia += float(data_base["Profit"])
    return (contador_quantity,ganancias)
