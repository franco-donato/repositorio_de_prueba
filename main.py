# Importamos el codigo principal

from leer_archivo import *
from resolucion_pregunta3 import *
from resolucion_pregunta5 import *
from resolucion_pregunta6 import *
import streamlit as st




def main():
    '''
    Estamos teniendo complicaciones en cuanto a usar streamlit, tanto para el grafico de torta, como
    para el mapa. Intentamos buscar en la documentacion, pero no encontramos solucion. Sin embargo, 
    las funciones deberian funcionar correctamente, lo que nos faltaria es controlar la salida y 
    entrada de datos por el main, y la elaboracion de la pagina.

    '''
    archivo_csv = leer_archivo()
    #pregunta 3
    estado = st.selectbox("Seleccione un estado: ", lista_estados_disponibles(archivo_csv))

    mostrar_estado = lat_lon_estado(archivo_csv, estado)
    mostrar_estado["color"] = ["#FFA500"]

    st.map(mostrar_estado, latitude = "lat", longitude = "lon", color = "color")

    st.table(contar_envios(archivo_csv,estado))
    
    # RESOLUCION_PREGUNTA5
    st.title("SUBCATEGORIA MAS VENDIDA")
    
    subcategoria = st.radio(
        "Selecciona una categoria:",
        ["Furniture","Technology","Office Supplies"]
    )

    st.write(mayor_subcategoria(subcategoria,leer_archivo()))
    # RESOLUCION_PREGUNTA6

    st.title("VENTAS POR SEGMENTOS")
    grafico_torta = genera_grafico(archivo_csv)
    st.pyplot(grafico_torta)

    return 0


if __name__ == '__main__':
    main()