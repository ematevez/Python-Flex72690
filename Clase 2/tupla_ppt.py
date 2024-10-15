"""
Descripción de la actividad. 
A partir de una variable llamada tupla, imprimir por pantalla de forma ordenada, lo siguiente:

El último ítem de tupla
El número de ítems de tupla
La posición donde se encuentra el ítem 87 de tupla
Una lista con los últimos tres ítems de tupla
Un ítem que haya en la posición 8 de tupla
El número de veces que el ítem 7 aparece en tupla

Copia esta tupla para iniciar el ejercicio:
tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

"""

tupla_1 = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355, 7)

# El último ítem de la tupla
print("Último ítem de la tupla:", tupla_1[-1])

# El número de ítems de la tupla
print("Número de ítems en la tupla:", len(tupla_1))

# La posición donde se encuentra el ítem 87 en la tupla
print("Posición del ítem 87 en la tupla:", tupla_1.index(87))

# Una lista con los últimos tres ítems de la tupla
ultimos_tres = tupla_1[-3:]
print("Últimos tres ítems de la tupla:", ultimos_tres)

# Un ítem que haya en la posición 8 de la tupla
print("Ítem en la posición 8 de la tupla:", tupla_1[7])

# El número de veces que el ítem 7 aparece en la tupla
print("Número de veces que el ítem 7 aparece en la tupla:", tupla_1.count(7))

