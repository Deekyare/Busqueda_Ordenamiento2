def visualize_range(low, high, guess, max_range=100):
    # Crea una lista de puntos "." para representar todas las posiciones (1 a 100).
    bar = ["." for _ in range(max_range)]
    
    # Marca el rango de búsqueda actual [low, high] con "█".
    # Ajusta low-1 y high para los índices de la lista (0 a 99).
    for i in range(low - 1, high):
        bar[i] = "█"
    
    # Marca la suposición actual con "G". Usa guess-1 porque los índices empiezan en 0.
    bar[guess - 1] = "G"
    
    # Imprime el rango y la barra visual como un string.
    print(f"Rango [{low}, {high}]: " + "".join(bar))

def binary_search_treasure():
    # Inicializa el rango de búsqueda: 1 a 100.
    low = 1
    high = 100
    # Contador de intentos.
    attempts = 0

    # Instrucciones para el usuario.
    print("Imagina que escondes un tesoro en una posición entre 1 y 100.")
    print("Yo intentaré encontrarlo usando búsqueda binaria.")
    print("Dime 'izquierda' si está a la izquierda, 'derecha' si está a la derecha, o 'encontrado' cuando acierte.")
    # Espera a que el usuario esté listo.
    input("Presiona Enter cuando estés listo...")

    # Bucle de búsqueda binaria: continúa mientras el rango sea válido.
    while low <= high:
        # Calcula la suposición como el punto medio del rango.
        guess = (low + high) // 2
        # Incrementa el contador de intentos.
        attempts += 1
        # Muestra el intento actual.
        print(f"\nIntento #{attempts}: ¿Está el tesoro en la posición {guess}?")
        # Muestra el rango visualmente.
        visualize_range(low, high, guess)
        # Pide la respuesta del usuario.
        response = input("Responde (izquierda/derecha/encontrado): ").lower()

        # Si la suposición es correcta:
        if response == "encontrado":
            print(f"¡Encontré el tesoro en la posición {guess} en {attempts} intentos!")
            break
        # Si el tesoro está a la izquierda, ajusta el límite superior.
        elif response == "izquierda":
            high = guess - 1
        # Si el tesoro está a la derecha, ajusta el límite inferior.
        elif response == "derecha":
            low = guess + 1
        # Maneja respuestas no válidas.
        else:
            print("Respuesta no válida. Usa 'izquierda', 'derecha' o 'encontrado'.")

# Inicia el juego si el archivo se ejecuta directamente.
if __name__ == "__main__":
    binary_search_treasure()