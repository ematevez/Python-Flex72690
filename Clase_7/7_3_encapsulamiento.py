# --- Encapsulamiento en Programación Orientada a Objetos ---
# El encapsulamiento es una técnica que protege los datos internos de una clase,
# ocultando atributos y métodos para evitar accesos no controlados.
# Esto se logra mediante el uso de atributos/métodos privados y protegidos.

# ------------------------------------------------
# Cómo proteger los datos internos de una clase
# ------------------------------------------------
# En Python, usamos convenciones para proteger datos:
# 1. _nombre (guion bajo simple): Indica que el atributo es *protegido*.
#    Aunque se puede acceder, no es recomendable hacerlo desde fuera de la clase.
# 2. __nombre (doble guion bajo): Indica que el atributo es *privado*.
# #    Python aplica "name mangling", renombrando internamente el atributo.

# class Perro:
#     def __init__(self, nombre, raza):
#         self._nombre = nombre  # Atributo protegido
#         self.__raza = raza     # Atributo privado

#     # Método público para obtener el nombre (getter)
#     def obtener_nombre(self):
#         return self._nombre

#     # Método público para obtener la raza (getter)
#     def obtener_raza(self):
#         return self.__raza


# ------------------------------------------------
# # Ejemplo básico: Atributos protegidos y privados
# # ------------------------------------------------
# print("\n--- Atributos protegidos y privados ---")
# perro1 = Perro("Aura", "Caniche")

# # Acceso al atributo protegido (posible, pero no recomendable)
# print(f"Acceso directo al atributo protegido: {perro1._nombre}")  # Output: Aura

# # Acceso al atributo privado (esto generará un error)
# # print(perro1.__raza)  # Descomentar esta línea causará AttributeError

# # Usar un método público para acceder al atributo privado
# print(f"Acceso controlado al atributo privado: {perro1.obtener_raza()}")  # Output: Caniche

# # ------------------------------------------------
# # Métodos privados
# # ------------------------------------------------
# # Los métodos privados también se definen con doble guion bajo (__). 
# # No pueden ser llamados directamente desde fuera de la clase.

# class PerroConLadrido:
#     def __init__(self, nombre, raza):
#         self._nombre = nombre
#         self.__raza = raza

#     # Método privado
#     def __ladrar(self):
#         print(f"{self._nombre} está ladrando.")

#     # Método público que utiliza el método privado
#     def mostrar_ladrar(self):
#         self.__ladrar()


# print("\n--- Métodos privados ---")
# mi_perro = PerroConLadrido("Max", "Beagle")
# # Intentar acceder al método privado directamente generará un error:
# # mi_perro.__ladrar()  # Descomentar esta línea causará AttributeError

# # Usar el método público para invocar el método privado
# mi_perro.mostrar_ladrar()  # Output: Max está ladrando.

# # ------------------------------------------------
# # Encapsulamiento efectivo: Getters y Setters
# # ------------------------------------------------
# # Los getters permiten obtener el valor de un atributo privado.
# # Los setters permiten modificar el valor de un atributo privado.

class PerroEncapsulado:
    def __init__(self, nombre, raza):
        self.__nombre = nombre  # Atributo privado
        self._raza = raza       # Atributo protegido

    # Getter para obtener el nombre
    def obtener_nombre(self):
        return self.__nombre

    # Setter para modificar el nombre
    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    # Método privado
    def __ladrar(self):
        print(f"{self.__nombre} está ladrando.")

    # Método público que usa el método privado
    def mostrar_ladrar(self):
        self.__ladrar()


print("\n--- Getters y Setters ---")
mi_perro = PerroEncapsulado("Firulais", "Labrador")

# Obtener el nombre usando un getter
print(f"Nombre inicial: {mi_perro.obtener_nombre()}")  # Output: Firulais

# Modificar el nombre usando un setter
mi_perro.establecer_nombre("Rex")
print(f"Nombre modificado: {mi_perro.obtener_nombre()}")  # Output: Rex

# Invocar un método privado a través de un método público
mi_perro.mostrar_ladrar()  # Output: Rex está ladrando.

# ------------------------------------------------
# Importancia del Encapsulamiento
# ------------------------------------------------
# El encapsulamiento protege los datos y garantiza que los objetos mantengan
# un estado coherente. Es especialmente útil en proyectos grandes, donde
# controlar el acceso a los datos internos es clave para evitar errores.

# ------------------------------------------------
# Ejemplo adicional: Aplicación del encapsulamiento
# ------------------------------------------------
class Banco:
    def __init__(self, titular, saldo):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo      # Atributo privado

    # Getter para obtener el saldo
    def obtener_saldo(self):
        return self.__saldo

    # Setter para modificar el saldo
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso: {cantidad}")
        else:
            print("Cantidad inválida para depositar.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso: {cantidad}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

print("\n--- Encapsulamiento en una clase Banco ---")
cuenta = Banco("Juan Pérez", 500)

# Ver saldo inicial
print(f"Saldo inicial: {cuenta.obtener_saldo()}")  # Output: 500

# Hacer un depósito
cuenta.depositar(200)  # Output: Depósito exitoso: 200
print(f"Saldo después del depósito: {cuenta.obtener_saldo()}")  # Output: 700

# Intentar retirar una cantidad válida
cuenta.retirar(300)  # Output: Retiro exitoso: 300
print(f"Saldo después del retiro: {cuenta.obtener_saldo()}")  # Output: 400

# Intentar retirar una cantidad inválida
cuenta.retirar(1000)  # Output: Fondos insuficientes o cantidad inválida.
