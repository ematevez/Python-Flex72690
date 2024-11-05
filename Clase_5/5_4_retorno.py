
# ----------------------------------------------
# 1. Introducción a la Sentencia return
# ----------------------------------------------

# En Python, la sentencia `return` se utiliza dentro de una función para devolver un valor al llamador de la función.
# Si no se especifica un valor en `return`, la función devolverá `None` por defecto.

def ejemplo_basico():
    # Esta función no devuelve un valor explícito, por lo que devuelve None
    print("Esta función no tiene return")

resultado = ejemplo_basico()  # Llamada a la función
print(f"Resultado de ejemplo_basico: {resultado}")  # Muestra "Resultado de ejemplo_basico: None"


# ----------------------------------------------
# 2. Uso de la Sentencia return con Valores
# ----------------------------------------------

# La sintaxis básica de `return` es:
#   return valor_a_devolver
# donde `valor_a_devolver` puede ser cualquier tipo de dato: número, cadena, lista, etc.

def saludo_personalizado(nombre):
    mensaje = f"Hola, {nombre}! ¿Cómo estás?"
    return mensaje  # Retorna el mensaje al llamador

# Ejemplo de llamada y uso del valor retornado
resultado = saludo_personalizado("Juan")
print(resultado)  # Imprime: "Hola, Juan! ¿Cómo estás?"


# ----------------------------------------------
# 3. Detalles Importantes sobre el uso de return
# ----------------------------------------------

# Cuando una función alcanza `return`, la ejecución se detiene inmediatamente y ningún código después de `return` se ejecutará.
def ejemplo_terminacion():
    print("Este mensaje se mostrará")
    return 42
    print("Este mensaje NO se mostrará")  # Este print no se ejecutará

resultado = ejemplo_terminacion()
print(f"Resultado de ejemplo_terminacion: {resultado}")


# ----------------------------------------------
# 4. Devolviendo Múltiples Valores
# ----------------------------------------------

# En Python, es posible devolver múltiples valores separados por comas. Esto devuelve una tupla, que es una estructura
# de datos que puede contener varios elementos ordenados.

def obtener_datos():
    nombre = "Juan"
    edad = 30
    return nombre, edad  # Devuelve ambos valores como una tupla

# Al recibir múltiples valores, podemos desempaquetarlos en varias variables.
nombre, edad = obtener_datos()
print(f"Nombre: {nombre}, Edad: {edad}")  # Imprime: "Nombre: Juan, Edad: 30"


# ----------------------------------------------
# 5. Pasando Argumentos a una Función
# ----------------------------------------------

# Las funciones en Python pueden recibir datos a través de parámetros.
# Estos valores, llamados argumentos, se pasan cuando se llama a la función.

def suma(numero1, numero2):
    return numero1 + numero2

# Ejemplo de llamada a la función suma con argumentos
resultado = suma(7, 5)
print(f"Resultado de la suma: {resultado}")  # Imprime: "Resultado de la suma: 12"


# ----------------------------------------------
# 6. Importancia del Orden de los Argumentos
# ----------------------------------------------

# Los argumentos deben pasarse en el mismo orden en que se definen los parámetros de la función.

def resta(a, b):
    return a - b

resultado_1 = resta(10, 5)
print(f"Resta (10 - 5): {resultado_1}")  # Imprime: "Resta (10 - 5): 5"

resultado_2 = resta(5, 10)
print(f"Resta (5 - 10): {resultado_2}")  # Imprime: "Resta (5 - 10): -5"


# ----------------------------------------------
# 7. Ejemplos Prácticos Adicionales
# ----------------------------------------------

# Ejemplo 1: Función que retorna el cuadrado de un número
def cuadrado(numero):
    return numero ** 2

print(f"El cuadrado de 4 es: {cuadrado(4)}")  # Imprime: "El cuadrado de 4 es: 16"


# Ejemplo 2: Función que calcula el promedio de una lista de números
def calcular_promedio(numeros):
    suma_total = sum(numeros)
    cantidad = len(numeros)
    return suma_total / cantidad if cantidad > 0 else 0  # Evita división por cero

print(f"El promedio de [3, 5, 8] es: {calcular_promedio([3, 5, 8])}")  # Imprime: "El promedio de [3, 5, 8] es: 5.333"


# ----------------------------------------------
# 8. Conclusión
# ----------------------------------------------

# La sentencia `return` es fundamental para que las funciones en Python puedan devolver resultados y colaborar
# efectivamente dentro de un programa. Esto permite crear funciones útiles y reutilizables, facilitando la creación
# de programas más complejos y organizados.
# La capacidad de modularizar el código en funciones y retornar valores permite escribir código más limpio, flexible y fácil de mantener.
