# 3.1 Introducción a las Colecciones en Python
#!========================================================================
# # Listas
# # Las listas son colecciones ordenadas y mutables de elementos.

print("\n--- LISTAS ---")

# # Crear una lista
mi_lista = [10, 20, 30, 40]
print(f"Lista original: {mi_lista}")

# append(x): Añade un ítem al final de la lista.
mi_lista.append(50)
print(f"Después de append(50): {mi_lista}")

# extend(iterable): Extiende la lista con los ítems de un iterable.
mi_lista.extend([60, 70])
print(f"Después de extend([60, 70]): {mi_lista}")

# insert(i, x): Inserta un ítem en la posición dada.
mi_lista.insert(100, 25)  # Inserta 25 en la posición 2
print(f"Después de insert(5, 25): {mi_lista}")

# remove(x): Elimina el primer ítem cuyo valor sea x.
mi_lista.remove(25)
print(f"Después de remove(25): {mi_lista}")

# pop([i]): Elimina el ítem en la posición dada de la lista y lo devuelve.
eliminado = mi_lista.pop(2)  # Elimina el ítem en la posición 2
print(f"Elemento eliminado con pop(2): {eliminado}, Lista actual: {mi_lista}")

# # pop([i]): Elimina el ítem en la posición dada de la lista y si no esta dentro del rango da erro.
# eliminado = mi_lista.pop(150)  # Elimina el ítem en la posición 2
# print(f"Elemento eliminado con pop(150): {eliminado}, Lista actual: {mi_lista}")

# clear(): Elimina todos los elementos de la lista.
mi_lista.clear()
print(f"Después de clear(): {mi_lista}")

# Crear una nueva lista para siguientes ejemplos
mi_lista = [1, 2, 2, 3, 4, 5, 6]

# index(x[, start[, end]]): Devuelve el índice del primer ítem cuyo valor sea x.
indice = mi_lista.index(2)
print(f"Índice de 2 en la lista: {indice}")

# count(x): Devuelve el número de veces que x aparece en la lista.
conteo = mi_lista.count(2)
print(f"El número 2 aparece {conteo} veces en la lista.")

# sort(key=None, reverse=False): Ordena la lista.
mi_lista.sort()
print(f"Lista ordenada: {mi_lista}")

# reverse(): Invierte los elementos de la lista.
mi_lista.reverse()
print(f"Lista invertida: {mi_lista}")

# copy(): Devuelve una copia superficial de la lista.
mi_lista_copia = mi_lista.copy()
print(f"Copia de la lista: {mi_lista_copia}")

#!========================================================================
# Conjuntos
# Los conjuntos son colecciones no ordenadas y no permiten duplicados.

print("\n--- CONJUNTOS ---")

# Crear un conjunto
mi_conjunto = {1, 2, 3}
print(f"Conjunto original: {mi_conjunto}")

# add(x): Añade un ítem al conjunto.
mi_conjunto.add(4)
print(f"Después de add(4): {mi_conjunto}")

# remove(x): Elimina un ítem del conjunto. Genera error si no existe.
mi_conjunto.remove(4)
print(f"Después de remove(4): {mi_conjunto}")

# discard(x): Elimina un ítem del conjunto si existe.
mi_conjunto.discard(5)  # No generará error aunque 5 no esté en el conjunto
print(f"Después de discard(5): {mi_conjunto}")

# pop(): Elimina y devuelve un ítem arbitrario del conjunto.
eliminado = mi_conjunto.pop()
print(f"Elemento eliminado con pop(): {eliminado}, Conjunto actual: {mi_conjunto}")

# clear(): Elimina todos los elementos del conjunto.
mi_conjunto.clear()
print(f"Después de clear(): {mi_conjunto}")

# Crear conjuntos para siguientes ejemplos
A = {1, 2, 3}
B = {3, 4, 5}

# union(*others): Devuelve la unión de conjuntos.
union = A.union(B)
print(f"Unión de A y B: {union}")

# intersection(*others): Devuelve la intersección de conjuntos.
interseccion = A.intersection(B)
print(f"Intersección de A y B: {interseccion}")

# difference(*others): Devuelve la diferencia de conjuntos.
diferencia = A.difference(B)
print(f"Diferencia de A - B: {diferencia}")

# symmetric_difference(other): Devuelve la diferencia simétrica.
diferencia_simetrica = A.symmetric_difference(B)
print(f"Diferencia simétrica de A y B: {diferencia_simetrica}")

# issubset(other): Verifica si A es subconjunto de B.
es_subconjunto = A.issubset(B)
print(f"A es subconjunto de B: {es_subconjunto}")

# issuperset(other): Verifica si A es superconjunto de B.
es_superconjunto = A.issuperset(B)
print(f"A es superconjunto de B: {es_superconjunto}")

# copy(): Devuelve una copia superficial del conjunto.
copia_conjunto = A.copy()
print(f"Copia del conjunto A: {copia_conjunto}")

#!========================================================================
# Diccionarios
# Los diccionarios son colecciones de pares clave-valor.

print("\n--- DICCIONARIOS ---")

# Crear un diccionario
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(f"Diccionario original: {mi_diccionario}")

# get(key[, default]): Devuelve el valor de la clave.
nombre = mi_diccionario.get("nombre")
print(f"Nombre: {nombre}")

# keys(): Devuelve una vista de las claves del diccionario.
claves = mi_diccionario.keys()
print(f"Claves del diccionario: {claves}")

# values(): Devuelve una vista de los valores del diccionario.
valores = mi_diccionario.values()
print(f"Valores del diccionario: {valores}")

# items(): Devuelve una vista de los pares clave-valor.
items = mi_diccionario.items()
print(f"Pares clave-valor: {items}")

# pop(key[, default]): Elimina una clave y devuelve su valor.
edad = mi_diccionario.pop("edad")
print(f"Edad eliminada: {edad}, Diccionario actual: {mi_diccionario}")

# popitem(): Elimina y devuelve un par clave-valor aleatorio.
par_eliminado = mi_diccionario.popitem()
print(f"Par eliminado: {par_eliminado}, Diccionario actual: {mi_diccionario}")

# clear(): Elimina todos los ítems del diccionario.
mi_diccionario.clear()
print(f"Después de clear(): {mi_diccionario}")

# Crear un nuevo diccionario para siguientes ejemplos
mi_diccionario = {"nombre": "Ana", "edad": 25}

# update([other]): Actualiza el diccionario con pares clave-valor de otro diccionario.
mi_diccionario.update({"ciudad": "Barcelona", "edad": 26})
print(f"Después de update(): {mi_diccionario}")

# setdefault(key[, default]): Si la clave está en el diccionario, devuelve su valor. Si no, la inserta con el valor por defecto.
ciudad = mi_diccionario.setdefault("ciudad", "Desconocida")
print(f"Ciudad: {ciudad}, Diccionario actual: {mi_diccionario}")
