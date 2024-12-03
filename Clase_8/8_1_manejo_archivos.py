"""
Clase 8.1: Introducción al Manejo de Archivos
============================================

Objetivo:
- Entender la persistencia de datos.
- Diferenciar datos efímeros de datos persistentes.
- Aprender a leer y escribir archivos en Python.
- Introducir los formatos CSV y JSON.

Ejemplos prácticos para aplicar conceptos aprendidos.
"""

import csv
import json


def introduccion():
    print("Bienvenidos a la clase de Introducción al Manejo de Archivos.")
    print("\nConceptos clave:")
    print("- Persistencia: capacidad de guardar datos de manera permanente.")
    print("- Datos efímeros: existen solo durante la ejecución del programa.")
    print("- Datos persistentes: sobreviven al cierre del programa.")
    print("\nEn esta clase nos enfocaremos en el uso de archivos para persistencia.")


# Función 1: Crear y escribir en un archivo de texto
def escribir_archivo_texto():
    print("\nEjemplo 1: Escribir en un archivo de texto")
    with open("datos.txt", "a") as archivo:
        archivo.write("Este es un ejemplo de archivo de texto.\n")
        archivo.write("Aprender a manejar archivos es importante.\n")
    print("Archivo 'datos.txt' creado y datos escritos.")


# Función 2: Leer un archivo de texto
def leer_archivo_texto():
    print("\nEjemplo 2: Leer un archivo de texto")
    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
    print("Contenido del archivo 'datos.txt':")
    print(contenido)


# Función 3: Trabajar con CSV
def escribir_archivo_csv():
    print("\nEjemplo 3: Escribir datos en formato CSV")
    encabezados = ["nombre", "edad", "opinión"]
    datos = [
        ["Juan", 28, "Me gusta"],
        ["Ana", 34, "No me gusta"],
        ["Pedro", 23, "Me encanta"]
    ]

    with open("encuesta.csv", "w", newline="") as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(encabezados)
        escritor.writerows(datos)

    print("Archivo 'encuesta.csv' creado con datos de encuesta.")


def leer_archivo_csv():
    print("\nEjemplo 4: Leer datos de un archivo CSV")
    with open("encuesta.csv", "r") as archivo_csv:
        lector = csv.reader(archivo_csv)
        for linea in lector:
            print(linea)


# Función 4: Trabajar con JSON
def escribir_archivo_json():
    print("\nEjemplo 5: Escribir datos en formato JSON")
    datos = {
        "resultados": [
            {"nombre": "Juan", "edad": 28, "opinión": "Me gusta"},
            {"nombre": "Ana", "edad": 34, "opinión": "No me gusta"},
            {"nombre": "Pedro", "edad": 23, "opinión": "Me encanta"}
        ]
    }

    with open("resultados.json", "w") as archivo_json:
        json.dump(datos, archivo_json, indent=4)

    print("Archivo 'resultados.json' creado con datos en formato JSON.")


def leer_archivo_json():
    print("\nEjemplo 6: Leer datos de un archivo JSON")
    with open("resultados.json", "r") as archivo_json:
        datos = json.load(archivo_json)
    print("Datos del archivo 'resultados.json':")
    print(json.dumps(datos, indent=4))


# Función interactiva
def actividad_interactiva():
    print("\nActividad: Crea un archivo con tu propio contenido.")
    nombre_archivo = input("Ingresa el nombre del archivo (con extensión): ")
    contenido = input("Escribe el contenido que deseas guardar: ")

    with open(nombre_archivo, "w") as archivo:
        archivo.write(contenido)

    print(f"Archivo '{nombre_archivo}' creado con el contenido proporcionado.")
    print("\n¿Quieres leer el archivo que acabas de crear? (sí/no)")
    opcion = input().strip().lower()

    if opcion == "sí":
        with open(nombre_archivo, "r") as archivo:
            print("\nContenido del archivo:")
            print(archivo.read())
    else:
        print("Actividad completada.")


# Ejecución de la clase
if __name__ == "__main__":
    introduccion()
    escribir_archivo_texto()
    leer_archivo_texto()
    escribir_archivo_csv()
    leer_archivo_csv()
    escribir_archivo_json()
    leer_archivo_json()
    actividad_interactiva()
