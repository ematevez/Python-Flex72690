"""
Esta es la clase 01 de python
"""
print("Hola")

# a = int(input("Ingrese el primer número: ")) 

# print("¡Bienvenido!")
# nombre = input("¿Cuál es tu nombre? ")    # Siempre doy una cadena de caracteres
# edad = input("¿Cuál es tu edad? ")
# print(nombre + " tiene " + edad + " años")


# numero_ingresado = 2
# print(numero_ingresado)
# print("================")
# numero_ingresado = "Ema"
# print(numero_ingresado)
# print("================")


# cadena_1 = "versátil"
# cadena_2 = "Python"
# cadena_3 = "es un lenguaje"
# cadena_4 = "de programación"
# print("================")
# print(cadena_1 +  cadena_2 + cadena_3 + cadena_4)
# print("================")
# print(cadena_2 + "     " + cadena_3 + "     " + cadena_4 + "    " + cadena_1)



#Actividad práctica 1.8 curso python Coderhouse, realizado por Daniel Greyling
#Mensaje de bienvenida
"""
Consigna

Trabajas en Coderhouse y te piden crear un programa que calcule la nota final de estudiantes del curso de Python. La nota final se calcula basándonos en tres notas previas de las cuales, cada una corresponde un porcentaje distinto de la nota final. Los porcentajes se detallan a continuación:

Los porcentajes asociados que debemos considerar de cada nota se detallan a continuación:

nota_1 cuenta como el 20% de la nota final

nota_2 cuenta como el 30% de la nota final

nota_3 cuenta como el 50% de la nota final

Aspectos a incluir

Tener en cuenta los temas vistos en la clase 1: números, print, input, variables, operaciones matemáticas, cadena de texto.

Los datos deben guardarse en variables y deben ser dinámicos por medio de input

"""

# print("Cálculadora notas finales, ingrese nota con valores de 0 a 10.")
# #Se ingresan vía input las notas
# nota_1 = input("Ingrese nota 1, vale 20% de la nota final.")
# nota_2 = input("Ingrese nota 2, vale 30% de la nota final.")
# nota_3 = float(input("Ingrese nota 3, vale 50% de la nota final."))

# print("================")
# print(type(nota_1))
# print("================")
# print(type(nota_2))
# print("================")
# print(type(nota_3))


# #Se calcula nota final realizando suma artimética de peso ponderado de cada nota
# nota_final = 20*int(nota_1)/100 + 30*int(nota_2)/100 + 50*int(nota_3)/100
# #Se muestra nota final
# print("La nota final es de", nota_final)


"""Descripción de la actividad. En nuestro trabajo, nos solicitan desarrollar un programa que permita calcular el promedio final de los equipos de futbol en un torneo. Para ello, debemos considerar tres aspectos: Jugaron 20 partidos durante el torneo. Los partidos poseen diferente puntaje según el resultado, los partidos ganados 3 puntos, partido empatado 1 punto, partido perdido 0 puntos. El promedio final resulta de la cantidad de puntos totales divididos la cantidad de partidos Descripción de la actividad. La cantidad de partidos que debemos considerar a un equipo para el ejemplo se detallan a continuación: partidos_ganados 8 partido_empatados 7 partido_perdidos 5 Importante: Cada una de las cantidades de partidos ganados, empatados o perdidos debe solicitarse al usuario utilizando la función input(). 
Aquí tienes el programa para calcular el promedio final de puntos de un equipo de fútbol basándote en los resultados de sus partidos:
"""

# # Solicitar al usuario la cantidad de partidos ganados, empatados y perdidos
# partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))
# partidos_empatados = int(input("Ingrese la cantidad de partidos empatados: "))
# partidos_perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))

# # Calcular la cantidad total de puntos obtenidos
# puntos_totales = (partidos_ganados * 3) + (partidos_empatados * 1) + (partidos_perdidos * 0)

# # Calcular el promedio final de puntos
# total_partidos = partidos_ganados + partidos_empatados + partidos_perdidos
# promedio_final = puntos_totales // total_partidos

# # Mostrar el promedio final
# print(f"El promedio final de puntos es: {promedio_final:.2f}")

#==================================================================================
# El slicing permite extraer una parte específica de una cadena utilizando la notación [inicio:fin:paso].


cadena = "Murcielago"
# print(cadena[0])  # Resultado: 'P'
# print(cadena[-1])  # Resultado: 'n'

# print(cadena[0:2])  # Resultado: 'Py'
print(cadena[::-2])  # Resultado: 'Pto'

# # Métodos de Cadenas
# # Python proporciona varios métodos integrados para trabajar con cadenas. Algunos de los métodos más comunes incluyen:

# # lower(): Convierte todos los caracteres de la cadena a minúsculas.

# # upper(): Convierte todos los caracteres de la cadena a mayúsculas.

# # replace(old, new): Reemplaza todas las apariciones de old con new.

# # split(delimiter): Divide la cadena en una lista de subcadenas, utilizando el delimitador especificado.

# # strip(): Elimina los espacios en blanco al principio y al final de la cadena.



# Copiar
# cadena = " Python es Increíble "
# print(cadena.lower())  # Resultado: ' python es increíble '
# print(cadena.upper())  # Resultado: ' PYTHON ES INCREÍBLE '
# print(cadena.replace("Increíble", "genial"))  # Resultado: ' Python es genial '
# print(cadena.split())  # Resultado: ['Python', 'es', 'Increíble']
# print(cadena.strip())  # Resultado: 'Python es Increíble'



# Copiar
# cadena1 = "Python"
# cadena2 = "es genial"
# resultado = cadena1 + " " + cadena2
# print(resultado)  # Resultado: 'Python es genial'

# partes = ["Python", "es", "genial"]
# resultado = " ".join(partes)
# print(resultado)  # Resultado: 'Python es genial'
# Ejemplos Prácticos
# #A continuación, se presentan algunos ejemplos prácticos que ilustran cómo trabajar con cadenas de texto en Python.


# Copiar
# # Crear una cadena
# saludo = "¡Hola, mundo!"

# # Manipulación de cadenas
# print(saludo.lower())  # Resultado: '¡hola, mundo!'
# print(saludo.upper())  # Resultado: '¡HOLA, MUNDO!'

# # Indexación y slicing
# print(saludo[0])  # Resultado: '¡'
# print(saludo[-1])  # Resultado: '!'
# print(saludo[1:5])  # Resultado: 'Hola'

# # Concatenación de cadenas
# nombre = "Python"
# frase = nombre + " es genial"
# print(frase)  # Resultado: 'Python es genial'

# # Uso de métodos de cadena
# frase_modificada = frase.replace("genial", "asombroso")
# print(frase_modificada)  # Resultado: 'Python es asombroso'