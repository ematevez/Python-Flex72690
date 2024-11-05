# Tema: Actividad práctica con funciones en Python

# Actividad: Determinar si un año es bisiesto

def es_anio_bisiesto(anio):
    """
    Determina si un año es bisiesto.
    
    Parámetros:
        anio (int): Año a evaluar.
    
    Retorna:
        str: Mensaje indicando si el año es bisiesto o no.

    Ejemplos:
        - es_anio_bisiesto(2012) -> "El año 2012 es bisiesto."
        - es_anio_bisiesto(2010) -> "El año 2010 no es bisiesto."
    """
    if not isinstance(anio, int):
        return "Por favor, ingrese un número entero válido para el año."
    
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return f"El año {anio} es bisiesto."
    else:
        return f"El año {anio} no es bisiesto."

# Pruebas
print(es_anio_bisiesto(2012))
print(es_anio_bisiesto(2010))
print(es_anio_bisiesto(2000))
print(es_anio_bisiesto(1900))


# Actividad: Función para calcular el área de un rectángulo

def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo dada su base y altura.
    
    Parámetros:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.
    
    Retorna:
        float: El área del rectángulo.

    Ejemplo:
        - area_rectangulo(15, 10) -> 150
    """
    return base * altura

# Pruebas
print(f"Área del rectángulo (base=15, altura=10): {area_rectangulo(15, 10)}")


# Actividad: Función para calcular el área de un círculo

import math

def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    
    Parámetros:
        radio (float): El radio del círculo.
    
    Retorna:
        float: El área del círculo.

    Ejemplo:
        - area_circulo(5) -> 78.53975
    """
    return math.pi * radio**2

# Pruebas
print(f"Área del círculo (radio=5): {area_circulo(5)}")


# Actividad: Función que compara dos números y devuelve una relación

def relacion(num1, num2):
    """
    Compara dos números y devuelve su relación.
    
    Parámetros:
        num1 (int/float): Primer número.
        num2 (int/float): Segundo número.
    
    Retorna:
        int: 1 si num1 > num2, -1 si num1 < num2, 0 si son iguales.

    Ejemplos:
        - relacion(5, 10) -> -1
        - relacion(10, 5) -> 1
        - relacion(5, 5) -> 0
    """
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0

# Pruebas
print(f"Relación entre 5 y 10: {relacion(5, 10)}")
print(f"Relación entre 10 y 5: {relacion(10, 5)}")
print(f"Relación entre 5 y 5: {relacion(5, 5)}")


# Actividad: Función que calcula el punto intermedio entre dos números

def intermedio(num1, num2):
    """
    Calcula el punto intermedio entre dos números.
    
    Parámetros:
        num1 (int/float): Primer número.
        num2 (int/float): Segundo número.
    
    Retorna:
        float: El punto intermedio de num1 y num2.

    Ejemplo:
        - intermedio(-12, 24) -> 6.0
    """
    return (num1 + num2) / 2

# Pruebas
print(f"Punto intermedio entre -12 y 24: {intermedio(-12, 24)}")


# Actividad: Función que recorta un número entre dos límites

def recortar(numero, limite_inferior, limite_superior):
    """
    Recorta un número entre un límite inferior y un límite superior.
    
    Parámetros:
        numero (int/float): Número a recortar.
        limite_inferior (int/float): Límite inferior.
        limite_superior (int/float): Límite superior.
    
    Retorna:
        int/float: El número recortado dentro de los límites.

    Ejemplo:
        - recortar(15, 0, 10) -> 10
    """
    if numero < limite_inferior:
        return limite_inferior
    elif numero > limite_superior:
        return limite_superior
    else:
        return numero

# Pruebas
print(f"Recortar 15 entre los límites 0 y 10: {recortar(15, 0, 10)}")

# Referencias
# - Año bisiesto: https://es.wikipedia.org/wiki/A%C3%B1o_bisiesto
# - Funciones matemáticas en Python: https://docs.python.org/3/library/math.html
# - Comparación de números y operadores de Python: https://docs.python.org/3/reference/
