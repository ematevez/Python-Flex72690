# variables_alcance.py
# ===============================
# Variables Locales
# ===============================

# Las variables locales son aquellas que se definen dentro de una función.
# Solo se pueden acceder dentro de la función en la que fueron creadas.
# Ejemplo de variable local:
def ejemplo_local():
    variable_local = 10  # Definida dentro de la función, es local a esta
    print("Dentro de la función:", variable_local)

ejemplo_local()

# Intentar acceder a una variable local fuera de su función
# print(variable_local)  # Esto causará un error NameError


# ===============================
# Variables Globales
# ===============================

variable_global = 20  # Definida en el ámbito global

def ejemplo_global():
    print("Accediendo a variable global dentro de la función:", variable_global)

ejemplo_global()
print("Accediendo a variable global fuera de la función:", variable_global)

# Comentario:
# La variable `variable_global` está disponible tanto dentro como fuera de la función `ejemplo_global`.


# ===============================
# Uso de Variables Globales y Locales en Funciones
# ===============================

variable_global_modificable = 50

def modificar_global():
    global variable_global_modificable  # Declaramos que usaremos la variable global
    variable_global_modificable = 30  # Modificamos el valor de la variable global

modificar_global()
print("Después de modificar la variable global:", variable_global_modificable)  # Imprimirá 30

# Sin la palabra clave `global`, se crearía una nueva variable local con el mismo nombre,
# y la variable global original no se vería afectada.
# Ejemplo sin modificar la variable global:

variable_global_no_modificada = 40

def intentar_modificar_global():
    variable_global_no_modificada = 100  # Esto crea una nueva variable local
    print("Dentro de la función:", variable_global_no_modificada)  # Imprimirá 100

intentar_modificar_global()
print("Fuera de la función:", variable_global_no_modificada)  # Imprimirá 40

# Comentario:
# En este caso, `variable_global_no_modificada` dentro de la función es local y no afecta la
# variable global con el mismo nombre fuera de la función.


# ===============================
# Buenas Prácticas al Usar Variables Globales y Locales
# ===============================

# Generalmente, se recomienda evitar el uso excesivo de variables globales, ya que pueden
# dificultar la comprensión del código y crear efectos secundarios inesperados.

# Ejemplo de mal uso de variables globales
contador_global = 0

def incrementar_contador():
    global contador_global
    contador_global += 1
    print("Contador global dentro de la función:", contador_global)

incrementar_contador()
incrementar_contador()
print("Contador global fuera de la función:", contador_global)

# En lugar de modificar variables globales directamente dentro de funciones, 
# una mejor práctica es pasar variables como argumentos y devolver resultados.

def incrementar_contador_buena_practica(contador):
    contador += 1
    print("Contador local dentro de la función:", contador)
    return contador

contador = 0
contador = incrementar_contador_buena_practica(contador)
contador = incrementar_contador_buena_practica(contador)
print("Contador fuera de la función:", contador)


# ===============================
# Conclusión
# ===============================
# args_kwargs_examples.py

# Ejemplo de uso de *args (argumentos variables) en Python

def sumar(*args):
    """
    Suma todos los números que se pasen como argumentos.
    *args permite pasar una cantidad variable de argumentos a la función.
    """
    total = 0
    for numero in args:
        total += numero
    return total

print("Ejemplos con *args:")
print(sumar(1, 2, 3))         # 6
print(sumar(4, 5))            # 9
print(sumar(10, 20, 30, 40))  # 100


# Pasar una lista usando * para desempaquetarla en argumentos individuales
numeros = [1, 2, 3, 4]
print("Sumar lista desempaquetada:", sumar(*numeros))  # 10


# Ejemplo de uso de **kwargs (argumentos con nombre) en Python

def info_persona(**kwargs):
    """
    Imprime la información de una persona.
    **kwargs permite pasar una cantidad variable de argumentos nombrados.
    """
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

print("\nEjemplos con **kwargs:")
info_persona(nombre="Alice", edad=30, ciudad="Madrid")
# Salida:
# nombre: Alice
# edad: 30
# ciudad: Madrid

info_persona(nombre="Bob", ocupacion="Ingeniero")
# Salida:
# nombre: Bob
# ocupacion: Ingeniero


# Pasar un diccionario usando ** para desempaquetarlo en argumentos nombrados
datos = {'nombre': 'Carlos', 'edad': 28, 'ciudad': 'Bogotá'}
print("\nInfo de persona desde diccionario desempaquetado:")
info_persona(**datos)
# Salida:
# nombre: Carlos
# edad: 28
# ciudad: Bogotá


# Ejemplo de paso de listas como argumentos en Python

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    La lista se pasa como un único argumento.
    """
    total = sum(numeros)
    promedio = total / len(numeros)
    return promedio

print("\nEjemplo de paso de listas como argumento:")
mi_lista = [10, 20, 30, 40]
print("Promedio de la lista:", calcular_promedio(mi_lista))  # 25.0


# Resumen de uso de *args, **kwargs y listas como argumentos

def ejemplo_completo(*args, **kwargs):
    """
    Ejemplo combinado de *args y **kwargs.
    Imprime todos los argumentos posicionales y nombrados.
    """
    print("\nArgumentos posicionales (*args):")
    for arg in args:
        print(arg)
    
    print("\nArgumentos nombrados (**kwargs):")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# Llamada a la función con combinación de *args y **kwargs
print("\nEjemplo combinado de *args y **kwargs:")
ejemplo_completo(1, 2, 3, nombre="Diana", edad=32, ciudad="Lima")
# Salida:
# Argumentos posicionales (*args):
# 1
# 2
# 3
#
# Argumentos nombrados (**kwargs):
# nombre: Diana
# edad: 32
# ciudad: Lima

"""Explicación
sumar(*args): muestra cómo usar *args para aceptar múltiples argumentos posicionales.
info_persona(**kwargs): ilustra cómo usar **kwargs para recibir múltiples argumentos nombrados.
calcular_promedio(numeros): usa una lista como argumento, mostrándose como un único parámetro.
ejemplo_completo(*args, **kwargs): combina ambos (*args y **kwargs) en una sola función para demostrar su versatilidad.
Al ejecutar este archivo, verás cómo funcionan *args, **kwargs y el paso de listas como argumentos en Python, con ejemplos claros para cada caso."""