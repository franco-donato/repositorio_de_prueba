#resolucion_pregunta6.py
import matplotlib.pyplot as plt


def cuenta_segments(database):

    cantidades = {}

    for clave in database:

        fila = database[clave]

        segment = fila["Segment"]

        quantity = int(fila["Quantity"])

        if segment not in cantidades:

            cantidades[segment] = quantity

        else: cantidades[segment] += quantity

    return cantidades


def division_para_porcentaje(numero : int, total : int)-> int:
    if total == 0:
        resultado = 0
    else:    
        resultado = round((numero * 100)/total)
        
    return resultado

def calcula_porcentaje(segmentos : dict)->list:

    cantidades : list = list(segmentos.values())

    porcentajes : list = []

    total : int = 0
    for valor in cantidades:
        total = total + valor
    
    for valor in cantidades:
        porcentaje = division_para_porcentaje(valor,total)
        porcentajes.append(porcentaje)
    
    return porcentajes



def genera_grafico(database : dict):
    segments = cuenta_segments(database)
    nombres = segments.keys()
    porcentajes = calcula_porcentaje(segments)
    colores = ["#4D05C9","#01A917","#F3FE5C"]
    fig, ax = plt.subplots()
    ax.pie(porcentajes,labels=nombres,colors = colores)

    
    return fig