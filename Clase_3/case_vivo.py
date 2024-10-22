# Unidad 3: Métodos de Colecciones y Operadores Básicos

# Repaso/consultas de la clase práctica en vivo anterior
# Aquí puedes incluir un resumen de lo visto en la clase anterior.

# Actividad: Colecciones 1
# Consigna:
# Utilizando todo lo que sabes sobre cadenas, listas y sus métodos internos,
# transforma el siguiente texto.

"""
Notas:
Estructura: He agregado comentarios para cada actividad y secciones en el código para que los alumnos puedan seguir fácilmente lo que se está haciendo.
Ejemplos: Cada actividad incluye un ejemplo práctico y resultados esperados para que los estudiantes puedan comprender mejor cada concepto.
Interactividad: En la actividad 3 y la actividad de expresiones anidadas, se incluye el uso de input para hacer las actividades más interactivas y permitir que los estudiantes ingresen sus propios datos.

"""

#! Descripción de la actividad Practica 1. 
#! Utilizando todo lo que sabes sobre cadenas, listas y sus métodos internos, transforma este texto:

# Actividad: Colecciones 2
# Consigna: Analizar e interpretar los siguientes conjuntos en Python.

# # Ejemplo 1: Unión de conjuntos
my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.union(my_set_2)
print("Unión de conjuntos:", my_new_set)

# Ejemplo 2: Intersección de conjuntos
my_new_set_intersection = my_set_1.intersection(my_set_2)
print("Intersección de conjuntos:", my_new_set_intersection)

# Ejemplo 3: Diferencia de conjuntos
my_new_set_difference = my_set_2.difference(my_set_1)
print("Diferencia de conjuntos:", my_new_set_difference)

print("\n--- Fin de la Actividad Colecciones 2 ---\n")


# Actividad: Colecciones 3
# Consigna: Crear un diccionario de divisas y solicitar al usuario que ingrese una divisa.

divisas = {'Dolar': '$', 'Euro': '€', 'Libra': '£'}

# Solicitar divisa al usuario
divisa_input = input("Ingrese la divisa que desea visualizar: ")

# Verificar si la divisa existe en el diccionario
if divisa_input in divisas:
    print(f"La divisa {divisa_input} es: {divisas[divisa_input]}")
else:
    print("La divisa no se encuentra disponible.")

print("\n--- Fin de la Actividad Colecciones 3 ---\n")


#CODIGO DE DANIEL =============================================
# dicc = {'Dolar':'$','Euro':'€', 'Libra':'£'}
# divisa = input('Ingrese el tipo de divisa (Dolar, Euro, Libra):')
 
# if (divisa == 'Dolar') or (divisa == 'Euro') or (divisa == 'Libra'):
#     print(f'El simbolo de {divisa} es {dicc.get(divisa)}')
# else:
#     print(f'No existe la divisa {divisa}.')




# Actividad: Operadores relacionales
# Consigna: Calcular el resultado de cada expresión.

expresiones = [
    False == True,
    10 >= 2 * 4,
    33 / 3 == 11,
    True > False,
    True * 5 == 2.5 * 2
]

# Guardar los resultados en una nueva lista
resultados_relacionales = [exp for exp in expresiones]
print("Resultados de expresiones relacionales:", resultados_relacionales)

print("\n--- Fin de la Actividad Operadores Relacionales ---\n")


# Actividad: Operadores lógicos
# Consigna: Calcular el resultado de cada expresión y almacenarlo en una nueva lista.

expresiones_logicas = [
    not False,
    not 3 == 5,
    33 / 3 == 11 and 5 > 2,
    True or False,
    True * 5 == 2.5 * 2 or 123 >= 23,
    12 > 7 and True < False
]

# Guardar los resultados en una nueva lista
resultados_logicos = [exp for exp in expresiones_logicas]
print("Resultados de expresiones lógicas:", resultados_logicos)

print("\n--- Fin de la Actividad Operadores Lógicos ---\n")


# Actividad: Expresiones anidadas
# Consigna: Crear una variable que almacene si se cumplen todas las condiciones.

"""
NOMBRE sea diferente de cuatro asteriscos “****”
EDAD sea mayor que 5 y a su vez menor que 20
Que la longitud de NOMBRE sea mayor o igual a 4  pero a la vez menor que 8
EDAD multiplicada por 3 sea mayor que 35

"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

# Verificamos las condiciones
condiciones_cumplidas = (
    nombre != "" and 5 < edad < 20 and 4 <= len(nombre) < 8 and edad * 3 > 35
)

# Resultado de las condiciones
print("Se cumplen todas las condiciones:", condiciones_cumplidas)

print("\n--- Fin de la Actividad Expresiones Anidadas ---\n")


# Cierre y preguntas
# Resumen de la clase repasando los puntos clave vistos durante la unidad.
# Espacio para consultas finales.
print("Fin de la Unidad 3: Métodos de Colecciones y Operadores Básicos")
