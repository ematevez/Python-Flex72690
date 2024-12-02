import os

"""
Clase 8.2: Archivos en Python
=============================

Objetivo:
- Entender qué son los archivos y sus tipos.
- Diferenciar entre archivos de texto y archivos binarios.
- Aprender a leer y escribir archivos de texto usando Python.
- Practicar con los métodos read(), readline(), y readlines().

Este archivo contiene ejemplos interactivos y ejercicios para reforzar los conceptos.
"""

def introduccion_archivos():
    print("Bienvenidos a la clase sobre Archivos.")
    print("\nConceptos clave:")
    print("- Un archivo es una secuencia de bytes almacenada en un dispositivo.")
    print("- Los archivos pueden ser de texto o binarios.")
    print("\nEn esta clase nos centraremos en los archivos de texto.")
    print("Aprenderemos a leer y escribir archivos usando Python.")


# Ejemplo 1: Escribir en un archivo de texto
def escribir_archivo():
    print("\nEjemplo 1: Crear y escribir en un archivo de texto.")
    contenido = """Hola, mundo
Este es un archivo de texto creado desde Python.
Vamos a aprender a manejar archivos paso a paso."""
    with open("archivo_ejemplo.txt", "w") as archivo:
        archivo.write(contenido)
    print("Archivo 'archivo_ejemplo.txt' creado con éxito.")


# Ejemplo 2: Leer archivo usando read()
def leer_con_read():
    print("\nEjemplo 2: Leer todo el contenido del archivo con read().")
    with open("archivo_ejemplo.txt", "r") as archivo:
        contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)


# Ejemplo 3: Leer archivo línea por línea usando readline()
def leer_con_readline():
    print("\nEjemplo 3: Leer el archivo línea por línea usando readline().")
    with open("archivo_ejemplo.txt", "r") as archivo:
        linea = archivo.readline()
        while linea:
            print(linea, end="")  # Evita añadir una nueva línea extra
            linea = archivo.readline()
    print("\nFinal de archivo.")


# Ejemplo 4: Leer archivo y convertir líneas en una lista con readlines()
def leer_con_readlines():
    print("\nEjemplo 4: Leer todas las líneas del archivo usando readlines().")
    with open("archivo_ejemplo.txt", "r") as archivo:
        lineas = archivo.readlines()
    print("Líneas del archivo como lista:")
    print(lineas)
    print("Imprimiendo línea por línea:")
    for linea in lineas:
        print(linea, end="")


# Actividad interactiva: Leer un archivo proporcionado por el usuario
def actividad_interactiva():
    print("\nActividad: Lee un archivo que elijas.")
    nombre_archivo = input("Ingresa el nombre del archivo que deseas leer (incluye la extensión): ")
    try:
        with open(nombre_archivo, "r") as archivo:
            print(f"\nContenido del archivo '{nombre_archivo}':")
            print(archivo.read())
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró. Por favor, verifica el nombre e inténtalo de nuevo.")


# Ejecución de la clase
if __name__ == "__main__":
    introduccion_archivos()
    escribir_archivo()
    leer_con_read()
    leer_con_readline()
    leer_con_readlines()
    actividad_interactiva()





# # Si no existe el archivo
# def crear_txt_si_no_existe(ruta, contenido):
#     try:
#         if not os.path.exists(ruta):
#             with open(ruta, 'w') as archivo:
#                 archivo.write(contenido)
#             print(f"Archivo '{ruta}' creado exitosamente.")
#         else:
#             print(f"El archivo '{ruta}' ya existe.")
#     except Exception as e:
#         print(f"Ocurrió un error al manejar el archivo: {e}")

# # Ruta y contenido del archivo
# ruta_archivo = "nuevo_archivo.txt"
# contenido = "Este es el contenido inicial del archivo.\n¡Hola, mundo!"

# # Llamar a la función
# crear_txt_si_no_existe(ruta_archivo, contenido)