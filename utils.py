def calcular_valor_libros(costo, depreciaciones):
    valores = []
    acumulado = 0
    for d in depreciaciones:
        acumulado += d
        valores.append(costo - acumulado)
    return valores
