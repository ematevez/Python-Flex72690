# Introducción a los Operadores Básicos en Python

# Operadores Aritméticos
# Se utilizan para realizar operaciones matemáticas comunes.

# Suma (+)
a = 5
b = 3
# print(f"Suma: {a} + {b} = {a + b}")  # Salida: 8

# Resta (-)
print(f"Resta: {a} - {b} = {a - b}")  # Salida: 2

# Multiplicación (*)
print(f"Multiplicación: {a} * {b} = {a * b}")  # Salida: 15

# División (/)
print(f"División: {a} / {b} = {a / b}")  # Salida: 1.6666666666666667

# División Entera (//)
print(f"División Entera: {a} // {b} = {a // b}")  # Salida: 1

# Módulo (%)
print(f"Módulo: {a} % {b} = {a % b}")  # Salida: 2

# Potencia (**)
print(f"Potencia: {a} ** {b} = {a ** b}")  # Salida: 125


# Operadores Lógicos
# Sirven para realizar combinaciones lógicas.

# AND (and)
x = True
y = False
print(f"AND: {x} and {y} = {x and y}")  # Salida: False

# OR (or)
print(f"OR: {x} or {y} = {x or y}")  # Salida: True

# NOT (not)
print(f"NOT: not {x} = {not x}")  # Salida: False


# Operadores Relacionales
# Comparan valores y devuelven un resultado booleano.

# Igual a (==)
print(f"Igual a: {a} == {b} = {a == b}")  # Salida: False

# Distinto de (!=)
print(f"Distinto de: {a} != {b} = {a != b}")  # Salida: True

# Mayor que (>)
print(f"Mayor que: {a} > {b} = {a > b}")  # Salida: True

# Menor que (<)
print(f"Menor que: {a} < {b} = {a < b}")  # Salida: False

# Mayor o igual que (>=)
print(f"Mayor o igual que: {a} >= {b} = {a >= b}")  # Salida: True

# Menor o igual que (<=)
print(f"Menor o igual que: {a} <= {b} = {a <= b}")  # Salida: False


# Ejemplos prácticos combinados
# Vamos a utilizar estos operadores para resolver problemas sencillos

# Ejemplo 1: Verificar si una persona tiene la edad suficiente para votar.
edad = 15
edad_minima_para_votar = 16
puede_votar = edad >= edad_minima_para_votar
print(f"¿La persona puede votar? {puede_votar}")  # Salida: True

# Ejemplo 2: Calcular el precio final después de aplicar un descuento.
precio_original = 100
descuento = 20  # en porcentaje
precio_final = precio_original - (precio_original * descuento / 100)
print(f"El precio final con un descuento del {descuento}% es: {precio_final}")  # Salida: 80.0

# Ejemplo 3: Combinando operadores lógicos y aritméticos Tabla AND
# Verificar si un número está en un rango específico
numero = 7
limite_inferior = 8
limite_superior = 10
esta_en_rango = numero >= limite_inferior and numero <= limite_superior
print(f"¿El número {numero} está entre {limite_inferior} y {limite_superior}? {esta_en_rango}")  # Salida: True

# Ejemplo 4: Combinando operadores lógicos y aritméticos Tabla OR
# Verificar si un número está en un rango específico
numero = 7
limite_inferior = 8
limite_superior = 10
esta_en_rango = numero >= limite_inferior or numero <= limite_superior
print(f"¿El número {numero} está entre {limite_inferior} y {limite_superior}? {esta_en_rango}")  # Salida: True



# Ejemplo adicional: Validación de contraseña con operadores relacionales y lógicos
password_correcto = "abc123"
password_introducido = "abc123"

# Comprobamos si la contraseña es correcta
es_correcta = password_introducido == password_correcto
print(f"¿La contraseña es correcta? {es_correcta}")  # Salida: True


# Resumen
# Los operadores básicos en Python permiten realizar operaciones matemáticas,
# lógicas y comparativas de manera eficiente. Estos ejemplos muestran cómo
# podemos utilizar operadores para resolver problemas en la vida real.

# ¡Sigue practicando y explorando estos operadores en tus propios programas!

"""
Explicación:
Cada operador tiene su propio ejemplo con la sintaxis correcta.
He añadido ejemplos prácticos adicionales al final, como la validación de un rango numérico, cálculos de descuento, y verificación de contraseñas.
El archivo es didáctico y explica cada paso con comentarios detallados, haciendo más fácil para los estudiantes entender cómo y cuándo usar cada operador.

"""