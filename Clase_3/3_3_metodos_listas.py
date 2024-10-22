# Métodos de Listas en Python
# ---------------------------
# Este archivo contiene ejemplos de los métodos más comunes para manipular listas en Python.
# Cada método tiene una explicación y un ejemplo para facilitar su comprensión.

# 1. Método clear()
# El método clear() elimina todos los elementos de una lista, dejándola vacía.

letras = ['a', 'b', 'c', 'd', 'e']
print("Lista original:", letras)

# Uso de clear()
letras.clear()
print("Después de usar clear():", letras)  # Salida: []

# 2. Método extend()
# El método extend() añade todos los elementos de un iterable (lista, tupla, etc.) al final de la lista actual.

numeros = [1, 2, 3]
print("\nLista original:", numeros)

# Uso de extend()
numeros.extend([4, 5, 6])
print("Después de usar extend():", numeros)  # Salida: [1, 2, 3, 4, 5, 6]

# 3. Método insert()
# El método insert() inserta un elemento en una posición específica de la lista.

numeros = [1, 2, 3, 4]
print("\nLista original:", numeros)

# Insertar 'a' en la posición 2
numeros.insert(2, 'a')
print("Después de usar insert():", numeros)  # Salida: [1, 2, 'a', 3, 4]

# 4. Método reverse()
# El método reverse() invierte el orden de los elementos en la lista.

numeros = [1, 2, 3, 4, 5]
print("\nLista original:", numeros)

# Uso de reverse()
numeros.reverse()
print("Después de usar reverse():", numeros)  # Salida: [5, 4, 3, 2, 1]

# 5. Método sort()
# El método sort() ordena los elementos de la lista en orden ascendente por defecto.
# También se puede usar el argumento reverse=True para ordenar en orden descendente.

numeros = [5, 2, 9, 1, 5, 6]
print("\nLista original:", numeros)

# Ordenar de forma ascendente
numeros.sort()
print("Después de usar sort() en orden ascendente:", numeros)  # Salida: [1, 2, 5, 5, 6, 9]

# Ordenar de forma descendente
numeros.sort(reverse=True)
print("Después de usar sort() con reverse=True:", numeros)  # Salida: [9, 6, 5, 5, 2, 1]

# 6. Tema adicional: Método pop()
# El método pop() elimina y devuelve el último elemento de la lista. También puede aceptar un índice opcional para eliminar un elemento específico.

frutas = ['manzana', 'banana', 'cereza']
print("\nLista original:", frutas)

# Eliminar el último elemento
ultima_fruta = frutas.pop()
print("Después de usar pop():", frutas)  # Salida: ['manzana', 'banana']
print("Fruta eliminada:", ultima_fruta)  # Salida: cereza

# Eliminar el elemento en la posición 0
primera_fruta = frutas.pop(0)
print("Después de usar pop(0):", frutas)  # Salida: ['banana']
print("Fruta eliminada en la posición 0:", primera_fruta)  # Salida: manzana

# 7. Tema adicional: Método len()
# El método len() devuelve el número de elementos en la lista.

frutas = ['manzana', 'banana', 'cereza']
print("\nLista original:", frutas)

# Obtener la longitud de la lista
longitud = len(frutas)
print("Número de elementos en la lista:", longitud)  # Salida: 3

# Fin del archivo.
# ----------------
# Este archivo cubre los métodos básicos y algunos adicionales para trabajar con listas en Python.
# Juega con estos métodos y trata de entender cómo se comportan cuando los aplicas a diferentes listas.
