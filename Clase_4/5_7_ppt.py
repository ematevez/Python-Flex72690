# Actividad 1: Saludo a una ciudad

def saludo_ciudad(ciudad):
    """
    Muestra un saludo personalizado para una ciudad.

    Parámetros:
        ciudad (str): Nombre de la ciudad.

    Ejemplo:
        - saludo_ciudad("Buenos Aires") -> "¡Hola, bienvenidx a Buenos Aires!"
    """
    print(f"¡Hola, bienvenidx a {ciudad}!")

# Prueba de la función saludo_ciudad
saludo_ciudad("Buenos Aires")


# Actividad 2: Calcular la media de una lista de números

def calcular_media(numeros):
    """
    Calcula la media de una lista de números.

    Parámetros:
        numeros (list): Lista de números (int o float).

    Retorna:
        float: La media de los números.

    Ejemplo:
        - calcular_media([10, 20, 30]) -> 20.0
    """
    if not numeros:  # Verifica si la lista está vacía
        return 0
    
    suma = sum(numeros)  # Suma todos los números en la lista
    media = suma / len(numeros)  # Calcula la media
    return media

# Prueba de la función calcular_media
print(f"La media de [10, 20, 30] es: {calcular_media([10, 20, 30])}")


# Actividad 3: Verificar si un número es múltiplo de otro

def es_multiplo(num1, num2):
    """
    Verifica si uno de los dos números es múltiplo del otro.

    Parámetros:
        num1 (int): Primer número.
        num2 (int): Segundo número.

    Retorna:
        str: Mensaje indicando si uno es múltiplo del otro.

    Ejemplo:
        - es_multiplo(10, 5) -> "10 es múltiplo de 5."
        - es_multiplo(7, 3) -> "Ninguno de los números es múltiplo del otro."
    """
    if num2 == 0:  # Evitar división por cero
        return "No se puede dividir por cero."
    
    if num1 % num2 == 0:
        return f"{num1} es múltiplo de {num2}."
    elif num2 % num1 == 0:
        return f"{num2} es múltiplo de {num1}."
    else:
        return "Ninguno de los números es múltiplo del otro."

# Prueba de la función es_multiplo
print(es_multiplo(10, 5))
print(es_multiplo(7, 3))


# Actividad 4: Conversión entre milímetros y metros

def convertir_medida(*args):
    """
    Convierte entre milímetros y metros, dependiendo de los argumentos recibidos.

    Parámetros:
        args: Puede ser uno o tres argumentos.

    Si recibe un argumento, se considera como milímetros y se convierte a metros, centímetros y milímetros.
    Si recibe tres argumentos, se considera como metros, centímetros y milímetros y se convierte a milímetros.

    Ejemplo:
        - convertir_medida(1500) -> (1.5, 0.0, 0.0)
        - convertir_medida(1, 50, 0) -> 1050
    """
    if len(args) == 1:
        milimetros = args[0]
        metros = milimetros / 1000  # Convertir a metros
        centimetros = (milimetros % 1000) / 10  # Obtener centímetros
        return metros, centimetros, milimetros % 10  # Devolver metros, centímetros y milímetros

    elif len(args) == 3:
        metros, centimetros, milimetros = args
        total_milimetros = (metros * 1000) + (centimetros * 10) + milimetros  # Convertir todo a milímetros
        return total_milimetros

    else:
        return "Por favor, ingrese uno o tres argumentos."

# Pruebas de la función convertir_medida
print(convertir_medida(1500))  # 1500 mm a metros
print(convertir_medida(1, 50, 0))  # 1 m, 50 cm, 0 mm a milímetros

"""Explicaciones de cada actividad:
Saludo a una ciudad:

La función saludo_ciudad() toma como argumento el nombre de una ciudad y muestra un saludo personalizado.
Utiliza una simple interpolación de cadenas para crear el mensaje.
Calcular la media:

La función calcular_media() recibe una lista de números y calcula su media.
Verifica si la lista está vacía para evitar errores y utiliza la función sum() y len() para realizar los cálculos.
Verificar múltiplos:

La función es_multiplo() verifica si uno de los números es múltiplo del otro, evitando la división por cero.
Retorna un mensaje apropiado basado en la comparación.
Conversión de medidas:

La función convertir_medida() puede aceptar uno o tres argumentos y realiza conversiones entre milímetros y metros.
Si recibe un solo argumento, asume que es en milímetros y convierte a metros y centímetros. Si recibe tres, convierte esas medidas a milímetros.
Cada función incluye ejemplos de uso para demostrar su funcionalidad. Puedes ejecutar este script en cualquier entorno de Python para probar su funcionamiento."""