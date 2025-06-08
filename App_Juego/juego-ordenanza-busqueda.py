import time  # Se importa el módulo 'time' para usar delays visuales (time.sleep)


# Juego 1: ORDENÁ TÚ MISMO


# Función auxiliar para mostrar la lista con énfasis en los elementos comparados
def mostrar_lista(lista, i=None, j=None):
    visual = ""
    for idx, num in enumerate(lista):
        if idx == i or idx == j:
            visual += f"[{num}] "  # Se destacan los números en comparación
        else:
            visual += f" {num}  "  # Los demás se muestran normalmente
    print(visual)

# Lógica del juego: el usuario ordena una lista paso a paso al estilo Bubble Sort
def ordena_tu_mismo(lista):
    aciertos = 0
    errores = 0
    n = len(lista)
    cambios_realizados = True  # Controla si hubo intercambios para continuar iterando

    print("\n🔄 Comenzamos el juego: ¡Ordena tú mismo!\n")
    
    ronda = 1
    while cambios_realizados:  # Repite mientras haya intercambios
        cambios_realizados = False
        print(f"\n--- Ronda #{ronda} ---\n")
        for j in range(n - 1):  # Recorre la lista hasta el penúltimo elemento
            print(f"Comparando posiciones {j} y {j+1}:")
            mostrar_lista(lista, j, j+1)  # Muestra la comparación
            print(f"\n¿Cuál número debería ir primero?")
            print(f"A: {lista[j]}")
            print(f"B: {lista[j+1]}")

            # Solicita elección del usuario
            eleccion = input("Escribe 'A' o 'B': ").strip().upper()
            while eleccion not in ['A', 'B']:
                eleccion = input("Entrada inválida. Escribe 'A' o 'B': ").strip().upper()

            # Valida si la elección fue correcta según el orden real
            if (eleccion == 'A' and lista[j] <= lista[j+1]) or \
               (eleccion == 'B' and lista[j] > lista[j+1]):
                print("✅ ¡Correcto!")
                aciertos += 1
            else:
                print("❌ Incorrecto.")
                errores += 1

            # Si es necesario, intercambia los elementos
            if lista[j] > lista[j+1]:
                print("🔁 Se intercambian los números.")
                lista[j], lista[j+1] = lista[j+1], lista[j]
                cambios_realizados = True
            else:
                print("✔️ No se necesita intercambio.")
            
            mostrar_lista(lista)  # Muestra el estado de la lista tras comparar/intercambiar
            print("-" * 40)
            time.sleep(0.5)  # Pausa para facilitar la visualización
        ronda += 1

    # Final del juego
    print("\n🎉 ¡Lista ordenada correctamente!")
    print("📋 Resultado final:")
    mostrar_lista(lista)
    print(f"\n✅ Aciertos: {aciertos}")
    print(f"❌ Errores: {errores}")

# Inicializa el juego de ordenamiento pidiendo 5 números al usuario
def iniciar_juego_ordenamiento():
    print("=== Juego educativo: ORDENÁ TÚ MISMO ===")
    print("Ingresa 5 números. Vas a decidir el orden paso a paso.")

    LIMITE = 5
    lista_usuario = []
    
    while len(lista_usuario) < LIMITE:
        try:
            num = int(input(f"Ingrese número #{len(lista_usuario)+1}: "))
            lista_usuario.append(num)
        except ValueError:
            print("❌ Entrada inválida. Solo se permiten números.")

    print("\n🔢 Lista inicial:")
    mostrar_lista(lista_usuario)

    ordena_tu_mismo(lista_usuario)  # Inicia el juego


# Juego 2: BUSCAR EL TESORO


# Función que muestra visualmente el rango donde la computadora busca el tesoro
def visualizar_rango(limite_inferior, limite_superior, suposicion_actual, rango_maximo=100):
    barra_visual = ["." for _ in range(rango_maximo)]  # Todos los puntos (1-100) representados como "."
    for i in range(limite_inferior - 1, limite_superior):
        barra_visual[i] = "█"  # El rango actual de búsqueda se marca con "█"
    barra_visual[suposicion_actual - 1] = "A"  # La suposición actual se marca con "A"
    print(f"Rango [{limite_inferior}, {limite_superior}]: " + "".join(barra_visual))

# Lógica del juego de búsqueda binaria: la computadora adivina
def buscar_tesoro_con_busqueda_binaria():
    limite_inferior = 1
    limite_superior = 100
    numero_de_intentos = 0

    # Introducción del juego
    print("🗺️ Juego: BUSCAR EL TESORO (Búsqueda Binaria)")
    print("Imagina que escondes un tesoro en una posición secreta entre 1 y 100.")
    print("Yo (la computadora) intentaré adivinar dónde está usando el método de 'búsqueda binaria'.")
    print("Cuando te pregunte, responde 'izquierda', 'derecha' o 'encontrado'.")
    input("Presiona Enter cuando estés listo para empezar...")

    while limite_inferior <= limite_superior:  # Mientras el rango siga siendo válido
        suposicion_actual = (limite_inferior + limite_superior) // 2
        numero_de_intentos += 1
        print(f"\nIntento #{numero_de_intentos}: ¿Está el tesoro en la posición {suposicion_actual}?")
        visualizar_rango(limite_inferior, limite_superior, suposicion_actual)

        respuesta_usuario = input("Responde (izquierda/derecha/encontrado): ").lower()

        # Ajusta el rango según la respuesta del jugador
        if respuesta_usuario == "encontrado":
            print(f"🎉 ¡Excelente! ¡Encontré el tesoro en la posición {suposicion_actual} en {numero_de_intentos} intentos!")
            break  # Fin del juego
        elif respuesta_usuario == "izquierda":
            limite_superior = suposicion_actual - 1
        elif respuesta_usuario == "derecha":
            limite_inferior = suposicion_actual + 1
        else:
            print("❌ Respuesta no válida. Usa 'izquierda', 'derecha' o 'encontrado'.")


# Menú principal


# Muestra el menú de juegos y permite al usuario elegir
def menu_principal():
    while True:
        print("\n🎓 MENÚ DE JUEGOS EDUCATIVOS")
        print("1. Ordena tú mismo (Bubble Sort)")
        print("2. Buscar el tesoro (Búsqueda Binaria)")
        print("3. Salir")
        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            iniciar_juego_ordenamiento()
        elif opcion == "2":
            buscar_tesoro_con_busqueda_binaria()
        elif opcion == "3":
            print("👋 ¡Hasta la próxima!")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()
