# expresiones_anidadas.py

# 3.7 Expresiones Anidadas y Precedencia de Operadores

def main():
    print("=== Expresiones Anidadas y Precedencia de Operadores en Python ===")

    # Reglas de Precedencia de Operadores
    print("\nReglas de Precedencia de Operadores:")

    # 1. Paréntesis
    resultado = (2 + 3) * 4
    print(f"1. (2 + 3) * 4 = {resultado} # Salida: {resultado}")

    # 2. Exponentes
    resultado = 2 * 3 ** 2
    print(f"2. 2 * 3 ** 2 = {resultado} # Salida: {resultado}")

    # 3. Operadores Unarios
    resultado = -3 + 5
    print(f"3. -3 + 5 = {resultado} # Salida: {resultado}")

    # 4. Multiplicación, División, División Entera y Módulo
    resultado = 10 // 3 * 2
    print(f"4. 10 // 3 * 2 = {resultado} # Salida: {resultado}")

    # 5. Suma y Resta
    resultado = 3 + 5 - 2
    print(f"5. 3 + 5 - 2 = {resultado} # Salida: {resultado}")

    # 6. Operadores Relacionales
    resultado = 3 < 5
    print(f"6. 3 < 5 = {resultado} # Salida: {resultado}")

    # 7. Igualdad y Desigualdad
    resultado = 3 == 3
    print(f"7. 3 == 3 = {resultado} # Salida: {resultado}")

    # 8. Operadores Lógicos
    resultado = not (3 > 5 and 2 < 4) or 4 == 4
    print(f"8. not (3 > 5 and 2 < 4) or 4 == 4 = {resultado} # Salida: {resultado}")

    # Evaluación de Expresiones Anidadas
    print("\nEvaluación de Expresiones Anidadas:")
    resultado = 3 + 5 * 2 ** 2 - (4 / 2)
    print(f"Resultado de 3 + 5 * 2 ** 2 - (4 / 2) = {resultado} # Salida: {resultado}")

    # Evitar Errores Comunes
    print("\nEvitar Errores Comunes:")
    
    # Uso de Paréntesis
    resultado = (3 + 5) * (2 - 4 / 2)
    print(f"Uso de paréntesis: (3 + 5) * (2 - 4 / 2) = {resultado} # Salida: {resultado}")

    # Distinguir entre División Entera y Flotante
    a = 7
    b = 3
    print(f"División entera (//): {a // b} # Salida: {a // b}")
    print(f"División flotante (/): {a / b} # Salida: {a / b}")

    # Tema Extra: Importancia de la Lectura de Código
    print("\nTema Extra: Importancia de la Lectura de Código y Comentarios")
    print("Los comentarios son esenciales para entender el propósito del código y su lógica.")
    print("# Ejemplo de comentario en Python:")
    # Este código calcula la suma de dos números
    suma = 2 + 3  # Calcula la suma de 2 y 3
    print(f"Suma de 2 y 3 = {suma} # Salida: {suma}")

if __name__ == "__main__":
    main()


"""
Explicación de Cada Sección
Reglas de Precedencia de Operadores: Muestra ejemplos de cómo se evalúan diferentes operadores.
Evaluación de Expresiones Anidadas: Un ejemplo complejo que muestra la combinación de varios operadores.
Evitar Errores Comunes: Se enfatiza la importancia de usar paréntesis y entender la diferencia entre divisiones.
Tema Extra: Se destaca la importancia de los comentarios en el código para mejorar su legibilidad.
"""