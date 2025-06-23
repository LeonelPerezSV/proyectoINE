import matplotlib.pyplot as plt
from activos import Activo
from optimizacion import evaluar_metodos

# Datos de ejemplo
activo = Activo(
    costo=100000,
    valor_residual=10000,
    vida=10,
    produccion=[1000, 950, 900, 850, 800, 750, 700, 650, 600, 550]
)

criterio = "fiscal"  # o "contable"

mejor, depreciaciones = evaluar_metodos(activo, criterio)

print(f"Mejor método según criterio '{criterio}': {mejor}")
print("Depreciación anual:")
for i, dep in enumerate(depreciaciones, start=1):
    print(f"Año {i}: ${dep:,.2f}")

plt.plot(depreciaciones, marker='o')
plt.title(f"Depreciación usando: {mejor}")
plt.xlabel("Año")
plt.ylabel("Valor depreciado")
plt.grid(True)
plt.show()