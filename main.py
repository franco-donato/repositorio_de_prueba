#Importamos el codigo principal
from leer_archivo import *

from resolucion_pregunta1 import *
from resolucion_pregunta2 import *
from resolucion_pregunta3 import *
from resolucion_pregunta4 import *
from resolucion_pregunta5 import *
from resolucion_pregunta6 import *
import streamlit as st




def main():
    '''

    '''
    data_set = open("SampleSuperstore_geo.csv")
    archivo_csv = leer_archivo(data_set)

    data_set.close()

    # --------------------------------------------------------------
    st.title("Proyecto Superstore Norteamericana- Grupo 9")
    # PREGUNTA 1:
    st.subheader("1. PAQUETES ENVIADOS Y GANANCIA POR CIUDAD")

    accion = st.menu_button("Selecciona una ciudad",options=ciudades(archivo_csv))
    
    cantidad_de_paquetes,ganancias = ventas_ganancias(accion,archivo_csv)

    tabla = {
    "Paquetes enviados":[cantidad_de_paquetes],
    "Ganancia":[ganancias]
    }
    st.table(tabla)


    # --------------------------------------------------------------
    # PREGUNTA 2
    st.subheader("2. El Estado que mas paquetes recibió")
    nombre_valor = estado_que_mas_recibio(estados_paquetes(archivo_csv))
    nombre_estado =nombre_valor[0]
    valor_estado = nombre_valor[1]

    st.success(f"El estado que mas paquetes recibio es **{nombre_estado}** con un total de **{valor_estado}** paquetes recibidos.")

    coordenadas_pregunta2 = lat_lon_estado(archivo_csv,nombre_estado)
    coordenadas_pregunta2["color"] = ["#FF0000"]
    st.map(coordenadas_pregunta2, latitude="lat", longitude="lon", color="color")
    

    # --------------------------------------------------------------
    # PREGUNTA 3
    st.subheader("3. Tipos de envio por estado")
    estado_pregunta3 = st.selectbox("Seleccione un estado: ", lista_estados_disponibles(archivo_csv))
    
    mostrar_estado = lat_lon_estado(archivo_csv, estado_pregunta3)
    mostrar_estado["color"] = ["#FFA500"]

    st.map(mostrar_estado, latitude = "lat", longitude = "lon", color = "color")

    st.table(contar_envios(archivo_csv,estado_pregunta3))


    # --------------------------------------------------------------
    # PREGUNTA 4
    st.subheader("4. Ganancias totales de cada region y ciudad que mas ventas realizó")

    ganancias_pregunta4= ganancias_region(archivo_csv)

    st.bar_chart(ganancias_pregunta4)
    ciudad_mayor_venta = mayor_sales(diccionario_ciudad(archivo_csv))
    
    st.metric(label="ciudad con más ventas", value= str(ciudad_mayor_venta[0]), delta=str(ciudad_mayor_venta[1]))
    

    # --------------------------------------------------------------
    # PREGUNTA 5:
    st.subheader("5. SUBCATEGORIA MAS VENDIDA")
    
    subcategoria = st.radio(
        "Selecciona una categoria:",
        ["Furniture","Technology","Office Supplies"]
    )

    st.write(mayor_subcategoria(subcategoria,archivo_csv))


    # --------------------------------------------------------------
    #PREGUNTA 6:

    st.subheader("6. VENTAS POR SEGMENTOS")
    grafico_torta = genera_grafico(archivo_csv)
    st.pyplot(grafico_torta)

    return 0
    

if __name__ == '__main__':
    main()