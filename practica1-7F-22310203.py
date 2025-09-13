import numpy as np

# Función de activación: Escalón
def step_function(x):
    return 1 if x >= 0 else 0

# Datos de entrada:
# [Está lloviendo, Pronóstico indica lluvia]
entradas = np.array([
    [0, 0],  # No llueve y pronóstico no
    [0, 1],  # No llueve pero pronóstico sí
    [1, 0],  # Llueve pero pronóstico no
    [1, 1]   # Llueve y pronóstico sí
])

# Salidas esperadas (1 = sí lleva paraguas, 0 = no)
salidas = np.array([0, 0, 0, 1])

# Inicialización
pesos = np.random.rand(2)
bias = np.random.rand(1)
tasa_aprendizaje = 0.1
epocas = 20

# Entrenamiento
for epoca in range(epocas):
    print(f"Época {epoca+1}")
    for entrada, salida_esperada in zip(entradas, salidas):
        suma = np.dot(entrada, pesos) + bias
        salida_obtenida = step_function(suma)
        error = salida_esperada - salida_obtenida

        # Actualización
        pesos += tasa_aprendizaje * error * entrada
        bias += tasa_aprendizaje * error

        print(f" Entrada: {entrada}, Esperada: {salida_esperada}, "
              f"Obtenida: {salida_obtenida}, Pesos: {pesos}, Bias: {bias}")
    print()

# Prueba final
print("Pruebas finales del perceptrón (llevar paraguas o no):")
for entrada in entradas:
    salida = step_function(np.dot(entrada, pesos) + bias)
    print(f"Lluvia={entrada[0]}, Pronóstico={entrada[1]} => Lleva paraguas: {salida}")
