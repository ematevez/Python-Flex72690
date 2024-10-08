# -*- coding: utf-8 -*-
"""Clase2-72690

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vUKZPoNhzDx5z17gA1YGz1lEPfHSp4bt

# Listas ( heterogeneas )
"""

[2, 4, 651, 1, 1, 2, 1, 1, 123, 1, 1, 1]

[25, 34, 'hola', 'otro string', 3]

[]
['elemento']

print(type([25, 34, 'hola', 'otro string', 3]))

lista1 = [1, 2, 3, 4, 1]
edad = 25
lista2 = [1, 2+2*15, 3,'pepe', 'roque', lista1, -15, type(edad)]

print(lista2)

"""# Listas y Strings

Index
"""

cadena = 'esta es cadena de prueba'
print(cadena[5])

lista = [1, 2, 3, 'pepe', 'roque']
#        0  1  2   3       4 -> subiendo...
#        -5 -4 -3  -2      -1
print(lista[3])
print(lista[-1])
# Estos 2 accesos generan un error
# print(cadena[55])
# print(lista[55])

"""Slicing"""

cadena = 'esta es cadena de prueba'
# print(cadena)
# print(cadena[3:15])
# print(cadena[3:15:3])
# print(cadena[3:])
# print(cadena[:15])
# print(cadena[-5:-2])
# print(cadena[4:-5])
print(cadena[-15:10])
# print(cadena[::-1])
# print(cadena)
# cadena = cadena[4:8]
# otra_variable = cadena[4:8]

lista = [1, 2, 3,'pepe', 'roque']

print(lista)
print(lista[2:4])
print(lista[2:4:2])
print(lista[2:])
print(lista[:3])
print(lista)

# lista = lista[2:4]
# print(lista)

# lista[1] = 'Aca estaba el numero 2'
# print(lista)

# lista[1] = lista[3:]
# print(lista)

# Para poder volver a utilizar el valor en el futuro

# segunda_lista = lista[2:4]
# print(segunda_lista)
# print(lista)

# segunda_lista = lista[::2]
# print(segunda_lista)
# print(lista)

[1,2,3,4,5]
2+2

"""concatenación"""

cadena = 'esta es cadena de prueba'
cadena_concatenada = cadena + ' soy pepe'
print(cadena_concatenada)

lista1 = [1, 2, 3, 'pepe', 'roque']
# lista_concatenada = lista1 + cadena
# lista_concatenada = lista1 + [cadena, 123]
lista2 = lista1 + cadena
# lista2 = [cadena]
print(lista1)
print(lista2)
# lista_concatenada = lista1 + lista2
# print(lista_concatenada)

# cadena1 = 'esta es cadena de prueba'
# cadena2 = ' otro gato'
# print(cadena1 + cadena2)
# lista1 = [1, 2, 3,'pepe', 'roque']
# lista2 = [6,7,8,1]
# print(lista1 + lista2)
# print(lista1 + [cadena1])

"""Inmutabilidad/Mutabilidad"""

cadena = 'claro'
# cadena[3] = 's'
cadena = cadena[:3] + 's' + cadena[4:]
print(cadena)

lista = ['primero', 'segundo', 'tercero']
print(lista)
print(lista[1])
lista[1] = 'cuarto'
print(lista)
print(lista[1])
lista[1] = 123
print(lista)
print(lista[1])
lista[1] = [1,2,3,4,5,'eaea']
print(lista)
print(lista[1])

"""Asignacion por slicing"""

lista = ['primero', 'segundo', 'tercero', 'cuarto', 'quinto']
print(lista)
print(lista[1:3])

lista[1:3] = [2, 3,'otro dato en string']
print(lista)

lista[1:3] = ['mas datos']
print(lista)

lista[1:3] = []
print(lista)

# print(lista[1:3])
# lista[1:3] = ['soy', 'mas', 'de', 'un', 'valor']
# print(lista)

lista[1:3] = 'hola' # -> implicitamente hace esto list('hola')
print(lista)

# print(list('hola pepito corre por la pradera'))
# print(list(2))
# lista_de_prueba = [2]

# lista = ['primero', 'segundo', 'tercero', 'cuarto', 'quinto']
# print(lista)
# print(lista[1:55])

lista[1:3] = ['soy', 'mas', 'de', 'un', 'valor']
print(lista)


lista[1:5] = []
print(lista)

# lista[1:3] = 'pepe'
# # print(list('hola')) # -> ['p', 'e', 'p', 'e']
# print(lista)

# # lista[1:3] = 4 # genera un error
# lista[1:3] = [4]
# print(lista)

"""Borrar valores con slicing o vaciar lista"""

lista = ['primero', 'segundo', 'tercero', 'cuarto', 'quinto']
print(lista)
lista[1:3] = []
print(lista)
# lista[1:3] = []
# print(lista)
# lista[::2] = [] # Genera error ya que no les permite la asignación con el salto de valores
lista = []
# lista.clear()
print(lista)

"""# Funciones de listas

append
"""

lista = [1, 2, 3, 'pepe', 'roque']
print(lista)
[1, 2, 3, 'pepe', 'roque'].append('otro valor')
lista.append('otro valor')
print(lista)
lista.append(['otro valor', 2])
print(lista)
# lista = lista + ['otro valor']
# print(lista)
# lista = lista + [['otro valor', 2]]
# print(lista)
# print(lista[0], lista[1])

"""len"""

lista = [1, 2, 3, 'pepe', 'roque']
print(len(lista))

lista = [1,2+2,3]
lista.append(int(input('Ingresa un numero: ')))

"""pop"""

lista = [1, 2, 3, 'pepe', 'roque']
lista.pop(2)
print(lista)

# valor_extraido = lista.pop()
# valor_extraido = lista.pop(3)
# print(lista)
# print(valor_extraido)
# lista.pop()
# print(lista)

"""count"""

lista = [1, 2, 3, 'pepe', 2, 'roque', 2]
# print(lista.count())
print(lista.count(2))
print(lista.count(4))
print(lista.count('pepe'))

"""index ( salteos para buscar, inexistencia )"""

lista = ['pepe', 'dato1', 'dato2', 'dato3', 'pepe', 'roque', 'pepe']
print(lista.index('pepe'))
print(lista.index('pepe', 1))
# print(lista.index('pepe', 5, 6))
# print(lista.index('pepe', 7))

# print(lista.index('salto')) # genera error al no encontrar el dato que se busca

"""# Break

# Tuplas ( heterogeneas )
"""

lista = [1,2,3,'pepe','gato']
tupla = (1,2,3,'pepe','gato')
tupla1 = 1,2,3,'pepe','gato'

print(type(lista))
print(type(tupla))
print(type(tupla1))

lista = [1]
print(type(lista))
entero = (1)
print(type(entero))
tupla = (1,)
print(type(tupla))
tupla = 1,
print(type(tupla))

lista = []
print(type(lista))
# tupla = ,
# print(type(tupla))
tupla = ()
print(type(tupla))

# lista = [2]
# tupla = ('2')
# tupla = ('2',)
# tupla = ('pepe',)
# tupla = (2,)
# tupla = (2)
tupla = 2,
# tupla = 'pepito corre loco',
# tupla = '',
# tupla = 2, 3, 4, 5
# print(tupla)
# print(type(lista))
print(type(tupla))

"""Inmutabilidad"""

lista = [1,2,3,'pepe','gato']
lista[1] = 'otro valor'
print(lista)

tupla = (1,2,3,'pepe','gato')
tupla[1] = 'otro valor'
print(tupla)

tupla = (1,2,3,'pepe','gato')
print(tupla[3])

lista = [1,2,3,4]
lista.clear()
lista = []

"""Vaciar"""

tupla = (1,2,3,'pepe','gato')
print(tupla)
print(type(tupla))
tupla = ()
print(tupla)
print(type(tupla))
tupla = tuple()
print(type(tupla))

"""Casting"""

tupla = tuple([2,3,4])
print(type(tupla))
print(tupla)
lista_nueva = list(tupla)
print(lista_nueva)

lista = list()
print(type(lista))

print(list('ricardo'))
print(tuple('ricardo'))
print(str(tuple('ricardo')))
str(tuple('ricardo'))

"""Index y slicing"""

tupla = (1,2,3,'pepe','gato')
print(tupla[2])
print(tupla[1:])
print(tupla[::2])
print(tupla)

"""Concatenación"""

tupla1 = (1,2,3)
tupla2 = ('pepe','gato')
tupla3 = tupla1 + tupla2
print(tupla3)
tupla1 = tupla1 + tupla3
print(tupla1)

variable = 123
variable = 432
variable = 'un string'

"""# Funcionalidades de las tuplas

len
"""

tupla34 = (1,2,3,'pepe','gato')
print(len(tupla34))

"""count"""

tupla = (1,'pepe', 2,3,'pepe','gato','pepe')
print(tupla.count('pepe'))
# print((1,'pepe', 2,3,'pepe','gato','pepe').count('pepe'))

"""index ( salteos para buscar, inexistencia )"""

tupla = ('pepe', 1, 2, 3, 'pepe', 'roque', 'pepe')
print(tupla.index('pepe'))
print(tupla.index(1))
print(tupla.index('pepe', 1))
print(tupla.index('pepe', 5, 6))
# print(tupla.index('pepe', 7))

# print(tupla.index('salto')) # genera error al no encontrar el dato que se busca

"""Casting"""

tupla = ('pepe', 1, 2, 3, 'pepe', 'roque', 'pepe')
print(tupla)
lista_desde_tupla = list(tupla)
print(lista_desde_tupla)

tupla_desde_lista = tuple(lista_desde_tupla)
print(tupla_desde_lista)

"""Anidación ( acceso )

lista = [1,2,3,'pepe','gato', ['lista', 'interna'], ('tupla', 'tupla2')]

 lista[-1][1] -> 'tupla2'

 lista[-1][1][2] -> 'p'

 [1,2,3,'pepe','gato', ['lista', 'interna'], ('tupla', 'tupla2')][-1][1]

 ('tupla', 'tupla2')[1]

 'tupla2'
"""

lista = [1,2,3,'pepe','gato', ['lista', 'interna'], ('tupla', 'tupla2')]
print(lista)
print(lista[-1]) # -> print(('tupla', 'tupla2'))
print(lista[-1][1]) # es como hacer esto -> print(('tupla', 'tupla2')[1])
print(lista[-1][1][3]) # es como hacer esto -> print('tupla2'[3])

# print(('tupla', 'tupla2')[0])
# lista[-1] = 2
# print(lista)

# lista[-2][1] = 2
# print(lista)

# variable = ('tupla', 'tupla2')
# variable = 2
# ...
# ...
# ...
# ...


# type(print(lista))

tupla = (1,2,3,'pepe','gato', 2, ('tupla', 'tupla2'))
print(tupla)
print(tupla[-2])
print(tupla[-2][0])
# print(tupla[5][0])
tupla[-2][0] = 2
print(tupla)

# print(tupla[5][1][2])
# print(['lista', 'interna'][1][2])
# print('interna'[2])
# print('t')

# print(lista[-1])
# print(lista[-1][1])
# print(len(lista[-1]))
# lista[-2][1] = 'otra lista'
# lista[-1][1] = 'otra lista' # Genera error
# print(lista)
# print(lista[-1])

# print(tuple(lista))

tupla = (1,2,3,'pepe','gato', ['lista', 'interna'], ('tupla', 'tupla2'))
print(tupla)
tupla[-2][1] = 'otra lista'
print(tupla)

lista = [1,2,3,'pepe','gato', ['lista', 'interna'], ('tupla', 'tupla2')]
lista[2] = 'aca estaba el numero 3'
# lista[-1][0] = 'soy un numero'
lista[-2][0] = 'soy un numero'
print(lista)

tupla = (1,2,3,'pepe','gato', ['lista', 'interna'], ('tupla', 'tupla2'))
# tupla[2] = 'aca estaba el numero 3'
# lista[-1][0] = 'soy un numero'
tupla[-2][0] = 'soy un numero'
print(tupla)

"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla."""

variable1 = input('Ingrese la primera asignatura')
variable2 = input('Ingrese la segunda asignatura')
variable3 = input('Ingrese la tercera asignatura')
variable4 = input('Ingrese la cuarta asignatura')
variable5 = input('Ingrese la quinta asignatura')
asignaturas = [variable1, variable2, variable3, variable4, variable5]
print(f'Las asignaturas son: {asignaturas}')

"""Pedir 5 datos para generar el listado de opciones y luego solicitar una ubicacion y mostrar el dato que ocupa dicha ubicacion"""

listado = []
opcion1 = input("dato 1: ")
opcion2 = input("dato 2: ")
opcion3 = input("dato 3: ")
opcion4 = input("dato 4: ")
opcion5 = input("dato 5: ")
listado.append(opcion1)
listado.append(opcion2)
listado.append(opcion3)
listado.append(opcion4)
listado.append(opcion5)

variable = int(input('Ingrese un numero de 1 a 5: '))

elemento = listado[variable]

# listado[int(input('Ingrese un numero de 1 a 5: '))]
print('El elemento seleccionado es:', elemento)
# print('El elemento seleccionado es:', listado[int(input('Ingrese un numero de 1 a 5: ')) - 1])

"""Descripción de la actividad.

En esta actividad, podrás poner en práctica todo lo aprendido durante la sesión.  

Dadas dos listas LISTA1 y LISTA2 debes realizar las siguientes tareas:

- Añade a la LISTA1 el int 456789 y luego el string “Hola Mundo”
- Luego añade a la LISTA2 el string “Hola y Adios” y luego el int 5555
- Genera una LISTA3 con todos los elementos de la LISTA1 sin considerar el último elemento
- Genera una LISTA4 con todos los elementos de la LISTA2 menos el primero y el último elemento
- Finalmente, genera una LISTA5 con los elementos de la LISTA4 y de la LISTA3
"""

lista1 = [1, 2, 3, 4, 'pepe', 'hola']
lista2 = [1, 5, ('mi', 'gato'), 'richard']

lista1.append(456789)
lista1.append('Hola Mundo')

lista2[6:] = ['Hola y Adios',5555]

lista3 = lista1[:-1]

lista4 = lista2[1:-1]

lista5 = lista4 + lista3

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)

lista1.append(456789)
lista1.append('Hola Mundo')
print(lista1)

lista2 = lista2 + ['Hola y Adios', 5555]
print(lista2)

lista3 = lista1[:-1]
print(lista3)

lista4 = lista2[1:-1]
print(lista4)

lista5 = lista4 + lista3
print(lista5)

lista1 = [1, 2, 3, 4, 'pepe', 'hola']
lista2 = [1, 5, ('mi', 'gato'), 'richard']

lista1.append(456789)
lista1.append('Hola Mundo')

lista2[4:] = ['Hola y Adios', 5555]

lista3 = lista1[:-1]

# lista1.pop()
# lista3 = lista1

lista4 = lista2[1:-1]

lista5 = lista4 + lista3


print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)

"""Descripción de la actividad.
A partir de una variable llamada tupla, imprimir por pantalla de forma ordenada, lo siguiente:
1. El último ítem de tupla
2. El número de ítems de tupla
3. La posición donde se encuentra el ítem 87 de tupla
4. Una lista con los últimos tres ítems de tupla
5. Un ítem que haya en la posición 8 de tupla
6. El número de veces que el ítem 7 aparece en tupla

Copia esta tupla para iniciar el ejercicio:
tupla = (8, 15, 4, 39, 5, 89, 87,  19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

"""

tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

# El último ítem de tupla
print(tupla[-1])
# El número de ítems de tupla
print(len(tupla))
# La posición donde se encuentra el ítem 87 de tupla
print(tupla.index(87))
# Una lista con los últimos tres ítems de tupla
print(list(tupla[-3:]))
# Un ítem que haya en la posición 8 de tupla
# Un ítem que haya en la indice 7 de tupla
print(tupla[7])
# El número de veces que el ítem 7 aparece en tupla
print(tupla.count(7))

tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

# El último ítem de tupla
print(tupla[-1])

# El número de ítems de tupla
print(len(tupla))

# La posición donde se encuentra el ítem 87 de tupla
print(tupla.index(87))

# Una lista con los últimos tres ítems de tupla
print(list(tupla[-3:]))

# Un ítem que haya en la posición 8 de tupla
print(tupla[8])

# El número de veces que el ítem 7 aparece en tupla
print(tupla.count(7))

tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

# 1
print(tupla[-1])

# 2
print(len(tupla))

# 3
print(tupla.index(87))

# 4
print(list(tupla[-3:]))

# 5
print(tupla[8])

# 6
print(tupla.count(7))

lista = ['ines', 'pablo', 'ignacio', 'bautista', 'justo']
print(lista)
# ['ines', 'pablo', 'ignacio', 'bautista', 'justo']
print(lista[1:3])
# ['pablo', 'ignacio']

lista[2:4] = ['valentina', 'julian']
# ['ines', 'pablo', 'ignacio', 'bautista', 'justo']
# ['ines', 'pablo', valentina', 'julian', 'justo']
print(lista)
# ['ines', 'pablo', valentina', 'julian', 'justo']

lista[1:4] = [' los del medio']
# ['ines', 'pablo', valentina', 'julian', 'justo']
# ['ines', ' los del medio', 'justo']
print(lista)
# ['ines', ' los del medio', 'justo']

print(lista[1:4])
# [' los del medio', 'justo']
lista[1:3] = ['no', 'me', 'los', 'banco']
# ['ines', 'no', 'me', 'los', 'banco']
print(lista)
# ['ines', 'no', 'me', 'los', 'banco']

lista[1:3] = ['hola']
# ['ines', 'no', 'me', 'los', 'banco']
# ['ines', 'hola', 'los', 'banco']
print(lista)
# ['ines', 'hola', 'los', 'banco']

"""# AFTER 7/8"""

variable1 = 2, 4, 'Pepe', 'Ricardo', 4.56
#           0  1     2        3        4  >>>>>>
#          -5  -4    -3      -2       -1  <<<<<<


print(variable1[4])
print(variable1[2:4])
print(variable1[:])
# print(variable1[::-1])
print(variable1[::])

nueva_variable = 2
print(nueva_variable)

mi_print = 'este string representaria un codigo que nos resuelve algun problema en especifico'

print(mi_print())

"""## Desafío Números (10 min)
Descripción de la actividad.

En nuestro trabajo, nos solicitan desarrollar un programa que permita calcular el promedio final de los equipos de futbol en un torneo.
Para ello, debemos considerar tres aspectos:

jugaron 20 partidos durante el torneo,
los partidos poseen diferente puntaje según el resultado, los partidos ganados 3 puntos, partido empatado 1 punto, partido perdido 0 puntos,
el promedio final resulta de la cantidad de puntos totales divididos la cantidad de partidos

La cantidad de partidos que debemos considerar a un equipo para el ejemplo se detallan a continuación:

partidos_ganados 8
partido_empatados 7
partido_perdidos 5

Importante: Cada una de las cantidades de partidos ganados, empatados o perdidos debe solicitarse al usuario utilizando la función input().
"""

partidos_jugados = 20

puntos_partidos_ganados = 3
puntos_partidos_empatados = 1
puntos_partidos_perdidos = 0

x = 8
y = 7
z = 5

puntos_totales = x * puntos_partidos_ganados + y

promedio_final = puntos_totales / partidos_jugados

print('El promedio final para tu equipo es', promedio_final, 'por partido')

partidos_jugados = 20

puntos_partidos_ganados = 5
puntos_partidos_empatados = 3
puntos_partidos_perdidos = 1

partidos_ganados = int(input('Cuantos partidos ganaste?'))
partidos_empatados = int(input('Cuantos partidos empataste?'))
partidos_perdidos = int(input('Cuantos partidos perdiste?'))

puntos_totales = partidos_ganados * puntos_partidos_ganados + partidos_empatados * puntos_partidos_empatados + partidos_perdidos * puntos_partidos_perdidos

promedio_final = puntos_totales / partidos_jugados

print('El promedio final para tu equipo es', promedio_final, 'por partido')


print('Cuantos puntos sacaste de los empates?', partidos_empatados * puntos_partidos_empatados)

print('El promedio final para tu equipo es', (int(input('Cuantos partidos ganaste?')) * 3 + int(input('Cuantos partidos empataste?'))) / 20, 'por partido')