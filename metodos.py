def linea_recta(costo, valor_residual, vida):
    anual = (costo - valor_residual) / vida
    return [anual] * vida

def saldo_decreciente(costo, valor_residual, vida, factor=2):
    valor_libros = costo
    depreciaciones = []
    for _ in range(vida):
        dep = valor_libros * (factor / vida)
        valor_libros -= dep
        if valor_libros < valor_residual:
            dep += valor_libros - valor_residual
            valor_libros = valor_residual
        depreciaciones.append(round(dep, 2))
    return depreciaciones

def suma_digitos(costo, valor_residual, vida):
    suma = sum(range(1, vida + 1))
    base = costo - valor_residual
    return [base * (vida - i) / suma for i in range(vida)]

def unidad_produccion(costo, valor_residual, produccion_anual):
    total = sum(produccion_anual)
    base = costo - valor_residual
    return [base * (año / total) for año in produccion_anual]
