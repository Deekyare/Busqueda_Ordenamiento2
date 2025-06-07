import random

# Función de búsqueda binaria
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio  # Devuelve la posición donde se encontró
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  # No se encontró

# Función de ordenamiento por selección interactivo
def ordenamiento_seleccion_interactivo(lista, frutas):
    for paso in range(len(lista)):
        print(f"\nPaso {paso + 1}: Encuentra el menor valor en la lista (índices {paso} a {len(lista)-1}):")
        for posicion in range(paso, len(lista)):
            print(f"Índice {posicion}: {frutas[posicion]} ({lista[posicion]})")
        
        # Encontrar el índice del menor valor automáticamente para comparar
        indice_menor = paso
        for j in range(paso + 1, len(lista)):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        
        # Pedir al usuario que elija el índice del menor valor
        try:
            indice_elegido = int(input(f"Ingresa el índice del menor valor: "))
            if indice_elegido < paso or indice_elegido >= len(lista):
                print(f"Índice inválido. Usando el índice correcto ({indice_menor}).")
            elif indice_elegido != indice_menor:
                print(f"¡Incorrecto! El menor valor es {lista[indice_menor]} en el índice {indice_menor}.")
            else:
                print("¡Correcto! Buen ojo.")
            
            # Realizar el intercambio
            lista[paso], lista[indice_menor] = lista[indice_menor], lista[paso]
        except ValueError:
            print(f"Entrada inválida. Usando el índice correcto ({indice_menor}).")
            lista[paso], lista[indice_menor] = lista[indice_menor], lista[paso]
    
    return lista

# Lista de 10 frutas
frutas = ["Manzana", "Banana", "Naranja", "Mango", "Kiwi", "Piña", "Fresa", "Uva", "Melón", "Pera"]
# Configuración inicial del juego
print("¡Bienvenido al Mercado de Frutas Mágicas!")
print("Ordena el puesto interactivamente y encuentra la fruta especial en 3 intentos.")

# Generar una lista de 10 valores mágicos únicos (números entre 1 y 10)
valores = random.sample(range(1, 11), 10)  # Números únicos de 1 a 10

# Fase de ordenamiento interactivo
print("\nPrimero, ordena las frutas por su valor mágico seleccionando el menor valor en cada paso.")
print("Puesto desordenado:", end=" ")
for posicion, valor in enumerate(valores):
    print(f"{frutas[posicion]}: {valor}", end=" ")
print()
valores_ordenados = ordenamiento_seleccion_interactivo(valores.copy(), frutas)
print("Puesto ordenado:", end=" ")
for posicion, valor in enumerate(valores_ordenados):
    print(f"{frutas[posicion]}: {valor}", end=" ")
print()

# Verificar si el ordenamiento es correcto
lista_correcta = sorted(valores)
if valores_ordenados != lista_correcta:
    print("\nEl ordenamiento no fue correcto. El mercado sigue en caos.")
    exit()

print("\n¡Puesto ordenado correctamente! Ahora busca la fruta especial.")

# Seleccionar la fruta especial
valor_fruta_especial = random.choice(valores_ordenados)  # Valor de la fruta especial
nombre_fruta_especial = frutas[valores.index(valor_fruta_especial)]  # Nombre de la fruta
intentos = 0
intentos_maximos = 3  # Límite de 3 intentos

# Mostrar la lista ordenada para la búsqueda
print("\nFrutas en el puesto ordenado (valor mágico):")
for posicion, valor in enumerate(valores_ordenados):
    print(f"{frutas[posicion]}: {valor}")
print(f"Busca la fruta especial ({nombre_fruta_especial}), con un valor entre 1 y 10.")

# Bucle principal del juego (búsqueda)
while intentos < intentos_maximos:
    try:
        adivinanza = int(input(f"Intento {intentos + 1}/{intentos_maximos} - Ingresa el valor mágico de la fruta: "))
        if adivinanza < 1 or adivinanza > 10:
            print("Por favor, ingresa un número válido (1-10).")
            continue
        intentos += 1

        # Usar búsqueda binaria para verificar si el valor es la fruta especial
        posicion = busqueda_binaria(valores_ordenados, adivinanza)
        
        if posicion != -1:
            print(f"¡Encontraste la {nombre_fruta_especial} en la posición {posicion + 1}!")
            print(f"Lo lograste en {intentos} intentos.")
            print("¡El mercado está en armonía!")
            break
        else:
            print("Ese valor no es el de la fruta especial. ¡Sigue buscando!")
            if intentos == intentos_maximos:
                print(f"¡Te quedaste sin intentos! La fruta especial era {nombre_fruta_especial} con valor {valor_fruta_especial}.")
                print("El mercado sigue en caos.")
                exit()
    except ValueError:
        print("Por favor, ingresa un número válido (1-10).")