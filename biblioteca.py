import random

# Función de búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Devuelve la posición donde se encontró
    return -1  # No se encontró

# Función de ordenamiento por inserción
def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

# Configuración inicial del juego
print("¡Bienvenido a La biblioteca desordenada!")
print("Encuentra el libro especial en 3 intentos y ordena los códigos para salvar la biblioteca.")

# Generar una lista de 8 códigos de libros (números aleatorios entre 1 y 10)
codigos = [random.randint(1, 10) for _ in range(8)]
libro_especial = random.choice(codigos)  # Elegir un código como libro especial
intentos = 0
intentos_max = 3  # Límite de 3 intentos

print(f"Códigos de libros en la estantería: {codigos}")
print("Ingresa un código (1-10) para buscar el libro especial.")

# Bucle principal del juego
while intentos < intentos_max:
    try:
        adivinanza = int(input(f"Intento {intentos + 1}/{intentos_max} - Ingresa un código: "))
        if adivinanza < 1 or adivinanza > 10:
            print("Por favor, ingresa un número válido (1-10).")
            continue
        intentos += 1

        # Usar búsqueda lineal para verificar si el código es el libro especial
        posicion = busqueda_lineal(codigos, adivinanza)
        
        if posicion != -1:
            print(f"¡Encontraste el libro especial en la posición {posicion + 1}!")
            print(f"Lo lograste en {intentos} intentos.")
            break
        else:
            print("Ese no es el libro especial. ¡Sigue buscando!")
            if intentos == intentos_max:
                print(f"¡Te quedaste sin intentos! El libro especial tenía el código {libro_especial}.")
                exit()
    except ValueError:
        print("Por favor, ingresa un número válido (1-10).")

# Fase de ordenamiento
print("\nAhora, ordena los códigos para organizar la estantería.")
print("Estantería desordenada:", codigos)
codigos_ordenados = ordenamiento_insercion(codigos.copy())  # Ordenar una copia
print("Estantería ordenada:", codigos_ordenados)

# Verificar si el ordenamiento es correcto
lista_correcta = sorted(codigos)  # Lista ordenada para comparar
if codigos_ordenados == lista_correcta:
    print("¡Estantería ordenada correctamente! La biblioteca está salvada.")
else:
    print("El ordenamiento no fue correcto. La biblioteca sigue en caos.")