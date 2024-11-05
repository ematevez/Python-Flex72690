# 4.1 Control de Flujo en Python

"""#! Descripción de la estructura del archivo:
#!Introducción y Explicación Teórica: Explica el flujo de ejecución, las instrucciones secuenciales y la importancia de controlar el flujo.

#!Declaraciones Condicionales: Incluye ejemplos de declaraciones condicionales if, elif, y else.

#!Bucles: Presenta ejemplos de bucles for y while, incluyendo iteraciones sobre rangos y colecciones.

#!Conclusión: Resume la importancia del control de flujo.
#!Función de Resumen: La función resumen_control_flujo contiene ejemplos adicionales para reforzar el aprendizaje.

"""

"""
Control de Flujo en Python
===========================

1. Definición del Flujo en Programación
---------------------------------------
En programación, el "flujo" se refiere a la secuencia en la que se ejecutan
las instrucciones de un programa. Imagina que un programa es como una receta
de cocina, donde cada paso debe seguirse en un orden específico para obtener el
resultado deseado. De manera similar, en un programa, las instrucciones se deben
ejecutar en una secuencia específica para lograr la funcionalidad correcta.

2. Importancia del Flujo en Programación
----------------------------------------
El control del flujo en un programa es crucial para la toma de decisiones y
la ejecución de bloques de código específicos según las condiciones presentes
durante la ejecución. Un control de flujo bien estructurado permite crear
programas más flexibles y robustos.

3. Ejecución Secuencial de Instrucciones
----------------------------------------
Por defecto, Python ejecuta las instrucciones de forma secuencial, es decir,
de arriba hacia abajo. Cada línea de código se ejecuta una tras otra en el orden
en que aparecen en el archivo. Sin embargo, la ejecución secuencial por sí sola
es insuficiente para manejar todas las situaciones; para eso, necesitamos
estructuras de control de flujo.
"""

# Ejemplo de Ejecución Secuencial
print("Inicio del programa")
print("Ejecutando paso 1")
print("Ejecutando paso 2")
print("Fin del programa")

"""
4. Manipulación del Flujo de Ejecución
---------------------------------------
Para que un programa responda a diferentes situaciones, necesitamos manipular
el flujo de ejecución. Esto se logra mediante:

- Declaraciones Condicionales: Permiten tomar decisiones en función de una
  condición específica.
- Bucles: Permiten repetir una sección de código varias veces, facilitando
  tareas repetitivas.
"""

# 4.1 Declaraciones Condicionales

"""
Las declaraciones condicionales permiten que el programa ejecute bloques de
código diferentes en función de condiciones específicas.

Estructura de una declaración condicional:
------------------------------------------
    if condicion:
        # Código a ejecutar si la condición es verdadera
    elif otra_condicion:
        # Código a ejecutar si la otra condición es verdadera
    else:
        # Código a ejecutar si ninguna condición anterior es verdadera
"""

# Ejemplo de Declaración Condicional
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Ejemplo adicional de declaración condicional con múltiples condiciones
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muy Bien")
elif nota >= 70:
    print("Bien")
else:
    print("Necesita mejorar")

# 4.2 Bucles

"""
Los bucles permiten que un bloque de código se ejecute repetidamente hasta que
se cumpla o deje de cumplirse una condición. Python ofrece dos tipos de bucles:

1. Bucle 'for': se utiliza para iterar sobre una secuencia, como una lista o un rango.
2. Bucle 'while': se utiliza para ejecutar un bloque de código mientras una
   condición sea verdadera.
"""

# Ejemplo de bucle 'for'
print("Bucle 'for' con un rango de 5:")
for i in range(5):
    print(f"Iteración {i}")

# Ejemplo de bucle 'for' para iterar sobre una lista
frutas = ["manzana", "banana", "cereza"]
print("Iterando sobre una lista de frutas:")
for fruta in frutas:
    print(f"Fruta: {fruta}")

# Ejemplo de bucle 'while'
contador = 0
print("Bucle 'while' que se ejecuta mientras contador sea menor que 3:")
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

# Ejemplo de bucle 'while' con una condición de entrada del usuario
print("Ejemplo con entrada de usuario:")
continuar = "s"
while continuar == "s":
    nombre = input("Ingrese su nombre: ")
    print(f"Hola, {nombre}")
    continuar = input("¿Desea continuar? (s/n): ")

"""
Conclusión
==========
El control de flujo es fundamental en programación. Sin la capacidad de tomar
decisiones y repetir acciones, los programas serían rígidos y poco funcionales.
El conocimiento de las estructuras de control de flujo en Python permite crear
programas más dinámicos y efectivos para manejar diferentes situaciones.
"""

# Resumen de conceptos con ejemplos prácticos
def resumen_control_flujo():
    print("Resumen del Control de Flujo en Python:")
    
    # Ejemplo de declaración condicional
    temperatura = 25
    if temperatura > 30:
        print("Hace calor.")
    elif temperatura < 15:
        print("Hace frío.")
    else:
        print("La temperatura es agradable.")

    # Ejemplo de bucle 'for' con diccionario
    edades = {"Ana": 25, "Luis": 32, "Marta": 18}
    print("Edades de las personas:")
    for nombre, edad in edades.items():
        print(f"{nombre} tiene {edad} años.")
    
    # Ejemplo de bucle 'while' que busca una condición específica
    num = 1
    while num <= 5:
        print(f"Número actual: {num}")
        num += 1

# Llamado a la función de resumen
resumen_control_flujo()
