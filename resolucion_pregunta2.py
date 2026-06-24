# resolucion_pregunta2.py 
def paquetes_por_estado(estado : str,diccionario : dict)->int:
    '''
    Estado: Es un string y representa un Estado de Estados Unidos.
    La función recibe un Estado (string) y un diccionario y devuelve los tres Estados que hayan recibido más paquetes
    y la cantidad de los mismos (un número entero).
    Hicimos esta función para determinar cuáles, de entre los 50 Estados de USA, fueron los tres que más paquetes
    recibieron y cuántos fueron.
    Ejemplos:
    test_paquetes_por_estado( ):
    test_paquetes_por_estado( ):
    test_paquetes_por_estado( ):
    '''
    contador_estado : int = 0
    contador_estado += int(diccionario["Quantity"])

    return contador_estado
