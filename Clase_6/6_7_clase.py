# Unidad 6: Excepciones y Programación Orientada a Objetos en Python

"""
Esta unidad se centra en el manejo de excepciones y los principios básicos de la Programación Orientada a Objetos en Python.
Incluye actividades prácticas para fortalecer la comprensión de estos conceptos.
"""

# ---------------------------------------
# Actividad: Desafío de errores
# ---------------------------------------

def dividir(a, b):
    """
    Divide el número `a` entre el número `b`.
    Si `b` es cero, devuelve None para evitar un error de división por cero.
    
    Parámetros:
    a (float): el dividendo.
    b (float): el divisor.
    
    Retorna:
    float: el resultado de la división o None si `b` es cero.
    """
    if b == 0:
        return None
    return a / b

# Ejemplo de uso:
resultado = dividir(10, 2)
print(f"Resultado de dividir 10 entre 2: {resultado}")

resultado = dividir(10, 0)
print(f"Resultado de dividir 10 entre 0: {resultado}")
# Al dividir entre 0, se retorna None

# ---------------------------------------
# Actividad: Desafío de excepciones
# ---------------------------------------

def dividir_con_excepcion(a, b):
    """
    Divide el número `a` entre el número `b` y maneja la excepción de división por cero.
    Si `b` es cero, se captura la excepción y se muestra un mensaje específico.
    
    Parámetros:
    a (float): el dividendo.
    b (float): el divisor.
    
    Retorna:
    float: el resultado de la división.
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir entre cero")

# Ejemplo de uso:
dividir_con_excepcion(10, 0)  # Mostrará el mensaje: No se puede dividir entre cero

# ---------------------------------------
# Para pensar: ¿Qué son los diagramas de clases?
# ---------------------------------------

"""
Los diagramas de clases son representaciones visuales de la estructura y las relaciones entre clases en un programa orientado a objetos.
Se utilizan para diseñar sistemas, visualizar las conexiones entre diferentes partes de un programa y facilitar la comprensión de cómo interactúan los objetos.

Herramienta sugerida: DrawIO
"""

# ---------------------------------------
# Actividad: Diagrama de clases
# ---------------------------------------

"""
Representación del siguiente escenario en un diagrama de clases:
1. La clase `Persona` actúa como clase base.
2. `Empleado` y `Cliente` heredan de `Persona`.
3. `Empleado` tiene un atributo de `sueldo_bruto`.
4. `Directivo` (una subclase de `Empleado`) tiene una `categoría` y subordinados.
5. `Cliente` añade un `telefono_de_contacto`.

El diagrama de clases se puede realizar en DrawIO y reflejar las relaciones de herencia.
"""

# ---------------------------------------
# Ejemplo en Python: Programación Orientada a Objetos
# ---------------------------------------

class Persona:
    """
    Clase base para representar a una persona.
    
    Atributos:
    nombre (str): El nombre de la persona.
    edad (int): La edad de la persona.
    """
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Empleado(Persona):
    """
    Clase para representar a un empleado, derivada de Persona.
    
    Atributos adicionales:
    sueldo_bruto (float): El sueldo bruto del empleado.
    """
    
    def __init__(self, nombre, edad, sueldo_bruto):
        super().__init__(nombre, edad)
        self.sueldo_bruto = sueldo_bruto

class Directivo(Empleado):
    """
    Clase para representar a un directivo, derivada de Empleado.
    
    Atributos adicionales:
    categoria (str): Categoría del directivo.
    subordinados (list): Lista de empleados subordinados.
    """
    
    def __init__(self, nombre, edad, sueldo_bruto, categoria):
        super().__init__(nombre, edad, sueldo_bruto)
        self.categoria = categoria
        self.subordinados = []

    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)

class Cliente(Persona):
    """
    Clase para representar a un cliente, derivada de Persona.
    
    Atributos adicionales:
    telefono_de_contacto (str): Teléfono de contacto del cliente.
    """
    
    def __init__(self, nombre, edad, telefono_de_contacto):
        super().__init__(nombre, edad)
        self.telefono_de_contacto = telefono_de_contacto

# Ejemplo de uso:

# Crear objetos de cada clase
empleado = Empleado("Ana", 30, 35000)
directivo = Directivo("Carlos", 45, 50000, "Gerente")
cliente = Cliente("Luis", 28, "123-456-789")

# Agregar subordinado
directivo.agregar_subordinado(empleado)

# Imprimir detalles
print(f"Empleado: {empleado.nombre}, Edad: {empleado.edad}, Sueldo: {empleado.sueldo_bruto}")
print(f"Directivo: {directivo.nombre}, Edad: {directivo.edad}, Categoría: {directivo.categoria}")
print(f"Cliente: {cliente.nombre}, Edad: {cliente.edad}, Teléfono: {cliente.telefono_de_contacto}")

# ---------------------------------------
# Bibliografía y recursos adicionales
# ---------------------------------------

"""
1. Python Software Foundation. (2024). *The Python Standard Library - Exceptions*. 
   https://docs.python.org/3/library/exceptions.html
   
2. Sweigart, A. (2019). *Automate the Boring Stuff with Python*. No Starch Press.
   
3. Lutz, M. (2013). *Learning Python*. O'Reilly Media.

4. Martínez, R. (2023). *Introducción a la Programación Orientada a Objetos en Python*. Ediciones académicas.
"""

# ---------------------------------------
# Cierre y preguntas
# ---------------------------------------

"""
Resumen:
- Hemos aprendido a manejar errores mediante excepciones en Python.
- Introducimos los fundamentos de la Programación Orientada a Objetos.
- Diseñamos un pequeño sistema orientado a objetos para gestionar empleados y clientes en una empresa.

Preguntas:
1. ¿Qué tipo de excepción utilizarías para gestionar errores de tipo en Python?
2. ¿Cómo puedes mejorar la legibilidad de un diagrama de clases?

"""
