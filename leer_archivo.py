import csv

def crear_diccionario_interno(fila):

    indice = 0

    columnas = ["Ship Mode","Segment","Country","City","State","Postal Code",
    "Region","Category","Sub-Category","Sales","Quantity","Discount","Profit","Latitude","Longitude"]

    diccionaro_interno = {}

    for valor in fila:

        diccionaro_interno[columnas[indice]] = fila[indice]
        indice+=1
    return diccionaro_interno

        


def leer_archivo(data_set):
    filas = []

    next(data_set)

    for linea in data_set:
        valores = linea.strip().split(',')
        diccionario_interno = crear_diccionario_interno(valores)
        filas.append(diccionario_interno)
        
        

    return filas

