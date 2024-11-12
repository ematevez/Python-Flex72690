# clases_y_relaciones.py

"""
Tema: Clases y Relaciones entre Clases en Programación Orientada a Objetos (POO)

Descripción:
Este archivo cubre el tema de las clases y las relaciones entre clases en POO.
Se explica cómo se relacionan las clases en Python mediante ejemplos de Asociación,
Agregación, Composición y Generalización, junto con ejemplos de código.
Incluye referencias a bibliografía para profundizar en el tema.
"""

"""
Asociación: La relación se representa mediante objetos que interactúan pero pueden existir sin depender uno del otro.

Agregación: Una relación en la cual los objetos (Clase y Estudiante) están relacionados de forma "todo/parte" y los objetos pueden existir independientemente.

Composición: Relación fuerte en la que el objeto (Motor) es parte esencial del contenedor (Coche).

Generalización: Se ejemplifica la herencia, donde la subclase (Perro) hereda propiedades de la superclase (Animal).

"""

# Clase Profesor y Clase Curso - Ejemplo de Asociación
class Profesor:
    def __init__(self, nombre, id_profesor):
        self.nombre = nombre
        self.id_profesor = id_profesor
        self.cursos = []

    def enseniar(self, curso):
        self.cursos.append(curso)
        print(f"{self.nombre} está enseñando el curso: {curso.titulo}")


class Curso:
    def __init__(self, titulo, codigo):
        self.titulo = titulo
        self.codigo = codigo

    def agregar(self, profesor):
        print(f"{self.titulo} fue asignado al profesor: {profesor.nombre}")


# Ejemplo de uso
profesor1 = Profesor("Juan Pérez", 1)
curso1 = Curso("Matemáticas", "MAT101")
profesor1.enseniar(curso1)
curso1.agregar(profesor1)

# # ------------------------------------------------------------------------

# Clase Clase y Clase Estudiante - Ejemplo de Agregación
class Clase:
    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula
        self.estudiantes = []  # Los estudiantes pueden existir sin la clase

    def iniciar(self):
        print(f"Clase {self.nombre} en el aula {self.aula} ha comenzado.")

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} se ha añadido a la clase {self.nombre}.")


class Estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula

    def asistir(self):
        print(f"{self.nombre} está asistiendo a la clase.")


# Ejemplo de uso
clase1 = Clase("Ciencias", "Aula 3")
estudiante1 = Estudiante("Ana López", "E123")
clase1.agregar_estudiante(estudiante1)

# ------------------------------------------------------------------------

# Clase Coche y Clase Motor - Ejemplo de Composición
class Coche:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca
        self.motor = Motor("V8", "200 HP")  # El motor es parte integral del coche

    def arrancar(self):
        print(f"El coche {self.modelo} de la marca {self.marca} ha arrancado.")
        self.motor.encender()

    def detener(self):
        print(f"El coche {self.modelo} se ha detenido.")
        self.motor.apagar()


class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def encender(self):
        print(f"El motor {self.tipo} con {self.potencia} está encendido.")

    def apagar(self):
        print(f"El motor {self.tipo} está apagado.")


# Ejemplo de uso
coche1 = Coche("Modelo X", "Tesla")
coche1.arrancar()
coche1.detener()

# ------------------------------------------------------------------------

# Clase Animal y Clase Perro - Ejemplo de Generalización (Herencia)
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")


class Perro(Animal):  # Perro hereda de Animal
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando.")


# Ejemplo de uso
perro1 = Perro("Rex", 5, "Labrador")
perro1.comer()
perro1.ladrar()

# ------------------------------------------------------------------------

# Recursos para profundizar en POO y Diagramas de Clases
"""
Bibliografía y Recursos:
1. "Learning Python" de Mark Lutz - Capítulo 29, para un análisis completo de la OOP.
2. "Python Programming: An Introduction to Computer Science" de John Zelle.
3. Curso online de Programación Orientada a Objetos en Python en plataformas como Udemy, Coursera o edX.
4. Documentación oficial de Python: https://docs.python.org/3/tutorial/classes.html
5. Herramientas para diagramas:
   - Draw.io: https://www.draw.io
   - Microsoft Visio
   - Moqups: https://www.moqups.com
"""

# Nota final sobre los diagramas de clases
"""
Los diagramas de clases son fundamentales para organizar y visualizar la estructura de un sistema en POO.
Representan clases y relaciones como Asociación, Agregación, Composición y Herencia, lo cual facilita la planificación
y desarrollo del código. Herramientas como Draw.io, Visio y Moqups permiten crear diagramas de clases de forma gráfica.
"""

# Guardar el archivo con extensión .py y ejecutarlo para ver los ejemplos en acción.
