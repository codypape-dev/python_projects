import math


def vel_en_caida_libre(altura: float) -> float:
    vf = math.sqrt(altura*2*9.8)
    return round(vf, 2)

def calcular_edad(dia_nacio: int, mes_nacio: int, anio_nacio:int, dia_actual: int, mes_actual: int, anio_actual:int) -> str:

    dif_anio = anio_actual - anio_nacio

    if mes_nacio > mes_actual and dif_anio > 0:
        dif_anio -= 1
        dif_mes = 12 + (mes_actual - mes_nacio)
    else:
        dif_mes = mes_actual - mes_nacio

    if dia_nacio > dia_actual and dif_mes > 0:
        dif_mes -= 1
        dif_dia = 30 + (dia_actual - dia_nacio)
    else:
        dif_dia = dia_actual - dia_nacio

    return str(dif_anio) + ',' + str(dif_mes) + ',' + str(dif_dia)

print(calcular_edad(20,11,1986,16,10,1987))
