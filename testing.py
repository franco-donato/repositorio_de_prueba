from resolucion_pregunta1 import *
from resolucion_pregunta2 import *
from resolucion_pregunta3 import *
from resolucion_pregunta4 import *
from resolucion_pregunta5 import *
from resolucion_pregunta6 import *


# TESTING FUNCIONES DEL ARCHIVO: "resolucion_pregunta6.py"


def test_division_para_porcentaje():   
    assert division_para_porcentaje(12,0) == 0
    assert division_para_porcentaje(12,4) == 3
    assert division_para_porcentaje(13,4) == 3
    assert division_para_porcentaje(7,4) == 2

def test_calcula_porcentaje():
    assert calcula_porcentaje({"Consumer":3,"Corporate":6,"Home Office":1}) == [30,60,10]
    assert calcula_porcentaje({}) == []


def test_segment_y_cantidad():
    assert segment_y_cantidad({})==[]
    assert segment_y_cantidad({'Consumer': 19521, 'Corporate': 11608, 'Home Office': 6744})==["Consumer (19521)","Corporate (11608)","HOme Office (6744)"]
    