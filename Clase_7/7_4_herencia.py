# --- Herencia en Python ---
# La herencia es un concepto clave en la Programación Orientada a Objetos (POO).
# Permite que una clase (subclase) herede atributos y métodos de otra clase (superclase).
# Esto promueve la reutilización del código y facilita la creación de jerarquías lógicas.
# DRY
# ------------------------------------------------
# Herencia simple
# ------------------------------------------------

# Clase Padre
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie  # Atributo común para todos los animales
        self.edad = edad        # Edad del animal

    def describeme(self):
        print(f"Soy un {self.especie} y tengo {self.edad} años.")


# Subclase Perro que hereda de Animal
class Perro(Animal):
    def __init__(self, especie, edad, nombre):
        super().__init__(especie, edad)  # Llamar al constructor de la superclase
        self.nombre = nombre            # Atributo específico de Perro

    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau!")

    def moverse(self):
        print(f"{self.nombre} está caminando sobre cuatro patas.")


# Subclase Gato que hereda de Animal
class Gato(Animal):
    def __init__(self, especie, edad, nombre):
        super().__init__(especie, edad)
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice: ¡Miau!")

    def moverse(self):
        print(f"{self.nombre} está caminando sobre cuatro patas.")


print("\n--- Herencia Simple ---")
# Crear instancias de las subclases
mi_perro = Perro("Canis lupus familiaris", 5, "Firulais")
mi_gato = Gato("Felis catus", 3, "Misu")

# Usar métodos heredados y específicos
mi_perro.describeme()  # Output: Soy un Canis lupus familiaris y tengo 5 años.
mi_perro.hablar()      # Output: Firulais dice: ¡Guau!
mi_perro.moverse()     # Output: Firulais está caminando sobre cuatro patas.

mi_gato.describeme()   # Output: Soy un Felis catus y tengo 3 años.
mi_gato.hablar()       # Output: Misu dice: ¡Miau!
mi_gato.moverse()      # Output: Misu está caminando sobre cuatro patas.

# ------------------------------------------------
# Herencia múltiple
# ------------------------------------------------

# Clase Padre 1
class Mamifero(Animal):
    def __init__(self, especie, edad, pelaje_color):
        super().__init__(especie, edad)
        self.pelaje_color = pelaje_color

    def caminar(self):
        print(f"{self.especie} está caminando.")

    def hablar(self):
        print(f"{self.especie} está haciendo un sonido de mamífero.")


# Clase Padre 2
class Volador(Animal):
    def __init__(self, especie, edad, envergadura_alas):
        super().__init__(especie, edad)
        self.envergadura_alas = envergadura_alas

    def volar(self):
        print(f"{self.especie} está volando.")

    def hablar(self):
        print(f"{self.especie} está haciendo un sonido de ave.")


# Clase Hija que hereda de Mamifero y Volador
class Murcielago(Mamifero, Volador):
    def __init__(self, especie, edad, pelaje_color, envergadura_alas):
        Mamifero.__init__(self, especie, edad, pelaje_color)  # Inicializar Mamifero
        Volador.__init__(self, especie, edad, envergadura_alas)  # Inicializar Volador

    def hablar(self):
        print(f"{self.especie} está haciendo un sonido de murciélago.")


print("\n--- Herencia Múltiple ---")
# Crear una instancia de Murciélago
bat = Murcielago("Murciélago", 2, "Negro", "1.5 metros")

# Usar métodos heredados
bat.caminar()  # Output: Murciélago está caminando.
bat.volar()    # Output: Murciélago está volando.

# Resolución de métodos con el mismo nombre
bat.hablar()   # Output: Murciélago está haciendo un sonido de murciélago.

# ------------------------------------------------
# Method Resolution Order (MRO)
# ------------------------------------------------
# El MRO determina el orden en que se buscan métodos en clases con herencia múltiple.
# Python usa el algoritmo C3 Linearization para definir este orden.

print("\n--- Método de Resolución de Orden (MRO) ---")
# Consultar el MRO de la clase Murcielago
print(Murcielago.mro())
# Output: [<class '__main__.Murcielago'>, <class '__main__.Mamifero'>, <class '__main__.Volador'>, <class '__main__.Animal'>, <class 'object'>]

# ------------------------------------------------
# Conclusión
# ------------------------------------------------
# La herencia permite reutilizar y especializar código:
# 1. Reutilización: Subclases heredan atributos y métodos de la superclase.
# 2. Especialización: Subclases pueden sobrescribir métodos de la superclase.
# 3. Organización: Jerarquías claras facilitan el diseño y mantenimiento del código.

