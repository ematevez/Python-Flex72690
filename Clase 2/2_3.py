# Python - Conjuntos y Diccionarios

"""
Conjuntos en Python:
--------------------
Los conjuntos (sets) son colecciones desordenadas de elementos únicos. No permiten duplicados, 
y aunque son mutables, no tienen un orden fijo, lo que significa que no se pueden acceder a sus elementos mediante índices.
"""

#? Conjuntos (Sets):

#? Los conjuntos son colecciones desordenadas de elementos únicos, por lo que no permiten duplicados. Puedes realizar operaciones como unión, intersección y diferencia para trabajar con conjuntos de datos.
#? Ejemplo: conjunto1 | conjunto2 devuelve la unión de ambos conjuntos.
#? Diccionarios (Dictionaries):

#? Son colecciones de pares clave-valor. Son útiles para búsquedas rápidas mediante claves únicas.
#? Ejemplo: Puedes agregar, modificar o eliminar pares clave-valor, y acceder a un valor a través de su clave, como en mi_diccionario['nombre'].

# Definiendo un conjunto de números
numeros = {1, 2, 3, 4, 5}

# Usando la función set() para crear un conjunto
letras = set(['a', 'b', 'c', 'd'])

# Conjunto vacío
conjunto_vacio = set()

# Los conjuntos no permiten duplicados, esto eliminará el duplicado '2'
numeros_con_duplicados = {1, 2, 2, 3}
print(f"Conjunto sin duplicados: {numeros_con_duplicados}")  # Resultado: {1, 2, 3}

"""
Operaciones con Conjuntos:
--------------------------
Los conjuntos permiten realizar operaciones matemáticas como unión, intersección y diferencia.
"""

# Unión de conjuntos: une los elementos de ambos conjuntos, eliminando duplicados
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1 | conjunto2  # {1, 2, 3, 4, 5}
print(f"Unión: {union}")

# Intersección: devuelve los elementos comunes entre ambos conjuntos
interseccion = conjunto1 & conjunto2  # {3}
print(f"Intersección: {interseccion}")

# Diferencia: devuelve los elementos que están en el primer conjunto pero no en el segundo
diferencia = conjunto1 - conjunto2  # {1, 2}
print(f"Diferencia: {diferencia}")

"""
Métodos en Conjuntos:
---------------------
Los conjuntos también tienen varios métodos útiles para manipular sus elementos.
"""

# Agregar un elemento al conjunto
numeros.add(6)  # numeros ahora es {1, 2, 3, 4, 5, 6}
print(f"Conjunto después de agregar un número: {numeros}")

# Eliminar un elemento usando remove() - genera un error si el elemento no existe
numeros.remove(6)  # numeros ahora es {1, 2, 3, 4, 5}
print(f"Conjunto después de eliminar un número: {numeros}")

# Eliminar un elemento usando discard() - no genera error si el elemento no existe
numeros.discard(6)  # no genera error si '6' no está en el conjunto
print(f"Conjunto después de intentar descartar el número 6: {numeros}")

# Vaciar el conjunto
numeros.clear()  # numeros ahora es un conjunto vacío
print(f"Conjunto después de limpiarlo: {numeros}")

"""
Diccionarios en Python:
-----------------------
Los diccionarios (dictionaries) son colecciones de pares clave-valor, donde cada clave es única y está asociada a un valor.
Son muy útiles cuando se necesitan búsquedas rápidas o cuando se necesita acceder a datos mediante una clave específica.
"""

# Definiendo un diccionario
mi_diccionario = {
    'nombre': 'Alice',
    'edad': 25,
    'ciudad': 'Nueva York'
}
print(f"Diccionario inicial: {mi_diccionario}")

# Acceder a un valor utilizando la clave
print(f"Nombre: {mi_diccionario['nombre']}")  # 'Alice'

# Modificar el valor de una clave existente
mi_diccionario['edad'] = 26  # Cambiamos la edad a 26
print(f"Diccionario después de modificar la edad: {mi_diccionario}")

# Agregar un nuevo par clave-valor
mi_diccionario['profesion'] = 'Ingeniera'
print(f"Diccionario después de agregar una nueva clave-valor: {mi_diccionario}")

# Eliminar un par clave-valor usando pop()
edad_eliminada = mi_diccionario.pop('edad')  # Elimina la clave 'edad'
print(f"Diccionario después de eliminar la edad: {mi_diccionario}")

# Verificar si una clave existe en el diccionario
if 'ciudad' in mi_diccionario:
    print(f"Ciudad: {mi_diccionario['ciudad']}")

# Obtener solo las claves, los valores o ambos
print(f"Claves del diccionario: {mi_diccionario.keys()}")
print(f"Valores del diccionario: {mi_diccionario.values()}")

# Limpiar el diccionario
mi_diccionario.clear()
print(f"Diccionario después de limpiarlo: {mi_diccionario}")
