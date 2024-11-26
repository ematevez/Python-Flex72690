# --- Atributos y Métodos en Clases en Python ---
# En este archivo, explicaremos los conceptos básicos de los atributos y métodos 
# en clases utilizando ejemplos prácticos.

# ------------------------------------------------
# Atributos en Clases
# ------------------------------------------------
# Los atributos son las "propiedades" que describen las características de una clase.
# Se dividen en:
# 1. Atributos de clase: Compartidos por todas las instancias de una clase.
# 2. Atributos de instancia: Propios de cada objeto (instancia) creado a partir de la clase.
#
# ------------------------------------------------
# Métodos en Clases
# ------------------------------------------------
# Los métodos son "funciones" definidas dentro de una clase. Describen los 
# comportamientos que los objetos pueden realizar. Hay tres tipos principales:
# 1. Métodos de instancia: Operan sobre instancias específicas. Siempre reciben `self`.
# 2. Métodos de clase: Trabajan con la clase en sí. Reciben `cls` y se declaran con @classmethod.
# 3. Métodos estáticos: No dependen de la clase ni de las instancias. Se declaran con @staticmethod.

# ------------------------------------------------
# Definición de una clase básica
# ------------------------------------------------
class Perro:
    # Atributo de clase: Compartido por todas las instancias
    especie = "Canis lupus familiaris"  # Es igual para todos los perros

    # Método constructor (__init__): Se ejecuta al crear un objeto
    def __init__(self, nombre, raza):
        # Atributos de instancia: Propios de cada objeto
        self.nombre = nombre  # Nombre del perro (único para cada perro)
        self.raza = raza  # Raza del perro (único para cada perro)

    # Método de instancia: Define el comportamiento de un objeto específico
    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

    # Método de clase: Permite trabajar con atributos de clase
    @classmethod
    def obtener_especie(cls):
        # 'cls' hace referencia a la clase, no a una instancia específica
        return cls.especie

    # Método estático: Función auxiliar que no depende de la clase ni de las instancias
    @staticmethod
    def es_perro_valido(nombre):
        # Verifica si el nombre del perro tiene longitud mayor a 0
        return len(nombre) > 0


# ------------------------------------------------
# Ejemplo práctico: Crear y usar objetos
# ------------------------------------------------
print("\n--- Ejemplo básico con la clase Perro ---")
# Crear un objeto de la clase Perro
mi_perro = Perro("Firulais", "Labrador")

# Usar atributos de instancia
print(f"Nombre: {mi_perro.nombre}, Raza: {mi_perro.raza}")  # Firulais, Labrador

# Usar un método de instancia
mi_perro.ladrar()  # Output: Firulais está ladrando.

# Usar un método de clase
print(f"Especie: {Perro.obtener_especie()}")  # Output: Canis lupus familiaris

# Usar un método estático
print(f"¿Es un nombre válido?: {Perro.es_perro_valido('Firulais')}")  # Output: True

# ------------------------------------------------
# Ejemplo adicional: Múltiples instancias
# ------------------------------------------------
print("\n--- Ejemplo con múltiples instancias ---")
perro_1 = Perro("Max", "Beagle")
perro_2 = Perro("Bella", "Golden Retriever")
perro_3 = Perro("Tito", "Terbal")
# Llamar al método ladrar para cada perro
perro_1.ladrar()  # Max está ladrando.
perro_2.ladrar()  # Bella está ladrando.
perro_3.ladrar() # Tito està ladrando
# ------------------------------------------------
# Cambiar atributos de clase
# ------------------------------------------------
print("\n--- Cambiar atributos de clase ---")
print(f"Especie inicial: {Perro.especie}")  # Canis lupus familiaris
# Modificar el atributo de clase
Perro.especie = "Perro comun"
print(f"Especie modificada: {Perro.especie}")  # Perro comùn

# ------------------------------------------------
# Métodos estáticos: Validación
# ------------------------------------------------
print("\n--- Validación con método estático ---")
print(f"¿'Max' es un nombre válido?: {Perro.es_perro_valido('Max')}")  # True
print(f"¿'' es un nombre válido?: {Perro.es_perro_valido('')}")  # False

# ------------------------------------------------
# Extender la funcionalidad con otra clase: Gato
# ------------------------------------------------
class Gato:
    especie = "Felis catus"  # Atributo de clase

    def __init__(self, nombre, color):
        # Atributos de instancia
        self.nombre = nombre
        self.color = color

    def maullar(self):
        # Método de instancia
        print(f"{self.nombre} dice: ¡Miau!")

    @classmethod
    def obtener_especie(cls):
        # Método de clase
        return cls.especie

    @staticmethod
    def es_gato_valido(nombre):
        # Método estático
        return len(nombre) > 0


# ------------------------------------------------
# Interacción entre clases: Perro y Gato
# ------------------------------------------------
print("\n--- Interacción entre Perro y Gato ---")

mi_gato = Gato("Michi", "Blanco")

mi_gato.maullar()  # Michi dice: ¡Miau!

print(f"Especie del gato: {Gato.obtener_especie()}")  # Felis catus

# Crear una lista de animales y recorrerlos
animales = [mi_perro, perro_1, mi_gato]
for animal in animales:
    # Verificar el tipo de animal
    if isinstance(animal, Perro):
        animal.ladrar()
    elif isinstance(animal, Gato):
        animal.maullar()

# ------------------------------------------------
# Conclusión
# ------------------------------------------------
# Este archivo demuestra cómo:
# 1. Definir atributos y métodos en clases.
# 2. Usar métodos de instancia, clase y estáticos.
# 3. Crear y manejar múltiples objetos.
# 4. Interactuar entre diferentes clases.
