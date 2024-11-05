"""
4.7 Función Range en Python

Descripción de la Función range:
La función `range` en Python es una herramienta muy útil para generar secuencias de números enteros. 
Es comúnmente utilizada en bucles `for` para iterar un número específico de veces. La función `range`
acepta hasta tres argumentos: el inicio, el fin y el paso de la secuencia, lo que permite gran flexibilidad 
en la generación de números.

Sintaxis de range:
La función range puede ser utilizada en tres formatos principales:

    range(stop)
    range(start, stop)
    range(start, stop, step)

Parámetros:
    start: El número desde el cual comienza la secuencia. Si no se especifica, el valor predeterminado es 0.
    stop: El número en el que termina la secuencia (no incluido en la secuencia).
    step: La diferencia entre cada par de números consecutivos en la secuencia. Si no se especifica, el valor predeterminado es 1.

A continuación se muestran varios ejemplos de uso de `range` para ilustrar su funcionalidad.
"""

# Ejemplo 1: Usar range con un Solo Argumento
print("Ejemplo 1: range(stop)")
for i in range(5):
    print(i)
# range(5) genera la secuencia [0, 1, 2, 3, 4]. La secuencia comienza en 0 y termina antes de 5.

# Ejemplo 2: Usar range con Dos Argumentos (start y stop)
print("\nEjemplo 2: range(start, stop)")
for i in range(2, 7):
    print(i)
# range(2, 7) genera la secuencia [2, 3, 4, 5, 6]. Comienza en 2 y termina antes de 7.

# Ejemplo 3: Usar range con Tres Argumentos (start, stop, step)
print("\nEjemplo 3: range(start, stop, step)")
for i in range(1, 10, 2):
    print(i)
# range(1, 10, 2) genera [1, 3, 5, 7, 9]. Comienza en 1, termina antes de 10, y avanza en pasos de 2.

# Ejemplo 4: Usar range con Paso Negativo
print("\nEjemplo 4: range con paso negativo")
for i in range(10, 0, -1):
    print(i)
# range(10, 0, -1) genera [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]. Comienza en 10, termina antes de 0 y avanza en pasos de -1.

# Ejemplo 5: Usar range para recorrer una lista por índice
print("\nEjemplo 5: Usar range para recorrer una lista por índice")
mi_lista = ['a', 'b', 'c', 'd']
for i in range(len(mi_lista)):
    print(f"Índice {i}: Valor '{mi_lista[i]}'")
# Utilizando range(len(mi_lista)) para iterar sobre los índices de la lista.

# Ejemplo 6: Usar range para generar una secuencia de números pares
print("\nEjemplo 6: Generar una secuencia de números pares")
for i in range(0, 11, 2):
    print(i)
# Genera la secuencia [0, 2, 4, 6, 8, 10]. Comienza en 0, termina antes de 11, avanza en pasos de 2.

# Ejemplo 7: Usar range para generar una secuencia de números impares
print("\nEjemplo 7: Generar una secuencia de números impares")
for i in range(1, 10, 2):
    print(i)
# Genera la secuencia [1, 3, 5, 7, 9]. Comienza en 1, termina antes de 10, avanza en pasos de 2.

# Ejemplo 8: Usar range con valores grandes y saltos grandes
print("\nEjemplo 8: Usar range con valores y saltos grandes")
for i in range(100, 0, -10):
    print(i)
# Genera [100, 90, 80, ..., 10]. Comienza en 100, termina antes de 0, avanza en pasos de -10.

# Conclusión
print("\nConclusión:")
print("La función range es extremadamente útil para generar secuencias de números en Python,")
print("especialmente en combinación con bucles for. Su capacidad para aceptar diferentes parámetros")
print("(inicio, fin y paso) proporciona una gran flexibilidad y control sobre las secuencias generadas.")
print("Con un buen dominio de range, se pueden escribir bucles más eficientes y gestionar iteraciones de manera efectiva.")
