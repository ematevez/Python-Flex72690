
#?------------------------------------------------------------------
#? Texto aleatorio guardado en un archivo: El programa genera un texto aleatorio a partir de una lista y lo guarda en texto_random.txt.

#? Lectura del texto: Luego, el programa levanta ese texto desde el archivo texto_random.txt para trabajar con él.

#? Aplicación de métodos: Se aplican los métodos de cadenas, listas, conjuntos y diccionarios, como lo hicimos anteriormente.

#? Guardar resultado: Finalmente, el texto procesado se guarda en resultado_procesado.txt.

#! Instrucciones:
#! Guarda este archivo como practica_metodos.py.
#! Ejecuta el archivo en tu entorno de desarrollo.
#! El archivo texto_random.txt se generará y se procesará con los métodos correspondientes. 
#! Los resultados finales se guardarán en resultado_procesado.txt.
#?------------------------------------------------------------------

#quiero hace un buscador de una plabra que me ponga por consola

import random

# ------------------------------------------------------------------
# PASO 1: Generar un texto aleatorio y guardarlo en un archivo .txt
# ------------------------------------------------------------------

# Texto aleatorio para generar
textos_random = [
    "Python es un lenguaje de programación de propósito general.",
    "Es popular para desarrollo web, ciencia de datos y automatización.",
    "Python tiene una gran cantidad de bibliotecas para diferentes áreas.",
    "Fue creado por Guido van Rossum y lanzado en 1991.",
    "La comunidad de Python es muy activa y siempre está contribuyendo."
]

# Seleccionamos un texto aleatorio
texto_aleatorio = random.choice(textos_random)

# Guardamos el texto aleatorio en un archivo
with open('texto_random.txt', 'w') as archivo:
    archivo.write(texto_aleatorio)

print(f"Texto random guardado en 'texto_random.txt': {texto_aleatorio}")

# ------------------------------------------------------------------
# PASO 2: Levantar el texto desde el archivo y comenzar a procesarlo
# ------------------------------------------------------------------

# Cargamos el texto desde el archivo
with open('texto_random.txt', 'r') as archivo:
    texto_cargado = archivo.read()

print("\nTexto cargado desde 'texto_random.txt':", texto_cargado)

# ------------------------------------------------------------------
# Aplicar Métodos de Cadenas
print("\n--- MÉTODOS DE CADENAS ---")

# Aplicar métodos de cadenas
print('Texto en mayúsculas (upper):', texto_cargado.upper())
print('Texto en minúsculas (lower):', texto_cargado.lower())
print('Capitalizar (capitalize):', texto_cargado.capitalize())
print('Título (title):', texto_cargado.title())
print('Conteo de "Python" (count):', texto_cargado.count('Python'))
print('Índice de la palabra "lenguaje" (find):', texto_cargado.find('lenguaje'))
print('Dividir el texto en una lista (split):', texto_cargado.split())
print('Reemplazar "Python" por "programación" (replace):', texto_cargado.replace("Python", "programación"))
print('Quitar espacios al principio y final (strip):', texto_cargado.strip())

# ------------------------------------------------------------------
# Aplicar Métodos de Listas
print("\n--- MÉTODOS DE LISTAS ---")

# Definimos una lista de ejemplo
mi_lista = [10, 20, 30, 40, 50]
print("Lista Original:", mi_lista)

# Aplicar algunos métodos de listas
mi_lista.append(60)  # Añadir un elemento
print("Lista después de append(60):", mi_lista)

mi_lista.insert(2, 25)  # Insertar en una posición específica
print("Lista después de insert(2, 25):", mi_lista)

mi_lista.remove(25)  # Eliminar un valor
print("Lista después de remove(25):", mi_lista)

mi_lista.reverse()  # Invertir la lista
print("Lista invertida:", mi_lista)

mi_lista.sort()  # Ordenar la lista
print("Lista ordenada:", mi_lista)

# ------------------------------------------------------------------
# Aplicar Métodos de Conjuntos
print("\n--- MÉTODOS DE CONJUNTOS ---")

# Definimos dos conjuntos de ejemplo
conjunto_1 = {1, 2, 3, 4}
conjunto_2 = {3, 4, 5, 6}
print("Conjunto 1:", conjunto_1)
print("Conjunto 2:", conjunto_2)

# Métodos de conjuntos
union = conjunto_1.union(conjunto_2)
print("Unión de conjuntos:", union)

interseccion = conjunto_1.intersection(conjunto_2)
print("Intersección de conjuntos:", interseccion)

diferencia = conjunto_1.difference(conjunto_2)
print("Diferencia (conjunto_1 - conjunto_2):", diferencia)

diferencia_simetrica = conjunto_1.symmetric_difference(conjunto_2)
print("Diferencia simétrica:", diferencia_simetrica)

# ------------------------------------------------------------------
# Aplicar Métodos de Diccionarios
print("\n--- MÉTODOS DE DICCIONARIOS ---")

# Definimos un diccionario de ejemplo
mi_diccionario = {'nombre': 'Alice', 'edad': 28, 'ciudad': 'Buenos Aires'}
print("Diccionario Original:", mi_diccionario)

# Aplicar algunos métodos de diccionarios
valor_nombre = mi_diccionario.get('nombre')  # Obtener valor
print("Valor de 'nombre':", valor_nombre)

claves = mi_diccionario.keys()  # Obtener las claves
print("Claves del diccionario:", list(claves))

valores = mi_diccionario.values()  # Obtener los valores
print("Valores del diccionario:", list(valores))

items = mi_diccionario.items()  # Obtener los pares clave-valor
print("Items del diccionario:", list(items))

# Actualizar el diccionario
mi_diccionario.update({'edad': 29, 'país': 'Argentina'})
print("Diccionario actualizado:", mi_diccionario)

# ------------------------------------------------------------------

# Guardar resultado final
resultado_procesado = texto_cargado.strip().replace("Python", "programación").title()

# Guardar el texto procesado en un archivo
with open('resultado_procesado.txt', 'w') as archivo:
    archivo.write(resultado_procesado)

print("\nTexto procesado guardado en 'resultado_procesado.txt':", resultado_procesado)
