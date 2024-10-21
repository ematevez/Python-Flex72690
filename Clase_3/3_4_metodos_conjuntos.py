# Métodos de Conjuntos en Python

# Los conjuntos en Python son colecciones desordenadas de elementos únicos.
# A continuación veremos ejemplos prácticos de varios métodos para trabajar con conjuntos.

# 1. copy() - Copia un conjunto
# El método copy() devuelve una copia superficial del conjunto original.

set1 = {1, 2, 3}
set2 = set1.copy()
print("Ejemplo copy():", set2)
# Salida: {1, 2, 3}

# 2. isdisjoint() - Verifica si dos conjuntos son disjuntos (no tienen elementos en común)
# El método isdisjoint() devuelve True si dos conjuntos no tienen elementos en común.

set1 = {1, 2, 3}
set2 = {4, 5, 6}
print("Ejemplo isdisjoint():", set1.isdisjoint(set2))
# Salida: True

# 3. issubset() - Verifica si un conjunto es subconjunto de otro
# El método issubset() devuelve True si todos los elementos del conjunto están en otro conjunto.

set1 = {1, 2}
set2 = {1, 2, 3, 4}
print("Ejemplo issubset():", set1.issubset(set2))
# Salida: True

# 4. issuperset() - Verifica si un conjunto es un superconjunto de otro
# El método issuperset() devuelve True si el conjunto contiene todos los elementos de otro conjunto.

set1 = {1, 2, 3, 4}
set2 = {1, 2}
print("Ejemplo issuperset():", set1.issuperset(set2))
# Salida: True

# 5. union() - Devuelve la unión de dos conjuntos
# El método union() devuelve un nuevo conjunto con todos los elementos de los conjuntos originales.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Ejemplo union():", set1.union(set2))
# Salida: {1, 2, 3, 4, 5}

# 6. difference() - Devuelve la diferencia entre dos conjuntos
# El método difference() devuelve un nuevo conjunto con los elementos que están en el conjunto original
# pero no en el otro conjunto.

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print("Ejemplo difference():", set1.difference(set2))
# Salida: {1}

# 7. difference_update() - Actualiza el conjunto eliminando los elementos presentes en otro conjunto
# El método difference_update() elimina del conjunto original todos los elementos que están en otro conjunto.

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.difference_update(set2)
print("Ejemplo difference_update():", set1)
# Salida: {1}

# 8. intersection() - Devuelve la intersección de dos conjuntos
# El método intersection() devuelve un nuevo conjunto con los elementos comunes a ambos conjuntos.

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print("Ejemplo intersection():", set1.intersection(set2))
# Salida: {2, 3}

# 9. intersection_update() - Actualiza el conjunto original con la intersección
# El método intersection_update() actualiza el conjunto original conservando solo los elementos comunes.

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print("Ejemplo intersection_update():", set1)
# Salida: {2, 3}

# OPERACIONES EXTRA CON CONJUNTOS

# 10. symmetric_difference() - Devuelve la diferencia simétrica de dos conjuntos
# El método symmetric_difference() devuelve un nuevo conjunto con los elementos que están en cualquiera
# de los conjuntos, pero no en ambos.

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print("Ejemplo symmetric_difference():", set1.symmetric_difference(set2))
# Salida: {1, 4}

# 11. add() - Agrega un elemento al conjunto
# El método add() agrega un nuevo elemento al conjunto. Si el elemento ya está presente, no pasa nada.

set1 = {1, 2, 3}
set1.add(4)
print("Ejemplo add():", set1)
# Salida: {1, 2, 3, 4}

# 12. remove() - Elimina un elemento del conjunto
# El método remove() elimina un elemento específico del conjunto. Si el elemento no está presente, lanza un error.

set1 = {1, 2, 3}
set1.remove(2)
print("Ejemplo remove():", set1)
# Salida: {1, 3}

# 13. discard() - Elimina un elemento sin lanzar error si no existe
# El método discard() elimina un elemento del conjunto, pero no lanza un error si el elemento no está presente.

set1 = {1, 2, 3}
set1.discard(4)  # No lanza error aunque el 4 no está en el conjunto
print("Ejemplo discard():", set1)
# Salida: {1, 2, 3}

# 14. clear() - Vacía un conjunto
# El método clear() elimina todos los elementos del conjunto.

set1 = {1, 2, 3}
set1.clear()
print("Ejemplo clear():", set1)
# Salida: set()


"""
Temas adicionales para agregar:
symmetric_difference(): Diferencia simétrica entre dos conjuntos.
add(), remove(), discard(), clear(): Métodos útiles para agregar, eliminar o vaciar conjuntos.

"""