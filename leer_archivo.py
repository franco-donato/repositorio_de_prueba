## leer_archivo.py
import csv
import streamlit as st

def crear_diccionario_interno(fila):

    indice = 0

    columnas = ["Ship Mode","Segment","Country","City","State","Postal Code",
    "Region","Category","Sub-Category","Sales","Quantity","Discount","Profit","Latitude","Longitude"]

    diccionaro_interno = {}

    for valor in fila:

        diccionaro_interno[columnas[indice]] = fila[indice]
        indice+=1
    return diccionaro_interno

        
