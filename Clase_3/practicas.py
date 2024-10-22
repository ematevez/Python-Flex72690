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


# ========================daniel======================================#

chain = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"
print("=============DANIEL===================")
print(chain)
print("================================")
lineas = chain.split("&")
final = []
final.append(lineas[1].capitalize() + '.')
final.append(lineas[2].capitalize() + '.')
final.append(lineas[3].capitalize() + '.')
final_espacios = '\n'.join(final)
print(final_espacios)
print("================================")


# ========================maxi=======================================#

cadena = 'gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista'
titulo = cadena.split('&')

print("=================MAXI===============")
print(cadena)
print("================================")
print(titulo)
print (titulo[0].capitalize() , "...")
print ("*" , titulo[1].capitalize() , ".")
print ("*" , titulo[2].capitalize() , ".")
print ("*" , titulo[3].capitalize() , ".")

# =============================================================