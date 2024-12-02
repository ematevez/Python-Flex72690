"""Unidad 8: Manejo de Archivos y Datos en Python
1. Scripts con Argumentos
Duración: 10 minutos
Objetivo: Aprender a ejecutar scripts que reciben argumentos desde la línea de comandos.

Descripción:
Crea un script Python que acepte argumentos desde la línea de comandos y los utilice para realizar una operación.
"""

import sys

def saludo_personalizado():
    # Verifica si se han pasado argumentos
    if len(sys.argv) > 1:
        nombre = sys.argv[1]
        print(f"Hola, {nombre}! Bienvenido al programa de manejo de archivos.")
    else:
        print("Por favor, proporciona un nombre como argumento.")

if __name__ == "__main__":
    saludo_personalizado()
    
    
