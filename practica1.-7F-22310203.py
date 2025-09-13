# Regresion_Lineal_VidaDiaria.py
# Ejemplo aplicado a la vida cotidiana: horas de estudio vs puntaje en examen

import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo: horas de estudio (x) vs puntaje en examen (y)
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([35, 50, 55, 65, 70, 75, 80, 85, 90, 95])

# Ajuste de regresión lineal: y = a*x + b
X = np.vstack([x, np.ones(len(x))]).T
a, b = np.linalg.lstsq(X, y, rcond=None)[0]

# Predicciones
y_pred = a * x + b

# Mostrar resultados
print("Modelo de regresión lineal aplicado a horas de estudio")
print(f"Ecuación: y = {a:.2f} * x + {b:.2f}")
horas = 7
print(f"Predicción para {horas} horas de estudio: {a*horas + b:.2f} puntos")

# Graficar datos y la recta ajustada
plt.scatter(x, y, color="blue", label="Datos reales")
plt.plot(x, y_pred, color="red", label="Recta ajustada")
plt.xlabel("Horas de estudio")
plt.ylabel("Puntaje en examen")
plt.title("Relación entre horas de estudio y puntaje")
plt.legend()
plt.grid(True)
plt.show()
