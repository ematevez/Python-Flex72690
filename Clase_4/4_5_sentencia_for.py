"""
Descripción del Archivo:
Introducción y Sintaxis: Explicación básica de la sentencia for.
Ejemplos Básicos:
Iteración en listas, cadenas y rangos.
Ejemplos Prácticos:
Modificar elementos en una lista.
Uso de enumerate.
Ejemplos Avanzados:
Iterar sobre diccionarios y conjuntos.
Aplicar condiciones dentro del for.
Uso de comprensión de listas para crear nuevas listas.

"""

# -----------------------------------------------------
# Introducción a la Sentencia For en Python
# -----------------------------------------------------
# La sentencia `for` en Python se utiliza para iterar sobre los elementos
# de un objeto iterable, como listas, tuplas, diccionarios, conjuntos y cadenas.
# Es una herramienta poderosa que permite realizar operaciones repetitivas
# en cada elemento de una colección sin gestionar manualmente un contador o índice.

# -----------------------------------------------------
# Sintaxis de la Sentencia For
# -----------------------------------------------------
# La estructura básica de un bucle `for` es la siguiente:
#
# for elemento in iterable:
#     # Bloque de código a ejecutar por cada elemento
#
# - `elemento`: Variable que toma el valor del siguiente elemento
#    del iterable en cada iteración.
# - `iterable`: Colección de elementos que se está iterando, como una lista o tupla.

# -----------------------------------------------------
# Ejemplos de Implementación de la Sentencia For
# -----------------------------------------------------

# # 1. Iterar sobre una Lista
# frutas = ["manzana", "plátano", "cereza"]
# print("Ejemplo 1: Iterar sobre una lista")
# for fruta in frutas:
#     print(fruta)

# # 2. Iterar sobre una Cadena
# print("\nEjemplo 2: Iterar sobre una cadena")
# for letra in "Python casa":
#     print(letra)

# # 3. Iterar sobre un Rango de Números
# print("\nEjemplo 3: Iterar sobre un rango de números")
# for i in range(1,10):
#     print(i)

# -----------------------------------------------------
# Ejemplos Prácticos de Sentencia For
# -----------------------------------------------------

# # 4. Iterar sobre Listas y Modificar Elementos
# numeros = [1, 2, 3, 4, 5]
# print("\nEjemplo 4: Iterar sobre lista y modificar elementos")
# for i in range(len(numeros)):
#     numeros[i] *= 2
# print("Lista modificada:", numeros)

# # 5. Uso de la Función enumerate
# print("\nEjemplo 5: Uso de enumerate para obtener índice y valor")
# frutas = ["manzana", "plátano", "cereza"]
# for indice, fruta in enumerate(frutas):
#     print(f"Índice: {indice}, Fruta: {fruta}")

# # 6. Modificar Elementos con enumerate
# print("\nEjemplo 6: Modificar elementos con enumerate")
# for indice, fruta in enumerate(frutas):
#     frutas[indice] = fruta.upper()
# print("Lista en mayúsculas:", frutas)

# # -----------------------------------------------------
# # Ejemplos Avanzados
# # -----------------------------------------------------

# 7. Iterar sobre un Diccionario
print("\nEjemplo 7: Iterar sobre un diccionario")
calificaciones = {"Matemáticas": 90, "Ciencia": 85, "Historia": 88}
for materia, calificacion in calificaciones.items():
    print(f"{materia}: {calificacion}")

# 8. Usar for con un Conjunto
print("\nEjemplo 8: Iterar sobre un conjunto")
conjunto_numeros = {1, 2, 3, 4, 5}
for numero in conjunto_numeros:
    print(numero)

# 9. Uso de For con Condiciones
print("\nEjemplo 9: Uso de for con condiciones")
numeros = [1, 2, 3, 4, 5, 6]
for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")

# 10. Uso de For para Crear una Nueva Lista
print("\nEjemplo 10: Uso de for para crear una nueva lista")
nombres = ["Ana", "Juan", "Luis", "María"]
nombres_mayus = [nombre.upper() for nombre in nombres]
print("Nombres en mayúsculas:", nombres_mayus)

# # -----------------------------------------------------
# # Conclusión
# # -----------------------------------------------------
# # La sentencia `for` en Python es una herramienta versátil y poderosa para iterar sobre elementos
# # de objetos iterables. Al comprender su sintaxis y diversas aplicaciones, como la iteración sobre
# # listas, cadenas, diccionarios y rangos, así como el uso de la función `enumerate` y comprensión
# # de listas, se pueden realizar operaciones complejas de manera eficiente. Esta capacidad de iteración
# # y modificación de elementos es fundamental para la programación efectiva en Python.
