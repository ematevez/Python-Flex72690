# parametros_y_argumentos.py

"""
Módulo: Parámetros y Argumentos en Funciones

En Python, es común trabajar con funciones que reciben datos para su procesamiento.
Es importante entender los conceptos de 'parámetros' y 'argumentos', así como
las diferentes formas de pasar estos argumentos (por posición o por nombre).
"""

# 1. Diferencia entre Parámetros y Argumentos
# ------------------------------------------------------

# Parámetros:
# Los parámetros son variables que se definen en la declaración de una función.
# Actúan como marcadores de posición para los valores que se pasarán a la función cuando se llame.

def sumar(a, b):
    """Función que suma dos números."""
    return a + b

# En este caso, `a` y `b` son parámetros de la función `sumar`.

# Argumentos:
# Los argumentos son los valores que se pasan a la función cuando se llama.
# Estos valores reemplazan a los parámetros en el momento de ejecución.

resultado = sumar(5, 3)
print(f"Resultado de sumar(5, 3): {resultado}")  # 5 y 3 son los argumentos pasados a `sumar`

# 2. Pasando Argumentos por Posición
# ------------------------------------------------------

# Los argumentos se pueden pasar a una función por posición,
# es decir, en el mismo orden en que los parámetros fueron definidos.

def resta(a, b):
    """Función que resta dos números."""
    return a - b

resultado = resta(10, 5)
print(f"Resultado de resta(10, 5): {resultado}")  # Imprimirá 5

# Si cambiamos el orden de los argumentos, los resultados cambiarán.
resultado = resta(5, 10)
print(f"Resultado de resta(5, 10): {resultado}")  # Imprimirá -5

# 3. Pasando Argumentos por Nombre
# ------------------------------------------------------

# Los argumentos también se pueden pasar a una función por nombre,
# especificando explícitamente a qué parámetro corresponde cada argumento.

resultado = resta(b=5, a=10)
print(f"Resultado de resta(b=5, a=10): {resultado}")  # Imprimirá 5

# En este caso, `a` recibe el valor 10 y `b` recibe el valor 5,
# independientemente del orden en que se pasaron los argumentos.

# 4. Ejemplos Adicionales: Combinando Argumentos Posicionales y Nombrados
# ------------------------------------------------------

# A veces es útil combinar argumentos por posición y por nombre en la misma función.
# Python permite pasar argumentos posicionales primero y luego argumentos nombrados.

def potencia(base, exponente=2):
    """Función que eleva una base a un exponente. El exponente predeterminado es 2."""
    return base ** exponente

# Ejemplo utilizando solo el argumento posicional (toma el valor predeterminado de `exponente`)
print(f"potencia(3): {potencia(3)}")  # Resultado: 9 (3^2)

# Ejemplo con argumentos posicionales y nombrados
print(f"potencia(2, exponente=3): {potencia(2, exponente=3)}")  # Resultado: 8 (2^3)

# Nota: Es importante siempre poner primero los argumentos posicionales,
# seguidos de los nombrados en la llamada de la función.

# 5. Uso de Parámetros y Argumentos Variables (*args y **kwargs)
# ------------------------------------------------------

# A veces, no sabemos de antemano cuántos argumentos puede recibir una función.
# En estos casos, Python nos permite usar `*args` y `**kwargs` para mayor flexibilidad.

# *args: permite pasar un número variable de argumentos posicionales.
# **kwargs: permite pasar un número variable de argumentos nombrados.

def suma_multiple(*args):
    """Función que suma una cantidad variable de números."""
    return sum(args)

print(f"suma_multiple(1, 2, 3, 4): {suma_multiple(1, 2, 3, 4)}")  # Resultado: 10

def imprimir_datos(**kwargs):
    """Función que imprime información proporcionada como argumentos nombrados."""
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

print("\nInformación del usuario:")
imprimir_datos(nombre="Carlos", edad=28, ocupacion="Ingeniero")


#?=====================================#

# args_kwargs_examples.py

# Ejemplo de uso de *args (argumentos variables) en Python

def sumar(*args):
    """
    Suma todos los números que se pasen como argumentos.
    *args permite pasar una cantidad variable de argumentos a la función.
    """
    total = 0
    for numero in args:
        total += numero
    return total

print("Ejemplos con *args:")
print(sumar(1, 2, 3))         # 6
print(sumar(4, 5))            # 9
print(sumar(10, 20, 30, 40))  # 100


# Pasar una lista usando * para desempaquetarla en argumentos individuales
numeros = [1, 2, 3, 4]
print("Sumar lista desempaquetada:", sumar(*numeros))  # 10


# Ejemplo de uso de **kwargs (argumentos con nombre) en Python

def info_persona(**kwargs):
    """
    Imprime la información de una persona.
    **kwargs permite pasar una cantidad variable de argumentos nombrados.
    """
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

print("\nEjemplos con **kwargs:")
info_persona(nombre="Alice", edad=30, ciudad="Madrid")
# Salida:
# nombre: Alice
# edad: 30
# ciudad: Madrid

info_persona(nombre="Bob", ocupacion="Ingeniero")
# Salida:
# nombre: Bob
# ocupacion: Ingeniero


# Pasar un diccionario usando ** para desempaquetarlo en argumentos nombrados
datos = {'nombre': 'Carlos', 'edad': 28, 'ciudad': 'Bogotá'}
print("\nInfo de persona desde diccionario desempaquetado:")
info_persona(**datos)
# Salida:
# nombre: Carlos
# edad: 28
# ciudad: Bogotá


# Ejemplo de paso de listas como argumentos en Python

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    La lista se pasa como un único argumento.
    """
    total = sum(numeros)
    promedio = total / len(numeros)
    return promedio

print("\nEjemplo de paso de listas como argumento:")
mi_lista = [10, 20, 30, 40]
print("Promedio de la lista:", calcular_promedio(mi_lista))  # 25.0


# Resumen de uso de *args, **kwargs y listas como argumentos

def ejemplo_completo(*args, **kwargs):
    """
    Ejemplo combinado de *args y **kwargs.
    Imprime todos los argumentos posicionales y nombrados.
    """
    print("\nArgumentos posicionales (*args):")
    for arg in args:
        print(arg)
    
    print("\nArgumentos nombrados (**kwargs):")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# Llamada a la función con combinación de *args y **kwargs
print("\nEjemplo combinado de *args y **kwargs:")
ejemplo_completo(1, 2, 3, nombre="Diana", edad=32, ciudad="Lima")
# Salida:
# Argumentos posicionales (*args):
# 1
# 2
# 3
#
# Argumentos nombrados (**kwargs):
# nombre: Diana
# edad: 32
# ciudad: Lima
"""Explicación
sumar(*args): muestra cómo usar *args para aceptar múltiples argumentos posicionales.
info_persona(**kwargs): ilustra cómo usar **kwargs para recibir múltiples argumentos nombrados.
calcular_promedio(numeros): usa una lista como argumento, mostrándose como un único parámetro.
ejemplo_completo(*args, **kwargs): combina ambos (*args y **kwargs) en una sola función para demostrar su versatilidad.
Al ejecutar este archivo, verás cómo funcionan *args, **kwargs y el paso de listas como argumentos en Python, con ejemplos claros para cada caso."""