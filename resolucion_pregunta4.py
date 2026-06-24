# resolucion_pregunta4.py
#¿Cuales fueron las ganancias de cada región y cuál fue la ciudad que realizó más compras?

def diccionario_ciudad(dataset):
    '''
    
    '''
    
    ciudades = {}
    
    for clave in dataset:
        fila = dataset[clave]
        ciudad = fila["City"]
        sales = float(fila["Sales"])

        if ciudad not in ciudades:
            ciudades[ciudad] = sales
        else: ciudades[ciudad] += sales
    return ciudades

def mayor_sales(dict):
    '''

    '''
    ventas = 0

    for city in dict:
        if dict[city] > ventas:
            ventas = dict[city]
            mayor_ciudad = city
    return (mayor_ciudad,ventas)

def ganancias_region(dataset):
    '''

    '''
    ganancias = {}
    
    for clave in dataset:

        fila = dataset[clave]
        region = fila["Region"]
        ganancia = float(fila["Profit"])

        if region not in ganancias:

            ganancias[region] = ganancia

        else: ganancias[region] += ganancia

    return ganancias