
"""
Tema 6.2: Manejo de Excepciones en Python

En este módulo aprenderemos a manejar errores en Python mediante el uso de excepciones.
El manejo de excepciones es crucial para desarrollar programas robustos y prevenir interrupciones abruptas
que puedan afectar la experiencia del usuario.

Bibliografía recomendada:
- Documentación oficial de Python sobre manejo de excepciones: https://docs.python.org/3/tutorial/errors.html
- "Learning Python" de Mark Lutz
"""

# Introducción a las Excepciones
print("Introducción a las Excepciones")
"""
Las excepciones en Python son eventos que interrumpen el flujo normal de un programa. Estos eventos suelen ocurrir
debido a errores, como dividir por cero o intentar abrir un archivo inexistente. Python permite capturar estos
errores mediante excepciones para que el programa continúe su ejecución.
"""

# ¿Qué es un Bloque Try-Except?
print("¿Qué es un Bloque Try-Except?")
"""
El bloque try-except permite manejar excepciones de forma controlada. La estructura básica es:
try:
    # Código que puede causar una excepción
except ExceptionType:
    # Código para manejar la excepción
Si ocurre una excepción en el bloque try, se captura en el except y se ejecuta un código alternativo.
"""
# print(10/0)

# Ejemplo 1: Manejo de ZeroDivisionError
print("Ejemplo 1: Manejo de ZeroDivisionError")
try:
    resultado = 10 / 0
except FileNotFoundError:
    print("Error: No se puede dividir por cero.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
# Ejemplo 2: Manejo de FileNotFoundError
print("Ejemplo 2: Manejo de FileNotFoundError")
try:
    with open('archivo_no_existente.txt', 'r') as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("Error: El archivo no existe.")

# Uso de Else y Finally en Excepciones
print("Uso de Else y Finally en Excepciones")

# Bloque Else
print("Ejemplo del Bloque Else")
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
else:
    print("La operación fue exitosa, el resultado es:", resultado)

# Bloque Finally
print("Ejemplo del Bloque Finally")
try:
    archivo = open('mi_archivo.txt', 'w')
    archivo.write("Hola, mundo!")
except IOError:
    print("Error: No se pudo escribir en el archivo.")
finally:
    archivo.close()
    print("El archivo ha sido cerrado.")

# Excepciones Múltiples
print("Excepciones Múltiples")
"""
En Python, se pueden manejar múltiples excepciones en un solo bloque try-except, usando múltiples except para
diferentes tipos de errores.
"""

# Ejemplo de Manejo de Múltiples Excepciones
print("Ejemplo de Manejo de Múltiples Excepciones")
try:
    valor = int(input("Ingresa un número: "))
    resultado = 10 / valor
except ValueError:
    print("Error: Debes ingresar un número.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

# Ejemplo Detallado de Múltiples Excepciones
print("Ejemplo Detallado de Múltiples Excepciones")
def procesar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            numero = int(contenido.strip())
            resultado = 100 / numero
            print("El resultado es:", resultado)
    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")
    except ValueError:
        print("Error: El contenido del archivo no es un número válido.")
    except ZeroDivisionError:
        print("Error: El número en el archivo es cero, lo cual no es permitido.")

# Llamada a la función
procesar_archivo('datos.txt')

"""
Conclusión
El manejo de excepciones en Python es esencial para desarrollar programas confiables. La estructura try-except
ayuda a manejar errores y mejorar la experiencia del usuario al prevenir interrupciones abruptas. Las cláusulas
else y finally permiten un control más detallado sobre la gestión de errores y recursos, mientras que el manejo
de excepciones múltiples ofrece flexibilidad al manejar diferentes tipos de errores específicos.
"""
