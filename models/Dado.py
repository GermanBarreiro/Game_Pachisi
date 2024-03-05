import random

def tirar_dado():
    return random.randint(1, 6)

resultado = tirar_dado()
print(f'El resultado de la tirada del dado es: {resultado}')
