# Importamos las funciones necesarias de matplotlib para poder hacer el grafico torta:
import matplotlib.pyplot as plt


def cuenta_segments(database : list[dict])->dict:
    '''
    la función toma un data_set, es decir, un diccionario donde las claves son enteros y los valores son diccionarios
    que representa a cada fila del data_set, y devuelve un diccionario donde las claves son los segmentos y los valores son
    la cantidad de ventas que se realizo a cada segmento.
    cuenta_segments({}) == {}
    '''
    cantidades : dict = {}

    for fila in database:

        segment : str = fila["Segment"]
        quantity : int = int(fila["Quantity"])

        if segment not in cantidades:

            cantidades[segment] = quantity

        else: cantidades[segment] += quantity

    return cantidades


def division_para_porcentaje(valor : int, total : int)-> int:
    '''
    la funcion toma dos numeros enteros (valor y total) y devuelve el resultado de redondear la division de valor entre total.
    division_para_porcentaje(12,0) == 0
    division_para_porcentaje(12,4) == 3
    division_para_porcentaje(13,4) == 3
    division_para_porcentaje(7,4) == 2
    '''
    if total == 0:
        resultado : int = 0
    else:    
        resultado : int = round((valor * 100)/total)
        
    return resultado
    


def calcula_porcentaje(segmentos : dict)->list:
    '''
    esta funcion recibe un diccionario, donde las claves son strings que representan a los segmentos y los valores
    son numeros enteros que representan la cantidad de ventas que se realizaron a cada segmento. Y devuelve una lista donde sus elementos son
    el porcentaje de ventas que se realizaron a cada segmento, este porcentaje se calcula con una regla de 3 simple,
    donde total es un entero que representa al total de las ventas realizadas (i,e: el 100% de las ventas)
    calcula_porcentaje({"Consumer":3,"Corporate":6,"Home Office":1}) == [30,60,10]
    calcula_porcentaje({}) == []
    '''
    cantidades : list = list(segmentos.values())

    porcentajes : list[int] = []

    total : int = 0
    for valor in cantidades:
        total = total + valor
    
    for valor in cantidades:
        porcentaje = division_para_porcentaje(valor,total)
        porcentajes.append(porcentaje)
    
    return porcentajes

def segment_y_cantidad(segmentos:dict)->list:
    '''
    esta funcion recibe un diccionario, donde las claves son strings que representan a los segmentos y los valores
    son numeros enteros que representan la cantidad de ventas que se realizaron a cada segmento. y devuelve una lista tal que 
    los elementos de esta son strings que representan las claves de segmentos y entre parentesis, las ventas realizadas.
    segment_y_cantidad({})==[]
    segment_y_cantidad({'Consumer': 19521, 'Corporate': 11608, 'Home Office': 6744})==["Consumer (19521)","Corporate (11608)","HOme Office (6744)"]
    '''
    nombres : list[str] = []
    for clave in segmentos:
        titulo = clave+" ("+str(segmentos[clave])+")"
        nombres.append(titulo)
    return nombres



def genera_grafico(database : list[dict]):
    '''
    la función toma un data_set, y genera un grafico de barras utilizando las funciones: plt.subplots(), ax.pie() de matplotlib
    
    '''
    segments : dict = cuenta_segments(database)
    nombres : list[str] = segment_y_cantidad(segments)
    porcentajes : list[int] = calcula_porcentaje(segments)
    colores : list[str] = ["#2612D8","#0EE92B","#F3FE5C"]
    fig, ax = plt.subplots()
    ax.pie(porcentajes,labels=nombres,colors = colores)

    
    return fig
