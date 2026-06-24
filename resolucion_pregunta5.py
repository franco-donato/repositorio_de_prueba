def mayor_el_lista(lista:list)->int:
    '''
    La función recibe una lista de numeros enteros y retorna el mayor elemento.
    Diseñamos esta función para que dada una lista, nos devuelva el mayor elemento de la misma.
    Ejemplos:
    test_mayor_el_lista( ):
    test_mayor_el_lista( ):
    test_mayor_el_lista( ):
    '''
    mayor = 0
    for elemento in list:
        if elemento > mayor:
            mayor = elemento
    return mayor


def contador_subcategoria_furniture(data_base:dict)-> int:
    '''
    La función recibe un database y devuelve la cantidad de ventas de cada una de las subcategorías de la
    categoría Furniture.
    Esta función se va a usar para saber con exactitud cuantas ventas se realizaron de cada una de las subcategorías
    (bookcases, chairs, tables y furnishings) de la categoría Furniture, para luego conocer cuál fue la que tuvo más
    ventas.
    Ejemplos:
    contador_subcategoria_furniture( ):
    contador_subcategoria_furniture( ):
    contador_subcategoria_furniture( ):
    '''
    contador_bookcases : int = 0
    contador_chairs : int = 0
    contador_tables : int = 0
    contador_furnishings : int = 0
    for fila in data_base:
        if fila["Sub-Category"] == "Bookcases":
            contador_bookcases += fila["Quantity"]
        elif fila["Sub-Category"] == "Chairs":
            contador_chairs += fila["Quantity"]
        elif fila["Sub-Category"] == "Tables":
            contador_tables += fila["Quantity"]
        elif fila["Sub-Category"] == "Furnishings":
            contador_furnishings += fila["Quantity"]
    lista_de_contadores = [contador_bookcases,contador_chairs,contador_tables,contador_furnishings]


    return mayor_el_lista(lista_de_contadores)

def contador_subcategoria_technology(data_base:dict)-> int:
    '''
    La función recibe un database y devuelve la cantidad de ventas de cada una de las subcategorías de la
    categoría Technology.
    Esta función se va a usar para saber con exactitud cuantas ventas se realizaron de cada una de las subcategorías
    (phones y accessories) de la categoría Technology, para luego conocer cuál fue la que tuvo más
    ventas.
    Ejemplos:
    contador_subcategoria_technology( ):
    contador_subcategoria_technology( ):
    contador_subcategoria_technology( ):
    '''
    contador_phones : int = 0
    contador_accessories : int = 0
    for fila in data_base:
        if fila["Sub-Category"] == "Phones":
            contador_phones += fila["Quantity"]
        elif fila["Sub-Category"] == "Accessories":
            contador_accessories += fila["Quantity"]
    
    lista_de_contadores = [contador_phones,contador_accessories]

    return mayor_el_lista(lista_de_contadores)


def contador_subcategoria_officesupplies(data_base:dict)-> int:
    '''
    La función recibe un database y devuelve la cantidad de ventas de cada una de las subcategorías de la
    categoría Office Supplies.
    Esta función se va a usar para saber con exactitud cuantas ventas se realizaron de cada una de las subcategorías
    (storage, art, labels, binders, appliances, paper, envelopes y fasteners) de la categoría Office Supplies, para luego 
    conocer cuál fue la que tuvo más ventas.
    Ejemplos:
    contador_subcategoria_officesupplies( ):
    contador_subcategoria_officesupplies( ):
    contador_subcategoria_officesupplies( ):
    '''
    contador_storage : int = 0
    contador_art : int = 0
    contador_labels : int = 0
    contador_binders : int = 0
    contador_appliances : int = 0
    contador_paper : int = 0
    contador_envelopes : int = 0
    contador_fasteners : int = 0
    for fila in data_base:
        if fila["Sub-Category"] == "Storage":
            contador_storage += fila["Quantity"]
        elif fila["Sub-Category"] == "Art":
            contador_art += fila["Quantity"]
        elif fila["Sub-Category"] == "Labels":
            contador_labels += fila["Quantity"]
        elif fila["Sub-Category"] == "Binders":
            contador_binders += fila["Quantity"]
        elif fila["Sub-Category"] == "Appliances":
            contador_appliances += fila["Quantity"]
        elif fila["Sub-Category"] == "Paper":
            contador_paper += fila["Quantity"]
        elif fila["Sub-Category"] == "Envelopes":
            contador_envelopes += fila["Quantity"]
        elif fila["Sub-Category"] == "Fasteners":
            contador_fasteners += fila["Quantity"]

    lista_de_contadores = [contador_storage,contador_art,contador_labels,contador_binders,contador_appliances,contador_paper,contador_envelopes,contador_fasteners]

    return mayor_el_lista(lista_de_contadores)


def mayor_subcategoria(categoria:str,data_base:dict):
    '''
    La función recibe una categoría y un database y devuelve la cantidad de ventas de la subcategoría más vendida
    de una categoría específica (un número entero) y también devuelve el nombre de la misma (string).
    Esta función fue hecha para que, dado un diccionario, devuelva cuantas ventas hubo de, y cuál es, la 
    subcategoría más vendida de una categoría elegida.
    Ejemplos:
    test_mayor_subcategoria( ):
    test_mayor_subcategoria( ):
    test_mayor_subcategoria( ):

    (falta modificar para que diga que subcategoria es la mas vendida,
    ahora devuelve solo la cantidad)
    '''
    retorno = 0
    if categoria == "Furniture":
        retorno = contador_subcategoria_furniture(data_base)
    
    elif categoria == "Office Supplies":
        retorno = contador_subcategoria_officesupplies(data_base)
    
    elif categoria == "Technology":
        retorno = contador_subcategoria_technology(data_base)

    return retorno