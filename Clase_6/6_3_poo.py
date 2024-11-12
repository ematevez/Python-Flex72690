# introduccion_poo.py

# ---------------------------
# Introducción a la Programación Orientada a Objetos (POO)
# ---------------------------

# ¿Qué es la POO?
# La Programación Orientada a Objetos (POO) es un paradigma de programación que organiza el código en torno a "objetos" y "clases", en lugar de centrarse solo en funciones o procedimientos. 
# Este enfoque permite agrupar tanto los datos como las funciones que operan sobre esos datos en unidades llamadas objetos.

# Definición de Clase y Objeto
# En POO, una clase es como un "molde" que define las características y comportamientos que tendrán los objetos creados a partir de ella. 
# Un objeto es una instancia de una clase y contiene datos (atributos) y métodos (funciones) para manipular esos datos.

# Ejemplo simple: Definición de una clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
    def arrancar(self):
        return f"El {self.marca} {self.modelo} ha arrancado."

    def detenerse(self):
        return f"El {self.marca} {self.modelo} se ha detenido."

    def tocar_bocina(self):
        return f"PIPIPIPIP"
# Crear una instancia (objeto) de la clase Vehiculo
# mi_auto = Vehiculo("Toyota", "Corolla", 2022)
# print(mi_auto.arrancar())
# print(mi_auto.detenerse())

primer_auto = Vehiculo("Ford","ka",2000,"Azul")
print(primer_auto)
print(primer_auto.arrancar())
print(primer_auto.tocar_bocina())

segundo_auto = Vehiculo("Fiat","uno", 1990, "Rojo")
print(segundo_auto.detenerse())

# ---------------------------
# Diferencias con la Programación Estructurada
# ---------------------------
# En la programación estructurada, el enfoque está en dividir el código en funciones que realizan acciones sobre datos. 
# En cambio, en POO, tanto los datos como las funciones se agrupan en objetos.

# ---------------------------
# Beneficios de la POO
# ---------------------------
# La POO presenta varias ventajas:
# - Modularidad: El código se organiza en objetos, facilitando su gestión y mantenimiento.
# - Reutilización: Las clases se pueden reutilizar en diferentes aplicaciones.
# - Escalabilidad: Facilita el manejo de proyectos grandes y complejos.
# - Mantenimiento: La estructura en clases y objetos permite localizar y corregir errores de forma eficiente.


# ---------------------------
# Conceptos Fundamentales de la POO
# ---------------------------

# Encapsulación: Permite agrupar datos y métodos en una unidad llamada clase.
# Abstracción: Oculta detalles complejos, permitiendo trabajar con conceptos de alto nivel.
# Herencia: Permite crear nuevas clases basadas en clases existentes.
# Polimorfismo: Permite que un método tenga un comportamiento diferente en distintas clases.

# # Ejemplos de cada concepto

# # 1. Encapsulación
# class Producto:
#     def __init__(self, nombre, precio, stock):
#         self.nombre = nombre
#         self.__precio = precio  # Atributo privado
#         self.__stock = stock    # Atributo privado

#     def get_precio(self):
#         return self.__precio

#     def set_precio(self, nuevo_precio):
#         if nuevo_precio > 0:
#             self.__precio = nuevo_precio

#     def mostrar_info(self):
#         return f"{self.nombre}: ${self.__precio}, Stock: {self.__stock} unidades"

# # Crear un producto y acceder a sus métodos
# producto = Producto("Camiseta", 19.99, 50)
# print(producto.mostrar_info())
# producto.set_precio(17.99)
# print(producto.mostrar_info())

# # 2. Abstracción
# class FormaGeometrica:
#     def area(self):
#         pass

#     def perimetro(self):
#         pass

# class Cuadrado(FormaGeometrica):
#     def __init__(self, lado):
#         self.lado = lado

#     def area(self):
#         return self.lado ** 2

#     def perimetro(self):
#         return 4 * self.lado

# cuadrado = Cuadrado(5)
# print("Área del cuadrado:", cuadrado.area())
# print("Perímetro del cuadrado:", cuadrado.perimetro())

# # 3. Herencia
# class Empleado:
#     def __init__(self, nombre, salario):
#         self.nombre = nombre
#         self.salario = salario

#     def trabajar(self):
#         return f"{self.nombre} está trabajando."

# class Gerente(Empleado):
#     def __init__(self, nombre, salario, departamento):
#         super().__init__(nombre, salario)
#         self.departamento = departamento

#     def trabajar(self):
#         return f"{self.nombre} está supervisando el departamento de {self.departamento}."

# gerente = Gerente("Carlos", 50000, "Ventas")
# print(gerente.trabajar())

# # 4. Polimorfismo
# class Animal:
#     def hacer_sonido(self):
#         pass

# class Perro(Animal):
#     def hacer_sonido(self):
#         return "Guau!"

# class Gato(Animal):
#     def hacer_sonido(self):
#         return "Miau!"

# animales = [Perro(), Gato()]
# for animal in animales:
#     print(animal.hacer_sonido())

# # ---------------------------
# # Ejemplo Práctico Completo
# # ---------------------------

# # Supongamos que desarrollamos una aplicación para una tienda de ropa

# class Cliente:
#     def __init__(self, nombre, email):
#         self.nombre = nombre
#         self.email = email

#     def actualizar_info(self, nuevo_email):
#         self.email = nuevo_email
#         return f"Información actualizada para {self.nombre}"

# class Pedido:
#     def __init__(self, numero_pedido, cliente):
#         self.numero_pedido = numero_pedido
#         self.cliente = cliente
#         self.lista_productos = []

#     def agregar_producto(self, producto):
#         self.lista_productos.append(producto)

#     def calcular_total(self):
#         total = sum([producto.get_precio() for producto in self.lista_productos])
#         return f"Total del pedido {self.numero_pedido}: ${total:.2f}"

# # Crear instancias de las clases
# cliente1 = Cliente("Ana", "ana@example.com")
# pedido1 = Pedido(1, cliente1)

# producto1 = Producto("Vestido", 49.99, 20)
# producto2 = Producto("Sombrero", 15.99, 15)

# # Agregar productos al pedido
# pedido1.agregar_producto(producto1)
# pedido1.agregar_producto(producto2)

# # Calcular total del pedido
# print(pedido1.calcular_total())

# # ---------------------------
# # Bibliografía y Recursos Adicionales
# # ---------------------------
# # Para profundizar en POO y Python:
# 1. "Python Crash Course" de Eric Matthes - Un libro excelente para principiantes.
# 2. Documentación oficial de Python sobre clases y POO: https://docs.python.org/es/3/tutorial/classes.html
# 3. "Automate the Boring Stuff with Python" de Al Sweigart - Ejemplos prácticos y útiles.
# 4. Curso de POO en Python de Real Python: https://realpython.com/

# Ejemplos adicionales y ejercicios pueden encontrarse en: https://www.w3schools.com/python/
