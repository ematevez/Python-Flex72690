"""
Clase 8.4: Trabajo con Datos Reales - Archivos CSV
==================================================

Objetivo:
- Aprender a leer y escribir archivos CSV usando la biblioteca estándar `csv` en Python.
- Explorar la manipulación de datos tabulares y trabajar con diccionarios.
- Realizar un ejercicio práctico que incluye leer, procesar, y escribir datos en archivos CSV.

Incluye ejemplos interactivos y ejercicios prácticos.
"""

import csv

def introduccion_csv():
    print("Bienvenidos a la clase sobre archivos CSV.")
    print("\n¿Qué es un archivo CSV?")
    print("- Es un archivo de valores separados por comas (Comma-Separated Values).")
    print("- Utilizado para almacenar datos tabulares en texto plano.")
    print("- Es ampliamente compatible con herramientas y aplicaciones de análisis.")
    print("\n¿Qué aprenderemos?")
    print("- Cómo leer y escribir archivos CSV en Python.")
    print("- Cómo manipular datos utilizando listas y diccionarios.")

# Ejemplo 1: Leer un archivo CSV
def leer_csv():
    print("\nEjemplo 1: Leer un archivo CSV.")
    nombre_archivo = "datos.csv"
    
    # Crear un archivo de ejemplo
    print(f"Creando un archivo de ejemplo llamado '{nombre_archivo}'...\n")
    with open(nombre_archivo, "w", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['nombre', 'edad', 'ciudad'])
        escritor_csv.writerows([
            ['Juan', 30, 'Madrid'],
            ['Ana', 25, 'Barcelona'],
            ['Pedro', 23, 'Sevilla']
        ])
    
    # Leer el archivo creado
    print("Contenido del archivo:")
    with open(nombre_archivo, newline="") as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            print(fila)

# Ejemplo 2: Escribir en un archivo CSV
def escribir_csv():
    print("\nEjemplo 2: Escribir datos en un archivo CSV.")
    nombre_archivo = "salida.csv"
    
    datos = [
        ['nombre', 'edad', 'ciudad'],
        ['Juan', '30', 'Madrid'],
        ['Ana', '25', 'Barcelona'],
        ['Pedro', '23', 'Sevilla']
    ]
    
    with open(nombre_archivo, "w", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(datos)
    
    print(f"Datos escritos en '{nombre_archivo}'. Leyendo el contenido:")
    with open(nombre_archivo, "r", newline="") as archivo_csv:
        print(archivo_csv.read())

# Ejemplo 3: Leer CSV con diccionarios
def leer_csv_con_diccionarios():
    print("\nEjemplo 3: Leer un archivo CSV utilizando diccionarios.")
    nombre_archivo = "datos_dict.csv"
    
    # Crear un archivo de ejemplo
    with open(nombre_archivo, "w", newline="") as archivo_csv:
        campos = ['nombre', 'edad', 'ciudad']
        escritor_dict = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor_dict.writeheader()
        escritor_dict.writerows([
            {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'},
            {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Barcelona'},
            {'nombre': 'Pedro', 'edad': 23, 'ciudad': 'Sevilla'}
        ])
    
    # Leer el archivo con diccionarios
    print("Contenido del archivo:")
    with open(nombre_archivo, newline="") as archivo_csv:
        lector_dict = csv.DictReader(archivo_csv)
        for fila in lector_dict:
            print(fila)

# Actividad: Leer y escribir un archivo CSV
def actividad_practica_csv():
    print("\nActividad: Crear y procesar datos en un archivo CSV.")
    nombre_archivo = "estudiantes.csv"

    # Crear archivo con datos de estudiantes
    print(f"Creando un archivo llamado '{nombre_archivo}' con datos iniciales...\n")
    with open(nombre_archivo, "w", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['nombre', 'edad', 'grado'])
        escritor_csv.writerows([
            ['Juan', 15, '10'],
            ['Ana', 14, '9'],
            ['Pedro', 16, '11']
        ])
    
    # Leer y procesar datos
    print("Leyendo y procesando datos del archivo:")
    total_edad = 0
    conteo_estudiantes = 0

    with open(nombre_archivo, newline="") as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        encabezados = next(lector_csv)  # Saltar los encabezados
        for fila in lector_csv:
            print(fila)
            total_edad += int(fila[1])
            conteo_estudiantes += 1
    
    edad_promedio = total_edad / conteo_estudiantes
    print(f"\nEdad promedio de los estudiantes: {edad_promedio:.2f}")

    # Escribir resumen en un nuevo archivo
    nombre_resumen = "resumen_estudiantes.csv"
    print(f"\nCreando archivo de resumen '{nombre_resumen}'...")
    with open(nombre_resumen, "w", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['nombre', 'edad', 'grado'])
        escritor_csv.writerows([
            ['Juan', 15, '10'],
            ['Ana', 14, '9'],
            ['Pedro', 16, '11'],
            ['Edad promedio', edad_promedio, '']
        ])
    
    print(f"Resumen escrito en '{nombre_resumen}'. Contenido:")
    with open(nombre_resumen, "r") as archivo_csv:
        print(archivo_csv.read())

# Ejecución de la clase
if __name__ == "__main__":
    introduccion_csv()
    leer_csv()
    escribir_csv()
    leer_csv_con_diccionarios()
    actividad_practica_csv()
