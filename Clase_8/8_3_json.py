"""
Clase 8.3: Trabajando con Archivos JSON
=======================================

Objetivo:
- Entender qué es JSON y su utilidad.
- Aprender a serializar y deserializar datos JSON en Python.
- Practicar la lectura y escritura de archivos JSON.
- Explorar el uso de json.dumps() y json.loads() para cadenas JSON.

Incluye ejemplos interactivos y actividades prácticas.
"""

import json

def introduccion_json():
    print("Bienvenidos a la clase sobre Archivos JSON.")
    print("\nConceptos clave:")
    print("- JSON (JavaScript Object Notation) es un formato de texto ligero para el intercambio de datos.")
    print("- JSON representa datos como pares clave-valor.")
    print("- Es fácil de leer para humanos y procesar por máquinas.")
    print("\nEn esta clase aprenderemos a manejar JSON en Python, tanto en archivos como en cadenas.")


# Ejemplo 1: Escribir datos en un archivo JSON (Serialización)
def escribir_archivo_json():
    print("\nEjemplo 1: Escribir datos en un archivo JSON.")
    datos = {
        "nombre": "Juan",
        "edad": 30,
        "ciudad": "Madrid"
    }

    with open("datos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

    print("Archivo 'datos.json' creado con los datos:")
    print(json.dumps(datos, indent=4))  # Mostrar cómo se ve el JSON escrito


# Ejemplo 2: Leer datos desde un archivo JSON (Deserialización)
def leer_archivo_json():
    print("\nEjemplo 2: Leer datos desde un archivo JSON.")
    try:
        with open("datos.json", "r") as archivo:
            datos = json.load(archivo)
        print("Datos deserializados desde 'datos.json':")
        print(json.dumps(datos, indent=4))
    except FileNotFoundError:
        print("El archivo 'datos.json' no existe. Por favor, crea el archivo primero.")


# Ejemplo 3: Serialización de datos a una cadena JSON
def serializar_cadena_json():
    print("\nEjemplo 3: Convertir datos de Python a una cadena JSON (serialización).")
    datos = {
        "nombre": "Ana",
        "edad": 25,
        "ciudad": "Barcelona"
    }

    cadena_json = json.dumps(datos, indent=4)
    print("Cadena JSON generada:")
    print(cadena_json)


# Ejemplo 4: Deserialización de una cadena JSON
def deserializar_cadena_json():
    print("\nEjemplo 4: Convertir una cadena JSON a un objeto de Python (deserialización).")
    cadena_json = '{"nombre": "Ana", "edad": 25, "ciudad": "Barcelona"}'

    datos = json.loads(cadena_json)
    print("Datos deserializados:")
    print(datos)


# Actividad Interactiva: Crear y leer un archivo JSON personalizado
def actividad_interactiva():
    print("\nActividad: Crear y leer un archivo JSON personalizado.")
    nombre_archivo = input("Ingresa el nombre del archivo JSON (con extensión): ")
    
    # Crear el archivo JSON
    print("Introduce los datos para crear el archivo JSON:")
    datos = {}
    while True:
        clave = input("Clave (o escribe 'fin' para terminar): ")
        if clave.lower() == "fin":
            break
        valor = input("Valor: ")
        datos[clave] = valor

    with open(nombre_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4)
    print(f"Archivo '{nombre_archivo}' creado con los datos proporcionados.")

    # Leer el archivo JSON creado
    print("\n¿Quieres leer el contenido del archivo que acabas de crear? (sí/no)")
    opcion = input().strip().lower()

    if opcion == "sí":
        try:
            with open(nombre_archivo, "r") as archivo:
                contenido = json.load(archivo)
            print(f"Contenido del archivo '{nombre_archivo}':")
            print(json.dumps(contenido, indent=4))
        except Exception as e:
            print(f"Hubo un problema al leer el archivo: {e}")
    else:
        print("Actividad completada.")


# Ejecución de la clase
if __name__ == "__main__":
    introduccion_json()
    escribir_archivo_json()
    leer_archivo_json()
    serializar_cadena_json()
    deserializar_cadena_json()
    actividad_interactiva()
