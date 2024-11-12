# errores_y_excepciones.py

"""
Tema: Errores y Excepciones en Python

1. Diferencias entre Errores y Excepciones en Python
2. Importancia de Manejar Excepciones
3. Ejemplos Prácticos de Manejo de Excepciones
4. Tipos de Errores:
   - Errores Sintácticos
   - Errores de Nombre
   - Errores Semánticos
5. Conclusiones y Buenas Prácticas
"""

# ============================================
# 1. Diferencias entre Errores y Excepciones en Python
# ============================================

# **Errores** en Python se detectan antes de la ejecución del programa. 
# Son problemas de sintaxis que el intérprete detecta y que impiden que el programa se ejecute.
# Ejemplo: Olvidar una comilla de cierre
# print("Hola mundo)  # Esto generará un SyntaxError

# **Excepciones** ocurren durante la ejecución del programa y pueden manejarse para que el programa continúe.
# Por ejemplo, intentar dividir por cero produce una excepción que puede manejarse con un bloque try-except.

# Ejemplo de manejo de excepción:
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
# Esto evita que el programa se detenga abruptamente. En lugar de detenerse, se muestra un mensaje de error.


# ============================================
# 2. Importancia de Manejar Excepciones
# ============================================

# La gestión de excepciones es fundamental para crear programas robustos.
# Un programa sin manejo de excepciones se detendrá abruptamente al encontrar un error,
# lo cual puede ser frustrante para los usuarios y, en algunos casos, puede causar pérdida de datos.

# Beneficios del manejo de excepciones:
# - Permite que el programa continúe ejecutándose
# - Ofrece mensajes de error claros y útiles
# - Facilita la depuración y el diagnóstico de problemas

# Ejemplo de uso práctico del manejo de excepciones en un programa de usuario:
try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print(f"El resultado es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Debes introducir un número válido.")
# Este código permite que el usuario reciba mensajes específicos y claros según el tipo de error.


# ============================================
# 3. Ejemplos Prácticos de Manejo de Excepciones
# ============================================

# Ejemplo con múltiples excepciones
try:
    lista = [1, 2, 3]
    valor = lista[5]  # Esto genera un IndexError
except IndexError:
    print("Error: El índice está fuera del rango de la lista.")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")

# Ejemplo de manejo de excepción general
# Es importante evitar el uso excesivo de excepciones genéricas, pero en casos necesarios,
# se puede usar Exception para capturar cualquier error.
try:
    x = int("texto")  # Esto genera un ValueError
except Exception as e:
    print(f"Ocurrió un error: {e}")


# ============================================
# 4. Tipos de Errores
# ============================================

# --------------------------------------------
# a. Errores Sintácticos
# --------------------------------------------
# Los errores sintácticos son detectados por el intérprete antes de que el programa se ejecute.
# Ocurren cuando el código no sigue las reglas de la sintaxis de Python.

# Ejemplo de error sintáctico:
# print("Hola mundo)  # Esto produce un SyntaxError por la falta de la comilla de cierre.

# Prevención de errores sintácticos:
# - Usar un editor de código con resaltado de sintaxis.
# - Revisar que todas las estructuras estén correctamente cerradas.
# - Ejecutar el código frecuentemente para detectar errores temprano.


# --------------------------------------------
# b. Errores de Nombre
# --------------------------------------------
# Los errores de nombre ocurren cuando intentamos usar una variable que no ha sido definida.

# Ejemplo de error de nombre:
# print(variable_inexistente)  # Esto produce un NameError

# Prevención de errores de nombre:
# - Asegurarse de que todas las variables estén definidas antes de su uso.
# - Evitar errores tipográficos y usar nombres de variables consistentes.
# - Usar herramientas como linters para detectar variables no definidas.

# Ejemplo correcto:
nombre = "Python"
print(nombre)  # Ahora se imprimirá correctamente.


# --------------------------------------------
# c. Errores Semánticos
# --------------------------------------------
# Los errores semánticos ocurren cuando la lógica del código es incorrecta.
# Son difíciles de detectar ya que el código se ejecuta sin problemas, pero produce resultados inesperados.

# Ejemplo de error semántico:
a = 5
b = 10
print("La suma es:", a * b)  # El código intenta sumar, pero en su lugar multiplica.

# Prevención de errores semánticos:
# - Escribir pruebas unitarias para verificar el comportamiento del código.
# - Revisar la lógica cuidadosamente.
# - Trabajar en equipo y realizar revisiones de código para detectar errores.

# Ejemplo correcto:
print("La suma es:", a + b)  # Corrige la operación lógica.


# ============================================
# 5. Conclusión y Buenas Prácticas
# ============================================

# - Diferenciar entre errores y excepciones permite a los desarrolladores escribir código más claro y confiable.
# - El manejo adecuado de excepciones es crucial para que los programas no se detengan abruptamente y puedan manejar problemas inesperados.
# - Es importante tener en cuenta las buenas prácticas de programación:
#   * Usar bloques try-except para manejar excepciones conocidas.
#   * Proporcionar mensajes claros y útiles al usuario en caso de error.
#   * Mantener el código limpio y organizado para facilitar la depuración y el mantenimiento.
#   * Escribir pruebas y revisar el código para evitar errores semánticos.

# Fin del archivo: errores_y_excepciones.py
