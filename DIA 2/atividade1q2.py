import math
def numeroR(numero2: float):
    floor = math.floor(numero2)
    ceiling = math.ceil(numero2)
    arredondar = round(numero2)
    return floor, ceiling, arredondar

print(numeroR(8.96))