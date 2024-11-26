# --- Polimorfismo en Python ---
# El polimorfismo es un principio de la Programación Orientada a Objetos (POO) que permite
# que objetos de diferentes clases sean tratados como objetos de una clase común.
# Esto se logra definiendo una interfaz común que es implementada por múltiples clases.

# ------------------------------------------------
# Clase Base (Interfaz Común)
# ------------------------------------------------

# Clase base que define una interfaz común
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del animal

    def hablar(self):
        # Método que debe ser implementado por las subclases
        raise NotImplementedError("Subclase debe implementar este método")


# ------------------------------------------------
# Clases Derivadas (Sobreescritura de Métodos)
# ------------------------------------------------

# Subclase Perro que implementa el método hablar
class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Guau!"


# Subclase Gato que implementa el método hablar
class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Miau!"


# ------------------------------------------------
# Uso del Polimorfismo
# ------------------------------------------------

print("\n--- Polimorfismo: Diferentes Comportamientos con una Interfaz Común ---")

# Crear instancias de Perro y Gato
animales = [Perro("Firulais"), Gato("Misu")]

# Iterar sobre la lista de animales y llamar al método hablar
for animal in animales:
    print(animal.hablar())
# Output:
# Firulais dice: ¡Guau!
# Misu dice: ¡Miau!


# ------------------------------------------------
# Otro Ejemplo Práctico: Polimorfismo en una Función
# ------------------------------------------------

# Función que utiliza polimorfismo
def describir_animal(animal):
    print(f"Interacción con {animal.nombre}: {animal.hablar()}")


print("\n--- Polimorfismo en Funciones ---")
# Usar la función con diferentes tipos de animales
describir_animal(Perro("Rex"))
# Output: Interacción con Rex: Rex dice: ¡Guau!
describir_animal(Gato("Luna"))
# Output: Interacción con Luna: Luna dice: ¡Miau!


# ------------------------------------------------
# Beneficios del Polimorfismo
# ------------------------------------------------

print("\n--- Beneficios del Polimorfismo ---")

# 1. Flexibilidad y Reutilización del Código:
# Se puede usar una misma interfaz para trabajar con múltiples tipos de objetos.
# Esto facilita escribir código genérico.

# Ejemplo:
class Pajaro(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Pío!"

animales.append(Pajaro("Piolín"))  # Agregamos un nuevo tipo de Animal

for animal in animales:
    print(animal.hablar())
# Output:
# Firulais dice: ¡Guau!
# Misu dice: ¡Miau!
# Piolín dice: ¡Pío!


# 2. Mantenimiento Simplificado:
# Al tener una interfaz común, es más fácil extender el comportamiento sin cambiar
# el código existente.

# ------------------------------------------------
# Conclusión
# ------------------------------------------------

# El polimorfismo es una característica poderosa en la POO:
# - Permite que múltiples clases implementen métodos con el mismo nombre pero con
#   comportamientos distintos.
# - Mejora la reutilización del código y la flexibilidad.
# - Facilita la creación de aplicaciones más extensibles y mantenibles.

# ------------------------------------------------
# Principio DRY (Don't Repeat Yourself)
# ------------------------------------------------

# El polimorfismo respalda el principio DRY al evitar la repetición de código.
# En lugar de escribir código específico para cada tipo de objeto, podemos usar
# una interfaz común que maneje diferentes tipos de objetos de manera uniforme.
