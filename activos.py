class Activo:
    def __init__(self, costo, valor_residual, vida, produccion=None):
        self.costo = costo
        self.valor_residual = valor_residual
        self.vida = vida
        self.produccion = produccion or [1]*vida  # default producción uniforme
