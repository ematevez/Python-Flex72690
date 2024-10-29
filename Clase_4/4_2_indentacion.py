"""
4.3 Indentación en Python

Python utiliza la **indentación** para definir bloques de código, a diferencia de muchos otros lenguajes de programación 
que emplean llaves `{}`. La indentación en Python es esencial, ya que define la estructura lógica del programa, lo cual 
afecta directamente la forma en que se ejecuta el código. La indentación correcta asegura que las instrucciones estén 
organizadas de manera comprensible y que el código funcione según lo esperado.

### Reglas Fundamentales de Indentación en Python
1. **Consistencia**: Utiliza el mismo número de espacios para cada nivel de indentación dentro de un bloque de código. 
   La convención más común en Python es usar cuatro espacios por cada nivel de indentación.
2. **Espacios vs. Tabuladores**: Es preferible utilizar espacios en lugar de tabuladores para evitar errores. En Python, 
   mezclar espacios y tabuladores puede causar problemas de ejecución difíciles de detectar.
3. **Bloques de Código**: Estructuras de control como `if`, `for`, `while`, así como definiciones de funciones y clases, 
   requieren un aumento en el nivel de indentación para el código contenido dentro de ellas.
"""
### Ejemplos de Indentación Correcta

#Veamos un ejemplo con la estructura `if-else` correctamente indentada:


# x = 15

# if x > 10:
#     print("El número es mayor que 10.")
#     if x > 20:
#         print("El número es mayor que 20.")
# else:
#     print("El número es 10 o menor.")

"""
En este ejemplo:
- El bloque de código dentro del primer `if` está indentado con cuatro espacios.
- El bloque de código dentro del segundo `if` tiene una indentación adicional de cuatro espacios.
- El bloque de código dentro de `else` se alinea al mismo nivel que el primer `if`, lo cual indica que pertenece al 
  mismo nivel lógico.

### Ejemplo Adicional de Estructura con Función

Python también requiere la indentación correcta en definiciones de funciones para agrupar las instrucciones de cada 
bloque funcional.
# """
# def evaluar_numero(x):
#     if x > 10:
#         print("El número es mayor que 10.")
#         if x > 20:
#             print("El número es mayor que 20.")
#     else:
#         print("El número es 10 o menor.")
        
# # Llamada a la función
# evaluar_numero(25)



### Ejemplos de Errores Comunes de Indentación

# 1. **Inconsistencia en la Indentación**: Mezclar espacios y tabuladores, o utilizar un número inconsistente de espacios en el mismo bloque de código, generará un error.

# x = 10

# if x > 5:
#     print("El número es mayor que 5.")
#        print("Esto causará un error.")  # Error: Inconsistencia en la indentación

# 2. **Falta de Indentación**: No aumentar el nivel de indentación después de una estructura de control (como `if`) provocará un error de sintaxis.

# if x > 10:
# print("El número es mayor que 10.")  # Error: Falta de indentación

# 3. **Indentación Excesiva**: Utilizar más espacios de los necesarios no produce un error, pero reduce la legibilidad del código y puede confundir al lector.

# x = 15

# if x > 10:
#         print("El número es mayor que 10.")  # Indentación excesiva, complica la legibilidad
          
### Buenas Prácticas de Indentación
"""
- **Sigue un Estándar Consistente**: La convención recomendada en Python es utilizar cuatro espacios por nivel de 
  indentación.
- **Evita Mezclar Espacios y Tabuladores**: Utiliza espacios de forma consistente en lugar de alternar entre espacios 
  y tabuladores para evitar errores difíciles de depurar.
- **Utiliza un Editor de Texto con Soporte para Python**: La mayoría de los editores modernos como Visual Studio Code, 
  PyCharm y otros pueden configurar automáticamente el uso de cuatro espacios para Python, facilitando la aplicación 
  de estas convenciones.

### Conclusión
La indentación en Python no solo contribuye a la claridad y legibilidad del código, sino que es fundamental para la 
correcta ejecución de los programas. Al seguir las reglas de indentación, puedes evitar errores comunes y asegurar 
que tu código sea fácil de leer y entender. Siguiendo estas prácticas, tu código será más robusto, legible y menos 
propenso a errores de sintaxis.

"""
