"""
Módulo: Funciones Recursivas e Integradas

Este módulo explora la recursividad y las funciones integradas de Python. Incluye explicaciones detalladas y ejemplos
prácticos de funciones recursivas (con y sin retorno) y de funciones integradas comunes como int(), float(), str() y round().

Referencias:
- Documentación de Python: https://docs.python.org/3/library/functions.html
"""

# ---------------------------------------------------------------
# 1. Funciones Recursivas
# ---------------------------------------------------------------

# La recursividad es una técnica de programación en la que una función se llama a sí misma para resolver subproblemas
# de un problema más grande. Es útil para problemas que pueden dividirse en partes más pequeñas del mismo tipo.

# Ejemplo: Cuenta regresiva usando recursión
def cuenta_regresiva(n):
    """
    Imprime una cuenta regresiva desde n hasta 0, usando recursión.

    Args:
        n (int): El número desde el cual comienza la cuenta regresiva.
    """
    if n <= 0:  # Caso base: cuando n llega a 0 o menos
        print('¡Despegue!')
    else:
        print(n)
        cuenta_regresiva(n - 1)  # Llamada recursiva con n - 1

# Ejecución del ejemplo de cuenta regresiva
print("Ejemplo de cuenta regresiva:")
cuenta_regresiva(5)

# Ejemplo: Cálculo del factorial de un número usando recursión
def factorial(n):
    """
    Calcula el factorial de un número entero positivo n utilizando recursión.

    Args:
        n (int): El número para calcular su factorial.
    
    Returns:
        int: El factorial de n.
    """
    if n == 0:  # Caso base: el factorial de 0 es 1
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva con n - 1

# Ejecución del ejemplo de factorial
print("\nEjemplo de cálculo factorial:")
print("Factorial de 5:", factorial(5))  # Salida esperada: 120

# ---------------------------------------------------------------
# 2. Funciones Integradas en Python
# ---------------------------------------------------------------

# Python incluye una serie de funciones integradas que facilitan tareas comunes de programación.
# A continuación, se muestran algunos ejemplos de funciones integradas.

# Función int(): Convierte un valor a un número entero.
print("\nEjemplo de uso de int():")
numero_entero = int(2.5)  # Convierte un flotante a entero
print("Convertir 2.5 a entero:", numero_entero)  # Salida: 2

numero_entero = int("25")  # Convierte una cadena a entero
print("Convertir '25' a entero:", numero_entero)  # Salida: 25

# Función float(): Convierte un valor a un número de coma flotante.
print("\nEjemplo de uso de float():")
numero_flotante = float(2)  # Convierte un entero a flotante
print("Convertir 2 a flotante:", numero_flotante)  # Salida: 2.0

numero_flotante = float("2.5")  # Convierte una cadena a flotante
print("Convertir '2.5' a flotante:", numero_flotante)  # Salida: 2.5

# Función str(): Convierte un valor a una cadena de caracteres.
print("\nEjemplo de uso de str():")
cadena = str(2.5)  # Convierte un número a cadena
print("Convertir 2.5 a cadena:", cadena)  # Salida: '2.5'

cadena = str(True)  # Convierte un booleano a cadena
print("Convertir True a cadena:", cadena)  # Salida: 'True'

# Función round(): Redondea un número flotante al entero más cercano o a un número específico de decimales.
print("\nEjemplo de uso de round():")
numero_redondeado = round(2.6)  # Redondea al entero más cercano
print("Redondear 2.6 al entero más cercano:", numero_redondeado)  # Salida: 3

numero_redondeado = round(2.456, 2)  # Redondea a dos dígitos decimales
print("Redondear 2.456 a dos decimales:", numero_redondeado)  # Salida: 2.46

# ---------------------------------------------------------------
# Conclusión
# ---------------------------------------------------------------

"""
Conclusión:
La recursividad permite resolver problemas complejos dividiéndolos en subproblemas más simples.
Las funciones integradas de Python como int(), float(), str() y round() son herramientas fundamentales que 
facilitan la manipulación y conversión de datos en el código.

Al comprender estas funciones, los desarrolladores pueden escribir código más eficiente, claro y efectivo.

Referencias:
- https://docs.python.org/3/library/functions.html
"""
