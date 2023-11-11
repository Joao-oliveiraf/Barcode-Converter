# Calculadora de volumes
# Cilindro base reta, base cone fina e base cone reta
# M2 de cubo
# Area retangulo M2

import math
from funcs import validation


# cilindro
def cilindro_breta(dim, h):
    area = math.pi * math.pow((dim / 2), 2) * h
    return area


def cilindro_bconefina(dim, h1_cilindro, h2_cone):
    area_cone = (math.pi * math.pow((dim / 2), 2) * h2_cone) / 3
    area_cil = (math.pi * math.pow((dim / 2), 2) * h1_cilindro)
    area = sum(area_cil, area_cone)
    return area


def cilindro_bconereta(dim_maior, dim_menor, h1, h2, ):
    dim_maior /= 2
    dim_menor /= 2
    cil = cilindro_breta(dim=dim_maior, h=h1)
    area = ((math.pi * h2) / 3) * (math.pow(dim_maior, 2) + dim_maior * dim_menor + math.pow(dim_menor, 2))
    return cil + area


def retangulo(depth, width, height):
    return depth * width * height

