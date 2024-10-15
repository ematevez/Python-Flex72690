# -*- coding: utf-8 -*-
"""
Título: Introducción a las Tuplas en Python
Descripción: Este archivo muestra ejemplos de cómo utilizar tuplas en Python,
explicando paso a paso sus características y uso práctico.

"""

#? Definición de Tuplas: Se definen tuplas con diferentes tipos de datos, mostrando cómo se pueden almacenar elementos heterogéneos.
#? Acceso por Índice: Se explica cómo acceder a los elementos de una tupla usando el índice, igual que en las listas.
#? Slicing: Se muestra cómo extraer subconjuntos de una tupla utilizando slicing.
#? Comparación entre Listas y Tuplas: Se comparan las listas y las tuplas, demostrando la mutabilidad de las listas y la inmutabilidad de las tuplas.
#? Mutabilidad e Inmutabilidad: Se ilustra con ejemplos cómo las listas pueden ser modificadas, pero las tuplas no.
#? Cuándo usar Tuplas vs Listas: Explicación de cuándo es más adecuado usar una lista o una tupla, dependiendo de si los datos deben cambiar.
#? Ventajas de las Tuplas: Explicación de algunas ventajas de las tuplas, como el acceso rápido y su uso como claves en diccionarios.

#TODO Ventajas y ejemplos adicionales de las tuplas:
# Las tuplas son más rápidas de iterar que las listas.
# Las tuplas pueden ser usadas como claves en diccionarios, ya que son inmutables.

# 1. Definiendo una Tupla
print("### Definiendo una Tupla ###")

# Tupla de números enteros
numeros_1 = ()
numeros_2 = tuple()
numeros = (10, 20, 30, 40, 50)
print("Tupla de números:", numeros)

# Tupla de cadenas de texto
nombres = ("Alice", "Bob", "Charlie")
print("Tupla de nombres:", nombres)

# Tupla heterogénea (diferentes tipos de datos)
datos = (25, "Python", 3.14, False)
print("Tupla heterogénea:", datos)

print("\n")

# 2. Accediendo a los Elementos de una Tupla
print("### Acceso por Índice ###")

# Se puede acceder a los elementos utilizando su índice, al igual que en las listas.
primer_numero = numeros[0]  # Índice 0 es el primer elemento
print("Primer número de la tupla 'numeros':", primer_numero)

segundo_nombre = nombres[1]  # Índice 1 es el segundo elemento
print("Segundo nombre de la tupla 'nombres':", segundo_nombre)

# Acceso en tuplas heterogéneas
primer_dato = datos[0]
print("Primer dato de la tupla 'datos':", primer_dato)

segundo_dato = datos[1]
print("Segundo dato de la tupla 'datos':", segundo_dato)

print("\n")

# 3. Slicing (Subconjuntos de una Tupla)
print("### Slicing en Tuplas ###")

# Python permite extraer subconjuntos de una tupla utilizando la técnica de slicing.
# La sintaxis es: tupla[inicio:fin] (el índice de fin es exclusivo)

# Slicing: obteniendo los primeros cinco elementos
primeros_cinco = numeros[0:5]
print("Primeros cinco números:", primeros_cinco)

# Slicing: obteniendo elementos desde el índice 5 hasta el final
desde_cinco = numeros[2:]
print("Elementos desde el índice 2 hasta el final:", desde_cinco)

# Slicing: obteniendo un subconjunto de elementos (índices 2 al 6)
sub_tupla = numeros[2:5]
print("Subtupla de 'numeros' desde el índice 2 al 4:", sub_tupla)

print("\n")

# 4. Comparación entre Listas y Tuplas
print("### Comparación entre Listas y Tuplas ###")

# Similitudes entre Listas y Tuplas:
# Ambas son colecciones ordenadas y permiten el acceso por índice.
mi_lista = [1, 2, 3]  # Lista mutable
mi_tupla = (1, 2, 3)  # Tupla inmutable

print("Lista antes de agregar un elemento:", mi_lista)
mi_lista.append(4)  # Puedo modificar una lista
print("Lista después de agregar un elemento:", mi_lista)

print("Tupla original:", mi_tupla)
# mi_tupla.append(4)  # Esto daría un error, las tuplas no se pueden modificar

print("\n")

# 5. Mutabilidad y Inmutabilidad
print("### Mutabilidad e Inmutabilidad ###")
# Las listas son mutables, lo que significa que se pueden modificar después de creadas.
# Las tuplas son inmutables, lo que significa que NO se pueden modificar después de creadas.


# En cambio, en una lista, sí puedo modificar sus valores
mi_lista[0] = 5
print("Lista después de modificar el primer elemento:", mi_lista)

print("\n")

# 6. Cuándo usar Tuplas vs Listas
print("### Cuándo usar Tuplas vs Listas ###")
# Las tuplas son útiles cuando quieres asegurarte de que los datos no cambien.
# Ejemplo: Coordenadas geográficas (no deberían cambiar)
coordenadas = (40.7128, -74.0060)  # Latitud y longitud de Nueva York
print("Coordenadas geográficas:", coordenadas)

# Las listas son más útiles cuando los datos pueden cambiar durante la ejecución del programa.
# Ejemplo: Una lista de tareas pendientes
tareas = ["Comprar leche", "Llamar al dentista", "Hacer ejercicio"]
print("Lista de tareas:", tareas)

# Puedo agregar tareas a una lista
tareas.append("Estudiar Python")
print("Lista de tareas actualizada:", tareas)

print("\n")

# 7. Ventajas de las Tuplas
print("### Ventajas de las Tuplas ###")
# Las tuplas, al ser inmutables, pueden ser más rápidas que las listas para ciertas operaciones,
# y también pueden usarse como claves en un diccionario (las listas no).
diccionario = {coordenadas: "Nueva York"}
print("Diccionario con tupla como clave:", diccionario)




#?====================================================================
# # tuplas_metodos_y_ejemplos.py

# # Métodos útiles para Tuplas

# # Tupla para ejemplos
# tupla_numeros = (1, 2, 3, 4, 3, 2, 1)
# print("\nTupla de números:", tupla_numeros)

# # 1. count() - Cuenta cuántas veces aparece un valor en la tupla
# conteo_dos = tupla_numeros.count(2)
# print("El número 2 aparece", conteo_dos, "veces en la tupla.")

# # 2. index() - Devuelve el índice de la primera aparición de un valor
# indice_tres = tupla_numeros.index(3)
# print("El número 3 aparece por primera vez en el índice:", indice_tres)


# # Ventajas de las Tuplas

# # 1. Las tuplas son más rápidas que las listas para ciertas operaciones
# import time

# # Comparación de tiempo entre listas y tuplas
# lista_grande = list(range(1000000))
# tupla_grande = tuple(range(1000000))

# # Medir el tiempo de acceso en una lista
# inicio_lista = time.time()
# lista_grande[500000]
# fin_lista = time.time()
# print("\nTiempo de acceso en una lista:", fin_lista - inicio_lista)

# # Medir el tiempo de acceso en una tupla
# inicio_tupla = time.time()
# tupla_grande[500000]
# fin_tupla = time.time()
# print("Tiempo de acceso en una tupla:", fin_tupla - inicio_tupla)

# # 2. Las tuplas pueden usarse como claves en diccionarios
# coordenadas = (40.7128, -74.0060)  # Ejemplo de coordenadas geográficas
# diccionario = {coordenadas: "Nueva York"}
# print("\nDiccionario con tupla como clave:", diccionario)


# # Tuplas con desempaquetado
# print("\n### Desempaquetado de Tuplas ###")
# # Las tuplas permiten el desempaquetado, lo que significa que podemos asignar
# # sus elementos a varias variables de una sola vez.

# mi_tupla = (10, 20, 30)
# a, b, c = mi_tupla
# print("Valores desempaquetados de la tupla:", a, b, c)

# # Desempaquetado parcial
# mi_tupla2 = (100, 200, 300, 400)
# x, *resto = mi_tupla2
# print("Primer valor:", x)
# print("Resto de la tupla:", resto)
