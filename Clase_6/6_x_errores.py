# errores_y_excepciones.py

"""
Este archivo contiene ejemplos de los errores y excepciones más comunes en Python,
junto con una explicación y un ejemplo que muestra cómo ocurre cada uno.
"""

# ---------------------------------------
# 1. ZeroDivisionError
# ---------------------------------------
# Ocurre cuando se intenta dividir un número entre cero.

try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
    # Salida: ZeroDivisionError: division by zero

# ---------------------------------------
# 2. IndexError
# ---------------------------------------
# Ocurre cuando se intenta acceder a un índice inexistente en una lista o secuencia.

try:
    lista = [1, 2, 3]
    print(lista[5])
except IndexError as e:
    print("IndexError:", e)
    # Salida: IndexError: list index out of range

# ---------------------------------------
# 3. KeyError
# ---------------------------------------
# Ocurre cuando se intenta acceder a una clave inexistente en un diccionario.

try:
    diccionario = {"nombre": "Alice", "edad": 25}
    print(diccionario["direccion"])
except KeyError as e:
    print("KeyError:", e)
    # Salida: KeyError: 'direccion'

# ---------------------------------------
# 4. TypeError
# ---------------------------------------
# Ocurre cuando se utiliza un tipo de dato inapropiado en una operación.

try:
    resultado = "10" + 5
except TypeError as e:
    print("TypeError:", e)
    # Salida: TypeError: can only concatenate str (not "int") to str

# ---------------------------------------
# 5. ValueError
# ---------------------------------------
# Ocurre cuando una función recibe un argumento con el tipo correcto pero un valor inapropiado.

try:
    numero = int("diez")
except ValueError as e:
    print("ValueError:", e)
    # Salida: ValueError: invalid literal for int() with base 10: 'diez'

# ---------------------------------------
# 6. AttributeError
# ---------------------------------------
# Ocurre cuando se intenta acceder a un atributo o método que no existe en un objeto.

try:
    texto = "Hola, mundo"
    texto.append("!")
except AttributeError as e:
    print("AttributeError:", e)
    # Salida: AttributeError: 'str' object has no attribute 'append'

# ---------------------------------------
# 7. ImportError / ModuleNotFoundError
# ---------------------------------------
# ImportError ocurre cuando no se puede importar un módulo.
# ModuleNotFoundError es una subclase de ImportError para módulos no encontrados.

try:
    import modulo_inexistente
except ModuleNotFoundError as e:
    print("ModuleNotFoundError:", e)
    # Salida: ModuleNotFoundError: No module named 'modulo_inexistente'

# ---------------------------------------
# 8. FileNotFoundError
# ---------------------------------------
# Ocurre cuando se intenta abrir un archivo que no existe.

try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError as e:
    print("FileNotFoundError:", e)
    # Salida: FileNotFoundError: [Errno 2] No such file or directory: 'archivo_inexistente.txt'

# ---------------------------------------
# 9. IOError
# ---------------------------------------
# Ocurre cuando ocurre un error de entrada/salida, como al intentar leer un archivo sin permisos.

try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except IOError as e:
    print("IOError:", e)
    # Nota: FileNotFoundError es una subclase de IOError en Python 3

# ---------------------------------------
# 10. StopIteration
# ---------------------------------------
# Ocurre cuando una función de iteración no tiene más elementos para devolver.

try:
    iterador = iter([1, 2, 3])
    while True:
        print(next(iterador))
except StopIteration as e:
    print("StopIteration:", e)
    # Salida: 1 2 3 StopIteration

# ---------------------------------------
# 11. RuntimeError
# ---------------------------------------
# Ocurre cuando se detecta un error no específico en tiempo de ejecución.

try:
    def recursiva():
        return recursiva()
    recursiva()
except RecursionError as e:
    print("RecursionError:", e)
    # Salida: RecursionError: maximum recursion depth exceeded in comparison

# ---------------------------------------
# 12. NameError
# ---------------------------------------
# Ocurre cuando se intenta acceder a una variable que no está definida.

try:
    print(variable_inexistente)
except NameError as e:
    print("NameError:", e)
    # Salida: NameError: name 'variable_inexistente' is not defined

# ---------------------------------------
# 13. MemoryError
# ---------------------------------------
# Ocurre cuando el sistema no puede asignar suficiente memoria para una operación.

try:
    lista_grande = [1] * (10**10)
except MemoryError as e:
    print("MemoryError:", e)
    # Puede ocurrir en sistemas con poca memoria

# ---------------------------------------
# 14. AssertionError
# ---------------------------------------
# Ocurre cuando una declaración assert falla.

try:
    assert 2 + 2 == 5, "La aritmética está fallando"
except AssertionError as e:
    print("AssertionError:", e)
    # Salida: AssertionError: La aritmética está fallando

# ---------------------------------------
# 15. SyntaxError
# ---------------------------------------
# Ocurre cuando el código contiene un error de sintaxis.

# Este error no se puede capturar en tiempo de ejecución; lo detectará el intérprete antes de ejecutar el código.
# Ejemplo:
# try:
#     eval("if True print('Hola')")
# except SyntaxError as e:
#     print("SyntaxError:", e)

# ---------------------------------------
# 16. IndentationError
# ---------------------------------------
# Ocurre cuando la indentación del código es incorrecta.

# try:
#     eval("def funcion():\nprint('Hola')")
# except IndentationError as e:
#     print("IndentationError:", e)

# Nota: SyntaxError e IndentationError son errores de compilación, no pueden atraparse en bloques try-except en tiempo de ejecución.

# ---------------------------------------
# Bibliografía:
# ---------------------------------------

"""
1. Python Software Foundation. (2024). "Built-in Exceptions". Python documentation.
   https://docs.python.org/3/library/exceptions.html

2. Sweigart, A. (2019). "Automate the Boring Stuff with Python". No Starch Press.

3. Lutz, M. (2013). "Learning Python". O'Reilly Media.

4. Ceder, N. (2010). "The Quick Python Book". Manning Publications.
"""

print("Fin del archivo: errores_y_excepciones.py")
