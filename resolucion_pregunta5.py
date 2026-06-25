def subcategoria_mas_vendida(diccionario : dict)->dict:
    '''
    Esta funcion recibe un diccionario donde las claves son strings (que representan a las subcategorias) y los valores son numeros enteros
    (que representan la cantidad de ventas de cada subcategoria), y devuelve un diccionario donde la clave es la subcategoria mas vendida
    y el valor es la cantidad de ventas de esta
    Ejemplos:
    subcategoria_mas_vendida( ):
    subcategoria_mas_vendida( ):
    subcategoria_mas_vendida( ):
    '''
    subcategoria_mas_vendida : dict = {}
    valor_mayor : int = 0
    subcategoria : str = ""
    for subcategoria in diccionario:
        if diccionario[subcategoria] > valor_mayor:
            valor_mayor = diccionario[subcategoria]
            clave = subcategoria
    
    subcategoria_mas_vendida[clave] = valor_mayor
    return subcategoria_mas_vendida


def contador_subcategoria_furniture(database:list[dict])-> int:
    '''
    La función recibe un database y devuelve un diccionario donde la clave es la subcategoria mas vendida de la categoria furniture y 
    la cantidad de ventas su valor.
    Esta función se va a usar para saber con exactitud cuantas ventas se realizaron de cada una de las subcategorías
    (bookcases, chairs, tables y furnishings) de la categoría Furniture, para luego conocer cuál fue la que tuvo más
    ventas.
    Ejemplos:
    contador_subcategoria_furniture( ):
    contador_subcategoria_furniture( ):
    contador_subcategoria_furniture( ):
    '''
    subcategorias : dict = {"Bookcases":0,"Chairs":0,"Tables":0,"Furnishings":0}
    
    for fila in database:

        if fila["Sub-Category"] == "Bookcases":
            subcategorias["Bookcases"] += int(fila["Quantity"])
        elif fila["Sub-Category"] == "Chairs":
            subcategorias["Chairs"] += int(fila["Quantity"])
        elif fila["Sub-Category"] == "Tables":
            subcategorias["Tables"] += int(fila["Quantity"])
        elif fila["Sub-Category"] == "Furnishings":
            subcategorias["Furnishings"] += int(fila["Quantity"])


    return subcategoria_mas_vendida(subcategorias)

def contador_subcategoria_technology(database:list[dict])-> int:
    '''
    La función recibe un database y devuelve un diccionario donde la clave es la subcategoria mas vendida de la categoria technology y 
    la cantidad de ventas su valor.
    Esta función se va a usar para saber con exactitud cuantas ventas se realizaron de cada una de las subcategorías
    (phones y accessories) de la categoría Technology, para luego conocer cuál fue la que tuvo más
    ventas.
    Ejemplos:
    contador_subcategoria_technology( ):
    contador_subcategoria_technology( ):
    contador_subcategoria_technology( ):
    '''
    subcategorias : dict = {"Phones":0,"Accessories":0}
    
    for fila in database:


        if fila["Sub-Category"] == "Phones":
            subcategorias["Phones"] += int(fila["Quantity"])
        elif fila["Sub-Category"] == "Accessories":
            subcategorias["Accessories"] += int(fila["Quantity"])
    

    return subcategoria_mas_vendida(subcategorias)


def contador_subcategoria_officesupplies(database:list[dict])-> int:
    '''
    La función recibe un database y devuelve un diccionario donde la clave es la subcategoria mas vendida de la categoria Office Supplies y 
    la cantidad de ventas su valor.
    Esta función se va a usar para saber con exactitud cuantas ventas se realizaron de cada una de las subcategorías
    (storage, art, labels, binders, appliances, paper, envelopes y fasteners) de la categoría Office Supplies, para luego 
    conocer cuál fue la que tuvo más ventas.
    Ejemplos:
    contador_subcategoria_officesupplies( ):
    contador_subcategoria_officesupplies( ):
    contador_subcategoria_officesupplies( ):
    '''
    subcategorias={"Storage":0,"Art":0,"Labels":0,"Binders":0,"Appliances":0,"Paper":0,"Envelopes":0,"Fasteners":0}
    
    for fila in database:

        if fila["Sub-Category"] == "Storage":
            subcategorias["Storage"] += int(fila["Quantity"])
        elif fila["Sub-Category"] == "Art":
            subcategorias["Art"] += int(fila["Quantity"])
        elif fila["Sub-Category"] == "Labels":
            subcategorias["Labels"] += int(fila["Quantity"])
        elif fila["Sub-Category"] == "Binders":
            subcategorias["Binders"] += int(fila["Quantity"])
        elif fila["Sub-Category"] == "Appliances":
            subcategorias["Appliances"] += int(fila["Quantity"])
        elif fila["Sub-Category"] == "Paper":
            subcategorias["Paper"] += int(fila["Quantity"])
        elif fila["Sub-Category"] == "Envelopes":
            subcategorias["Envelopes"] += int(fila["Quantity"])
        elif fila["Sub-Category"] == "Fasteners":
            subcategorias["Fasteners"] += int(fila["Quantity"])

    return subcategoria_mas_vendida(subcategorias)


def mayor_subcategoria(categoria:str,data_base:list[dict])-> str:
    '''
    La función recibe una categoría y un database y un string en el que se especifica la subcategoria mas vendida, y la cantidad
    de ventas de esta.
    Esta función fue hecha para que, dado un diccionario, devuelva cuantas ventas hubo de, y cuál es, la 
    subcategoría más vendida de una categoría elegida.
    Ejemplos:
    test_mayor_subcategoria( ):
    test_mayor_subcategoria( ):
    test_mayor_subcategoria( ):
    '''
    retorno : str = ""
    if categoria == "Furniture":
        subcategoria : dict = contador_subcategoria_furniture(data_base)    
    elif categoria == "Office Supplies":
        subcategoria : dict = contador_subcategoria_officesupplies(data_base)
    elif categoria == "Technology":
        subcategoria : dict = contador_subcategoria_technology(data_base)

    for clave in subcategoria:
        retorno = "La subcategoria mas vendida es: "+clave+" y la cantidad de ventas es: "+str(subcategoria[clave])
         
    return retorno