# nombres_funciones.py

"""
Módulo 5.2: Buenas Prácticas en Nombres de Funciones

Este módulo cubre las buenas prácticas para nombrar funciones en Python.
Seguir estas recomendaciones ayuda a mejorar la claridad, consistencia y mantenibilidad del código.
"""

# ========================================================
# Buenas Prácticas en Nombres de Funciones
# ========================================================

# 1. Uso de Minúsculas
# --------------------------------------------------------
# En Python, los nombres de las funciones deben escribirse en minúsculas.
# Esto sigue las convenciones de estilo de la comunidad Python y mejora la legibilidad del código.
# Veamos un ejemplo:

def calcular_area():
    """
    Calcula el área de una figura geométrica.
    """
    pass

# Ejemplo incorrecto:
# def CalcularArea():
# def calcularArea():

# Las dos últimas versiones no son recomendadas en Python. Es preferible utilizar nombres en minúsculas.

# --------------------------------------------------------

# 2. Uso de Guiones Bajos
# --------------------------------------------------------
# Para separar palabras en los nombres de las funciones, se deben usar guiones bajos (_).
# Esto mejora la legibilidad y permite entender rápidamente el propósito de la función.

def obtener_datos_usuario():
    """
    Solicita y devuelve los datos de un usuario.
    """
    pass

# Ejemplo incorrecto:
# def obtenerDatosUsuario():

# La versión sin guiones bajos no sigue la convención de Python, por lo que es menos legible.

# --------------------------------------------------------

# 3. Nombres Autoexplicativos
# --------------------------------------------------------
# Es fundamental utilizar nombres autoexplicativos que describan claramente la tarea de la función.
# Evite usar nombres genéricos, abreviaciones o iniciales que puedan dificultar la comprensión del código.

def calcular_promedio(lista_de_numeros):
    """
    Calcula y devuelve el promedio de una lista de números.
    """
    pass

# Ejemplo incorrecto:
# def cp(l):
# La versión anterior con un nombre abreviado y sin contexto puede ser confusa.
# Es mejor usar nombres descriptivos que indiquen la acción y los datos que maneja la función.

# Ejemplos adicionales de nombres autoexplicativos:
def enviar_mensaje_sms(numero_destino, mensaje):
    """
    Envía un mensaje SMS al número destino especificado.
    """
    pass

def convertir_celsius_a_fahrenheit(temperatura_celsius):
    """
    Convierte una temperatura en grados Celsius a grados Fahrenheit.
    """
    pass

# --------------------------------------------------------

# Ejemplo Completo
# --------------------------------------------------------
# A continuación, se presenta una función que sigue todas las buenas prácticas mencionadas:

def enviar_correo_electronico(destinatario, asunto, mensaje):
    """
    Envía un correo electrónico al destinatario con el asunto y mensaje proporcionados.

    Parámetros:
    destinatario (str): Dirección de correo electrónico del destinatario.
    asunto (str): Asunto del correo electrónico.
    mensaje (str): Cuerpo del mensaje a enviar.

    Retorno:
    None
    """
    pass

# Explicación:
# - El nombre de la función está en minúsculas.
# - Las palabras están separadas por guiones bajos para mejorar la legibilidad.
# - El nombre de la función es autoexplicativo y describe claramente su propósito.

# --------------------------------------------------------

# Conclusión
# --------------------------------------------------------
# Adherirse a estas buenas prácticas al nombrar funciones en Python mejora la claridad y mantenibilidad del código.
# Usar minúsculas, separar palabras con guiones bajos y elegir nombres autoexplicativos facilita la colaboración
# y el mantenimiento del código a largo plazo.

# Referencias:
# - Python Software Foundation. "PEP 8 – Style Guide for Python Code". Disponible en: https://peps.python.org/pep-0008/
# - Effective Python: 59 Specific Ways to Write Better Python, 2nd Edition, Brett Slatkin.

