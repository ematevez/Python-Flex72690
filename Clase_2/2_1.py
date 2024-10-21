# listas_en_python.py

# Introducción a las Listas en Python

# Las listas son estructuras de datos que permiten almacenar múltiples elementos.
# A diferencia de otros lenguajes, en Python las listas pueden contener distintos tipos de datos.

#?¿Qué incluye este archivo?
#?Introducción a las listas: Explicación básica y definición de listas.
#? Acceso por índice: Ejemplos de cómo acceder a los elementos de una lista.
#? Slicing: Cómo obtener subconjuntos de una lista.
#? Operaciones básicas: Agregar, eliminar y modificar elementos en una lista.
#? Funciones útiles: Uso de append(), pop(), count(), e index().



# Definición de Listas

# Lista de números enteros
# lista = []
# lista_1 = list()
numeros = [1, 2, 3, 4, 5]
# print("Lista de números:", numeros)

#Lista de cadenas de texto
frutas = ['manzana', "banana", "cereza"]
# print("Lista de frutas:", frutas)

# Lista heterogénea (contiene diferentes tipos de datos)
mi_lista = [1, "Hola", 3.14, True]
# print("Lista heterogénea:", mi_lista)

# # Las listas son **mutables**, lo que significa que podemos cambiar sus elementos después de haberlas creado.


# Acceso por Índice

# Para acceder a los elementos de una lista, utilizamos su índice, el cual empieza en 0.
# Ejemplos:

# primer_numero = numeros[0]  # Accediendo al primer número
# print("Primer número en la lista 'numeros':", primer_numero)

# segundo_nombre = frutas[1]  # Accediendo al segundo nombre en la lista 'frutas'
# print("Segunda fruta en la lista 'frutas':", segundo_nombre)

# # Las listas heterogéneas también permiten acceso por índice.
# primer_dato = mi_lista[-1]  # El primer dato en la lista 'mi_lista' es 1
# print("Primer dato en la lista heterogénea 'mi_lista':", primer_dato)


# Slicing (Subconjuntos de Listas)

# Python permite extraer partes de una lista usando "slicing".
# La sintaxis es lista[inicio:fin], donde 'inicio' es el índice desde donde se empieza
# y 'fin' es el índice hasta donde queremos llegar (sin incluir ese valor).

# numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Redefinimos la lista 'numeros' para más ejemplos

# Obteniendo los primeros cinco elementos
# primeros_cinco = numeros[0:5]  # Obtiene los elementos desde el índice 0 hasta el 4
# print("Primeros cinco elementos de 'numeros':", primeros_cinco)

# # Obteniendo elementos desde el índice 5 hasta el final
# desde_cinco = numeros[5:]  # Obtiene los elementos desde el índice 5 hasta el final de la lista
# print("Elementos desde el índice 5 hasta el final de 'numeros':", desde_cinco)

# # Obteniendo un subconjunto de la lista
# sub_lista = numeros[2:7]  # Obtiene los elementos desde el índice 2 hasta el 6
# print("Subconjunto de la lista 'numeros' (índices 2 a 6):", sub_lista)

# # Usando un tercer parámetro en slicing: 'paso'
# pares = numeros[0:10:2]  # Obtiene los elementos desde el índice 0 hasta el 9 con un paso de 2 (pares)
# print("Elementos pares en 'numeros':", pares)


# Operaciones Básicas con Listas

# A continuación se muestran algunas operaciones comunes con listas: agregar, eliminar y modificar.

# Lista inicial
mi_lista = [1, 2, 3, 1, 1,2]
print("\nLista original:", mi_lista)

# 1. Agregar un elemento al final de la lista con 'append'
mi_lista.append(4)  # [1, 2, 3, 4]
print("Después de agregar el 4 al final:", mi_lista)

# 2. Insertar un elemento en una posición específica con 'insert'
mi_lista.insert(1, 1.5)  # Inserta 1.5 en la posición 1: [1, 1.5, 2, 3, 4]
mi_lista.insert(3, "Hola")  # Inserta Hola en la posición 3: [1, 1.5, 2, "Hola",3, 4]
print("Después de insertar 1.5 en la posición 1:", mi_lista)

# 3. Eliminar un elemento específico con 'remove'
mi_lista.remove(1.5)  # Elimina el valor 1.5: [1, 2, 3, 4]
print("Después de eliminar 1.5:", mi_lista)

# 4. Modificar un elemento existente accediendo por su índice
mi_lista[0] = "Me modifique"  # Cambia el primer valor a 5: [5, 2, 3, 4]
print("Después de modificar el primer elemento a 5:", mi_lista)


# Funciones Útiles en Listas

# Python tiene varias funciones integradas que podemos usar para trabajar con listas.

# Contar cuántas veces aparece un elemento en la lista con 'count'
repeticiones = mi_lista.count(2)  # Cuenta cuántas veces aparece el número 2 en la lista
print("\nEl número 2 aparece", repeticiones, "veces en 'mi_lista'")

# Obtener el índice de la primera aparición de un elemento con 'index'
indice_tres = mi_lista.index(3)  # Devuelve el índice donde aparece el número 3
print("El número 3 se encuentra en el índice:", indice_tres)

# Eliminar y devolver el último elemento de la lista con 'pop'
ultimo_elemento = mi_lista.pop()  # Elimina el último elemento y lo devuelve
print("Después de hacer pop, el último elemento era:", ultimo_elemento)
print("Lista después del pop:", mi_lista)

# Finalmente, agregamos nuevamente el elemento 4 para dejar la lista como estaba
mi_lista.append(4)
print("Lista restaurada:", mi_lista)


# Conclusión:
# Las listas en Python son estructuras de datos muy poderosas y flexibles.
# Nos permiten almacenar colecciones de datos, realizar operaciones básicas como agregar,
# eliminar y modificar elementos, y utilizarlas de manera eficiente en nuestros programas.

# # TODO Métodos para Listas:
# # extend(): Añade los elementos de una lista al final de otra lista.
# # reverse(): Invierte el orden de los elementos en la lista.
# # sort(): Ordena los elementos de la lista.
# # Métodos para Strings:
# # upper(): Convierte una cadena a mayúsculas.
# # lower(): Convierte una cadena a minúsculas.
# # replace(): Reemplaza una subcadena por otra.
# # split(): Divide una cadena en una lista.
# # join(): Une los elementos de una lista en una cadena.

# # listas_en_python_y_strings.py

# # Métodos adicionales para Listas

# # # Lista inicial para ejemplos
# # numeros = [1, 2, 3]
# # print("\nLista original de números:", numeros)

# # # 1. extend() - Añade los elementos de una lista al final de otra
# # numeros.extend([4, 5, 6])
# # print("Después de extender con [4, 5, 6]:", numeros)

# # # 2. reverse() - Invierte los elementos de la lista
# # numeros.reverse()
# # print("Lista después de reverse:", numeros)

# # # 3. sort() - Ordena los elementos de la lista
# # numeros.sort()
# # print("Lista ordenada:", numeros)


# # # Métodos adicionales para Strings

# # # String inicial para ejemplos
# # mi_string = "Hola, Mundo"
# # print("\nCadena original:", mi_string)

# # # 1. upper() - Convierte una cadena a mayúsculas
# # mayusculas = mi_string.upper()
# # print("En mayúsculas:", mayusculas)

# # # 2. lower() - Convierte una cadena a minúsculas
# # minusculas = mi_string.lower()
# # print("En minúsculas:", minusculas)

# # # 3. replace() - Reemplaza una subcadena por otra
# # reemplazado = mi_string.replace("Mundo", "Python")
# # print("Después de reemplazar 'Mundo' por 'Python':", reemplazado)

# # # 4. split() - Divide una cadena en una lista
# # dividido = mi_string.split(", ")
# # print("Después de dividir por ', ':", dividido)

# # # 5. join() - Une los elementos de una lista en una cadena
# # unido = " - ".join(dividido)
# # print("Después de unir con ' - ':", unido)


# # # Listas y strings juntos: Un ejemplo combinando ambos tipos de datos

# # # Lista de nombres
# # nombres = ["Ana", "Luis", "Carlos"]

# # # Convertir todos los nombres a mayúsculas usando list comprehension
# # nombres_mayusculas = [nombre.upper() for nombre in nombres]
# # print("\nNombres en mayúsculas:", nombres_mayusculas)

# # # Unir los nombres en una cadena
# # cadena_nombres = ", ".join(nombres_mayusculas)
# print("Nombres unidos en una cadena:", cadena_nombres)
