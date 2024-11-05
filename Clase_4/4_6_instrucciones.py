"""
4.5 Instrucciones Break, Continue y Pass

Este archivo contiene una explicación detallada y ejemplos de las instrucciones break, continue y pass en Python. 
Estas instrucciones permiten controlar el flujo de los bucles, lo que resulta útil para manejar condiciones especiales 
durante la iteración y mejorar la legibilidad y funcionalidad del código.
"""

# Introducción
# print("=== Introducción a las Instrucciones break, continue y pass ===\n")
# print("En Python, las instrucciones 'break', 'continue' y 'pass' se utilizan para controlar el flujo de los bucles.")
# print("Con ellas, es posible gestionar condiciones específicas sin alterar completamente la lógica del bucle.")

# # Instrucción break
# print("\n--- Instrucción break ---\n")
# print("La instrucción 'break' se utiliza para salir de un bucle de manera inmediata.")
# print("Independientemente de si la condición del bucle se ha cumplido o no, cuando se ejecuta 'break',")
# print("el control del programa se transfiere a la primera línea de código después del bucle.")

# Ejemplo básico de break
# print("\nEjemplo de uso básico de 'break':")
# for i in range(10):
#     if i == 5:
#         break
#     print(i)  # Este código imprimirá los números hasta el 4 y luego se detendrá.

# Ejemplo práctico con 'break' para buscar un número
# print("\nEjemplo práctico de 'break' para buscar un número en un rango:")
# encontrado = False
# for numero in range(1, 11):
#     if numero == 7:
#         encontrado = True
#         break
# print(f"Número 7 {'encontrado' if encontrado else 'no encontrado'}")

# Instrucción continue
print("\n--- Instrucción continue ---\n")
print("La instrucción 'continue' permite omitir el resto del código en la iteración actual y pasar a la siguiente iteración.")
print("Esto es útil para evitar ciertas condiciones dentro del bucle sin detener la ejecución completa del mismo.")

# Ejemplo básico de continue
# print("\nEjemplo de uso básico de 'continue':")
# for i in range(10):
#     if i % 2 == 0:
#         continue  # Omite el resto de la iteración si i es par
#     print(i)  # Este código imprimirá solo números impares.

# # Ejemplo práctico con 'continue' para imprimir solo números impares
# print("\nEjemplo práctico de 'continue' para imprimir números impares:")
# for numero in range(1, 11):
#     if numero % 2 == 0:
#         continue
#     print(numero)  # Solo imprimirá los números impares dentro del rango.

# Instrucción pass
# print("\n--- Instrucción pass ---\n")
# print("La instrucción 'pass' se utiliza como un marcador de posición.")
# print("Es útil en situaciones donde una declaración es necesaria por razones sintácticas, pero no requiere acción.")
# print("'pass' no afecta el flujo del bucle; simplemente indica que no se debe realizar ninguna operación en ese punto.")

# # Ejemplo básico de pass
# print("\nEjemplo de uso básico de 'pass':")
# for i in range(10):
#     if i < 5:
#         pass  # No realiza ninguna acción si i es menor que 5
#     else:
#         print(i)  # Este código imprimirá los números del 5 al 9.

# # Ejemplo práctico: Uso de pass como marcador de posición en el desarrollo
# print("\nEjemplo práctico de 'pass' como marcador de posición:")
# for i in range(10):
#     if i < 5:
#         pass  # Aquí podríamos añadir lógica específica en el futuro
#     else:
#         print(f"Procesando número {i}")  # Solo imprime números mayores o iguales a 5

# Ejemplo de Break y Continue en conjunto
# print("\n--- Ejemplo de 'break' y 'continue' combinados ---\n")
# print("A veces, es posible combinar 'break' y 'continue' para manejar múltiples condiciones dentro de un bucle.")

# # Ejemplo con break y continue juntos
# print("\nEjemplo: Encontrar el primer número impar en un rango, pero saltarse el 3:")
# for numero in range(1, 10):
#     if numero == 3:
#         continue  # Salta el número 3
#     if numero % 2 != 0:
#         print(f"Primer número impar (excluyendo el 3): {numero}")
#         break  # Detiene el bucle en el primer número impar

# # Conclusión
# print("\n=== Conclusión ===\n")
# print("Las instrucciones 'break', 'continue' y 'pass' proporcionan un control más fino sobre el flujo de los bucles en Python.")
# print("- 'break' permite salir de un bucle prematuramente.")
# print("- 'continue' omite el resto de la iteración actual y pasa a la siguiente.")
# print("- 'pass' actúa como un marcador de posición sin realizar ninguna acción.")
# print("El uso adecuado de estas instrucciones puede mejorar la legibilidad y funcionalidad del código.")
