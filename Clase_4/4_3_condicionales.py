# """
# 4.2 Sentencias Condicionales en Python

# Introducción
# =============
# Las sentencias de control condicionales en Python permiten la toma de decisiones dentro de un programa. Con las
# sentencias `if`, `elif` y `else`, podemos evaluar condiciones específicas y ejecutar diferentes bloques de código
# dependiendo de si dichas condiciones son verdaderas o falsas.

# A continuación, exploraremos cada una de estas sentencias con ejemplos prácticos.
# """

# # Estructura de una declaración condicional:
# # ------------------------------------------
# #     if condicion:
# #         # Código a ejecutar si la condición es verdadera
# #     elif otra_condicion:
# #         # Código a ejecutar si la otra condición es verdadera
# # 
# # """

# # Operadores Relacionales y Lógicos
# # =================================
# # Para evaluar condiciones, utilizamos operadores relacionales y lógicos.
# # Los operadores relacionales comparan valores y devuelven un valor booleano (True o False).

# # Ejemplos de operadores relacionales:
# # == : igual a
# # != : diferente de
# # >  : mayor que
# # <  : menor que
# # >= : mayor o igual que
# # <= : menor o igual que

# # Los operadores lógicos permiten combinar condiciones:
# # and : devuelve True si ambas condiciones son verdaderas.
# # or  : devuelve True si al menos una condición es verdadera.
# # not : invierte el valor de una condición.

# # Sentencia If
# # ============
# # La sentencia `if` evalúa una condición y, si se cumple (es decir, si la condición es True), ejecuta un bloque de código.
# # Ejemplo básico de `if`:

# edad = 18

# if edad >= 18:
#     print("Eres mayor de edad.")  # Esto se imprimirá porque la condición es True

# # Ejemplo adicional:
# # Aquí mostramos cómo utilizar `if` con variables de texto.

# nombre = "Alice"

# if nombre == "Alice":
#     print("Hola, Alice!")  # Se imprimirá porque el nombre es igual a "Alice"


# # Sentencia Elif
# # ==============
# # La sentencia `elif` (abreviatura de "else if") se usa después de una sentencia `if` inicial para evaluar
# # múltiples condiciones. Se ejecuta cuando la condición en `if` es falsa, y la condición en `elif` es verdadera.

# temperatura = 40

# if temperatura > 30:
#     print("Hace calor.")
# elif temperatura > 30:
#     print("El clima es agradable.")
# elif temperatura > 10:
#     print("Hace un poco de frío.")
# else:
#     print("Hace mucho frío.")

# # En este ejemplo, se evalúan varias condiciones secuenciales:
# # - Si la temperatura es mayor a 30, imprime "Hace calor".
# # - Si la temperatura es mayor a 20 pero menor o igual a 30, imprime "El clima es agradable".
# # - Si la temperatura es mayor a 10 pero menor o igual a 20, imprime "Hace un poco de frío".
# # - Si ninguna condición se cumple, imprime "Hace mucho frío".


# # Sentencia Else
# # ==============
# # La sentencia `else` se ejecuta si ninguna de las condiciones anteriores (en `if` o `elif`) se cumple.
# # Es útil para cubrir todos los casos restantes.

# edad = 16

# if edad >= 18:
#     print("Eres mayor de edad.")
# else:
#     print("Eres menor de edad.")  # Se ejecuta porque la condición de `if` es False

# # Ejemplo adicional:
# # Otro ejemplo práctico con `else`:

# puntaje = 55

# if puntaje >= 60:
#     print("Aprobaste el examen.")
# else:
#     print("No aprobaste el examen.")  # Se ejecuta porque el puntaje es menor a 60



# Ejemplo con operadores lógicos y relacionales combinados:

# edad = 18
# tiene_licencia = False

# if edad >= 18 and tiene_licencia:
#     print("Puedes conducir.")
# else:
#     print("No puedes conducir.")  # Se ejecuta si al menos una de las condiciones es False

# # Otro ejemplo usando `or` y `not`:

# es_estudiante = False
# es_profesor = False

# if es_estudiante or es_profesor:
#     print("Tienes acceso a la plataforma educativa.")
# else:
#     print("No tienes acceso a la plataforma educativa.")

# # El operador `or` permite que si una de las condiciones es True, se ejecute el bloque de código.
# # Si ambas condiciones fueran False, se ejecutaría el bloque de `else`.


# # Ejemplo Completo de Uso de If, Elif y Else
# # ==========================================
# # Este ejemplo muestra cómo usar `if`, `elif` y `else` para evaluar una calificación.

# calificacion = 85

# if calificacion >= 90:
#     print("Obtuviste una A.")
# elif calificacion >= 80:
#     print("Obtuviste una B.")
# elif calificacion >= 70:
#     print("Obtuviste una C.")
# elif calificacion >= 60:
#     print("Obtuviste una D.")
# else:
#     print("Obtuviste una F.")

# Explicación:
# - Si la calificación es 90 o más, se imprimirá "Obtuviste una A".
# - Si la calificación es 80 o más pero menos de 90, se imprimirá "Obtuviste una B".
# - Si la calificación es 70 o más pero menos de 80, se imprimirá "Obtuviste una C".
# - Si la calificación es 60 o más pero menos de 70, se imprimirá "Obtuviste una D".
# - Si ninguna condición se cumple, se imprimirá "Obtuviste una F".


# Ejemplo Complejo: Sentencias Condicionales Anidadas
# ===================================================
# Las sentencias condicionales pueden anidarse dentro de otras para construir lógica más compleja.

# Ejemplo: Validación de acceso a un sistema
usuario_activo = True
usuario_admin = False

if usuario_activo:
    if usuario_admin:
        print("Bienvenido, administrador.")
    else:
        print("Bienvenido, usuario.")
else:
    print("Cuenta inactiva. Por favor, contacta al soporte.")

# Explicación:
# - Primero, se evalúa si el usuario está activo.
# - Si el usuario está activo, se evalúa si es administrador.
# - Si no es administrador, se muestra un mensaje de bienvenida normal.
# - Si el usuario no está activo, se muestra un mensaje para contactar soporte.


"""
Conclusión
==========
Las sentencias condicionales `if`, `elif` y `else` son esenciales para controlar el flujo de ejecución en Python,
permitiendo que el programa tome decisiones en base a condiciones específicas. El uso de operadores relacionales y lógicos
en combinación con estas sentencias hace posible escribir código más flexible y dinámico, capaz de manejar diferentes
situaciones y casos.
"""
