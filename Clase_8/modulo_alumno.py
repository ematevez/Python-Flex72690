"""Objetivo: Aprender a crear un módulo y utilizarlo desde otro archivo Python.

Descripción:
Crea un módulo que contenga una clase Alumno con atributos y métodos, y utilízalo desde otro archivo.
"""

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Alumno: {self.nombre}")
        print(f"Nota: {self.nota}")


class Perro:
    
    def ladro():
        print("Guau")