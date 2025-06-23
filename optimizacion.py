from metodos import linea_recta, saldo_decreciente, suma_digitos, unidad_produccion


def evaluar_metodos(activo, criterio="fiscal"):
    resultados = {}
    metodos = {
        "Línea Recta": linea_recta,
        "Saldo Decreciente": saldo_decreciente,
        "Suma Dígitos": suma_digitos,
        "Unidad Producción": unidad_produccion
    }

    for nombre, metodo in metodos.items():
        if nombre == "Unidad Producción":
            depreciaciones = metodo(activo.costo, activo.valor_residual, activo.produccion)
        else:
            depreciaciones = metodo(activo.costo, activo.valor_residual, activo.vida)

        if criterio == "fiscal":
            score = sum(depreciaciones[:3])  # depreciación acelerada
        elif criterio == "contable":
            media = sum(depreciaciones) / len(depreciaciones)
            score = -sum([(d - media) ** 2 for d in depreciaciones])  # menor variabilidad
        else:
            score = 0
        resultados[nombre] = (score, depreciaciones)

    mejor = max(resultados, key=lambda x: resultados[x][0])
    return mejor, resultados[mejor][1]
