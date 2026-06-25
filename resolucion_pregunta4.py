#¿Cuales fueron las ganancias de cada región y cuál fue la ciudad que realizó más compras?

def diccionario_ciudad(dataset : list[dict])->dict:
    '''
    Esta funcion recibe un dataset, y devuelve un diccionario, donde las claves son strings (que representan a las ciudades) y
    los valores son float (que representa a las ventas).

    '''
    
    ciudades : dict = {}
    
    for fila in dataset:
        ciudad : str = fila["City"]
        sales : float = float(fila["Sales"])

        if ciudad not in ciudades:
            ciudades[ciudad] = sales
        else: ciudades[ciudad] += sales
    return ciudades

def mayor_sales(diccionario : list[dict])->tuple:
    '''
    Esta funcion recibe un diccionario, donde las claves son str (que representan a las ciudades) y los valores son
    valores numericos, float o int(que representan a las ventas) y devuelve una tupla donde el primer valor es la ciudad
    y el segundo es la cantidad de ventas.
    esta funcion determina la ciudad con la mayor cantidad de ventas.
    '''
    ventas = 0

    for city in diccionario:
        if diccionario[city] > ventas:
            ventas = diccionario[city]
            mayor_ciudad : str = city
    return (mayor_ciudad,ventas)

def ganancias_region(dataset: list[dict])-> dict:
    '''
    Esta funcion recibe un dataset y devuelve un diccionario, donde las claves son str (que representan a las regiones) y
    los valores son float (que representan a las ganancias de cada region).
    
    '''
    ganancias : dict = {}
    
    for fila in dataset:

        region : str = fila["Region"]
        ganancia : float = float(fila["Profit"])

        if region not in ganancias:

            ganancias[region] = ganancia

        else: ganancias[region] += ganancia

    return ganancias
