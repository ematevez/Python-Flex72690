"""
Clase 8.5: Uso de la Función WITH
=================================

Objetivo:
- Comprender el uso de la función `with` para manejar archivos en Python.
- Explorar sus ventajas, como la gestión automática de recursos y el manejo de excepciones.
- Aprender a leer y escribir archivos utilizando bloques `with`.

Incluye ejemplos interactivos y ejercicios prácticos.
"""

def introduccion_with():
    print("Bienvenidos a la clase sobre el uso de la función `with`.")
    print("\n¿Qué es `with`?")
    print("- Es un gestor de contexto que facilita la gestión de recursos, como archivos.")
    print("- Asegura que los archivos se cierren automáticamente al finalizar el bloque.")
    print("- Mejora la legibilidad del código y reduce el riesgo de errores.")
    print("\nVentajas del uso de `with`:")
    print("- Gestión automática de recursos.")
    print("- Código más limpio y legible.")
    print("- Manejo adecuado de excepciones.")

# Ejemplo 1: Leer un archivo utilizando `with`
def leer_archivo_con_with():
    print("\nEjemplo 1: Leer un archivo con `with`.")
    nombre_archivo = "ejemplo.txt"
    print(f"Creando un archivo de ejemplo llamado '{nombre_archivo}'...\n")
    
    # Crear archivo para el ejemplo
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Hola, este es un archivo de ejemplo.\n")
        archivo.write("Aquí aprenderemos sobre el uso de with.\n")

    # Leer el archivo creado
    print("Leyendo el archivo:")
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print(contenido)

# Ejemplo 2: Escribir en un archivo utilizando `with`
def escribir_archivo_con_with():
    print("\nEjemplo 2: Escribir en un archivo con `with`.")
    nombre_archivo = "salida.txt"
    
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Hola, mundo\n")
        archivo.write("Este es un archivo creado con `with`.\n")
    
    print(f"Datos escritos en '{nombre_archivo}'. Leyendo el contenido:")
    with open(nombre_archivo, "r") as archivo:
        print(archivo.read())

# Ejemplo 3: Leer un archivo línea por línea utilizando `with`
def leer_lineas_con_with():
    print("\nEjemplo 3: Leer un archivo línea por línea con `with`.")
    nombre_archivo = "ejemplo_lineas.txt"

    # Crear archivo para el ejemplo
    with open(nombre_archivo, "w") as archivo:
        archivo.writelines([
            "Primera línea de texto.\n",
            "Segunda línea de texto.\n",
            "Tercera línea de texto.\n"
        ])

    # Leer línea por línea
    print("Leyendo líneas del archivo:")
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            print(linea, end="")  # Evitar nueva línea adicional

# Actividad Interactiva: Leer y escribir utilizando `with`
def actividad_interactiva():
    print("\nActividad: Leer y escribir un archivo utilizando `with`.")
    nombre_archivo = input("Ingresa el nombre del archivo que deseas crear o leer (con extensión): ")

    # Escribir en el archivo
    print("Escribe las líneas que deseas agregar al archivo. Escribe 'fin' para terminar:")
    with open(nombre_archivo, "w") as archivo:
        while True:
            linea = input("Línea: ")
            if linea.lower() == "fin":
                break
            archivo.write(linea + "\n")

    # Leer el archivo
    print("\n¿Quieres leer el contenido del archivo que acabas de crear? (sí/no)")
    opcion = input().strip().lower()
    
    if opcion == "sí":
        print(f"Contenido del archivo '{nombre_archivo}':")
        with open(nombre_archivo, "r") as archivo:
            print(archivo.read())
    else:
        print("Actividad completada. Puedes abrir el archivo manualmente para verificar el contenido.")

# Ejecución de la clase
if __name__ == "__main__":
    introduccion_with()
    leer_archivo_con_with()
    escribir_archivo_con_with()
    leer_lineas_con_with()
    actividad_interactiva()
