#resolucion_pregunta6.py

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
