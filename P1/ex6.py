
import random

def dado():
    return random.randint(1, 6)

contadores = [0, 0, 0, 0, 0, 0]

for _ in range(100):
    resultado = dado()
    contadores[resultado - 1] += 1

for i in range(6):
    print(f"O valor {i+1} foi obtido {contadores[i]} vezes.")
