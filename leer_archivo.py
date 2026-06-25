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

        


def leer_archivo():
    data_set = open("SampleSuperstore_geo.csv")
    filas = {}
    clave = 1
    next(data_set)

    for linea in data_set:
        valores = linea.strip().split(',')
        diccionario_interno = crear_diccionario_interno(valores)

        filas[clave] = diccionario_interno
        clave +=1
        
    data_set.close()
    return filas

