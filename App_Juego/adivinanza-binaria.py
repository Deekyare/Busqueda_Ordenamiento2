def visualizar_rango(limite_inferior, limite_superior, suposicion_actual, rango_maximo=100):
    # Crea una lista de puntos "." para representar todas las posiciones posibles (del 1 al 100).
    barra_visual = ["." for _ in range(rango_maximo)]
    
    # Marca el rango de búsqueda actual [limite_inferior, limite_superior] con "█".
    # Restamos 1 a los límites para ajustarlos a los índices de la lista (que van de 0 a 99).
    for i in range(limite_inferior - 1, limite_superior):
        barra_visual[i] = "█"
    
    # Marca la suposición actual con "A". También restamos 1 para el índice.
    barra_visual[suposicion_actual - 1] = "A"
    
    # Imprime el rango y la barra visual como un solo string.
    print(f"Rango [{limite_inferior}, {limite_superior}]: " + "".join(barra_visual))

def buscar_tesoro_con_busqueda_binaria():
    # Inicializa el rango de búsqueda: el tesoro puede estar entre 1 y 100.
    limite_inferior = 1
    limite_superior = 100
    # Contador para saber cuántos intentos llevamos.
    numero_de_intentos = 0

    # Instrucciones claras para el usuario del juego.
    print("Imagina que escondes un tesoro en una posición secreta entre 1 y 100.")
    print("Yo (la computadora) intentaré adivinar dónde está usando el método de 'búsqueda binaria'.")
    print("Cuando te pregunte, responde 'izquierda' si el tesoro está a la izquierda de mi suposición,")
    print("responde 'derecha' si está a la derecha, o 'encontrado' si he acertado.")
    # Espera a que el usuario lea las instrucciones y esté listo para jugar.
    input("Presiona Enter cuando estés listo para empezar...")

    # El corazón de la búsqueda binaria: seguimos buscando mientras el rango sea válido.
    while limite_inferior <= limite_superior:
        # Calcula la suposición actual como el punto medio del rango de búsqueda.
        suposicion_actual = (limite_inferior + limite_superior) // 2
        # Aumenta el contador de intentos.
        numero_de_intentos += 1
        # Muestra el intento actual y la suposición.
        print(f"\nIntento #{numero_de_intentos}: ¿Está el tesoro en la posición {suposicion_actual}?")
        # Muestra visualmente el rango de búsqueda y la suposición actual.
        visualizar_rango(limite_inferior, limite_superior, suposicion_actual)
        # Pide la respuesta del usuario. Convertimos a minúsculas para que no importe cómo escriba.
        respuesta_usuario = input("Responde (izquierda/derecha/encontrado): ").lower()

        # Si la suposición es correcta:
        if respuesta_usuario == "encontrado":
            print(f"¡Excelente! ¡Encontré el tesoro en la posición {suposicion_actual} en {numero_de_intentos} intentos!")
            break # Terminamos el juego.
        # Si el tesoro está a la izquierda de la suposición:
        elif respuesta_usuario == "izquierda":
            # Reducimos el límite superior del rango de búsqueda.
            limite_superior = suposicion_actual - 1
        # Si el tesoro está a la derecha de la suposición:
        elif respuesta_usuario == "derecha":
            # Aumentamos el límite inferior del rango de búsqueda.
            limite_inferior = suposicion_actual + 1
        # Si el usuario da una respuesta que no entendemos:
        else:
            print("¡Ups! Respuesta no válida. Por favor, usa 'izquierda', 'derecha' o 'encontrado'.")

# Esto asegura que el juego solo comience cuando ejecutes este archivo directamente.
if __name__ == "__main__":
    buscar_tesoro_con_busqueda_binaria()