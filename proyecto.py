import streamlit as st


st.title ("AGUANTE BOCA")
st.write ("EL ÚNICO GRANDE: C.A.B.J.")


def leer_archivo()->list:
    '''
    data_set : str
    fila : list[str]
    filas : list[fila]
    La funcion toma el archivo con exstension csv, es decir el data-set y lo representa como una 
    lista de filas, es decir, como una lista de listas de strings, donde cada string de la fila 
    representa a una columna del data-set
    '''
    data_set = open("SampleSuperstore_geo.csv")
    filas = []
    for linea in data_set:
        lista.append(linea.strip("\n").split(","))

    data_set.close()
    return filas

# funciones para la resolucion de la pregunta 6:

def ventas_segment(fila : list, segment : str)->tuple:
    '''
    fila : list[str]
    segment : str("Consumer","Corporate" o "Home Office")
    contador_segment : int
    la funcion, dada una fila, si el elemento en la posición 1 de la lista coincide
    con el string segment la función devuelve el elemento en la posicion 10 de la fila, que corresponde
    a la cantidad de ventas
    ejemplos:
    ventas_segment("Standard Class","Consumer","United States","Fort Lauderdale","Florida","33311",
    "South","Furniture","Tables","957.5775","5","0.45","-383.031,26.121561","-80.128778","") == -1
    ventas_segment("Standard Class","Consumer","United States","Fort Lauderdale","Florida","33311",
    "South","Furniture","Tables","957.5775","5","0.45","-383.031,26.121561","-80.128778","Consumer") == 1)
    ventas_segment([], "Consumer") == -1
    '''
    contador_segment = 0
    if len(fila) == 15:
        if fila[1] == segment:
            contador_segment += int(fila[10])
        else:
            contador_segment = -1
    else:
        contador_segment = -1

    return contador_segment

def test_ventas_segment():
    assert ventas_segment("Standard Class","Consumer","United States","Fort Lauderdale","Florida","33311","South","Furniture","Tables","957.5775","5","0.45","-383.031,26.121561","-80.128778","") == -1
    assert ventas_segment("Standard Class","Consumer","United States","Fort Lauderdale","Florida","33311","South","Furniture","Tables","957.5775","5","0.45","-383.031,26.121561","-80.128778","Consumer") == 1)
    assert ventas_segment([], "Consumer") == -1

def cuenta_ventas_segment(data_set:list)->tuple:
    '''
    cantidad_consumer : int
    cantidad_corporate : int
    cantidad_homeoffice : int
    tupla_cantidades : tupla(int)
    dada una lista de listas de strings (data-set) devuelve la cantidad de ventas de cada segmento,
    representadas en una tupla
    ejemplos
    '''
    cantidad_consumer = 0
    cantidad_corporate = 0
    cantidad_homeoffice = 0
    
    for fila in data_set:
        if fila[1] == "Consumer":
            cantidad_consumer = ventas_segment(fila,"Consumer")        
        elif fila[1] == "Consumer":
            cantidad_consumer = ventas_segment(fila,"Consumer")
        elif fila[1] == "Consumer":
            cantidad_consumer = ventas_segment(fila,"Consumer")
    
    tupla_cantidades = (cantidad_consumer,cantidad_corporate,cantidad_homeoffice)
    return tupla_cantidades

