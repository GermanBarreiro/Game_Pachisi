import random


def tirar_dado():
    respuesta = input("¿Quieres lanzar el dado? (s/n): ")
    if respuesta.lower() == 's':
        return random.randint(1, 6)
    elif respuesta.lower() == 'n':
        print("Si aprietas 'n' no vas a avanzar en el juego.")
        return tirar_dado()
    else:
        print("Respuesta no reconocida. Por favor, intenta de nuevo.")
        return tirar_dado()


resultado = tirar_dado()
print(f'El resultado de la tirada del dado es: {resultado}')
