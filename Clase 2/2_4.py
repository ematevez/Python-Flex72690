# Diccionarios en Python

# ¿Qué son los Diccionarios?
# Los diccionarios son estructuras de datos que permiten almacenar colecciones de pares clave-valor.
# Son no ordenados y las claves son únicas.

# Sintaxis Básica
# Definir un diccionario con claves y valores

#? Definición de diccionarios: Se muestran ejemplos de cómo definir diccionarios y acceder a sus valores.
#? Modificación de diccionarios: Se explican operaciones como modificar, agregar y eliminar pares clave-valor.
#? Métodos útiles: Se usan los métodos keys(), values(), items(), get(), update(), entre otros.
#? Operaciones adicionales: Se cubren funciones como len(), del y clear() para manipular diccionarios.


persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Otro ejemplo de diccionario
inventario = {
    "manzanas": 10,
    "naranjas": 5,
    "peras": 7
}

# Características de los Diccionarios
# 1. Colecciones No Ordenadas
# 2. Pares Clave-Valor
# 3. Acceso Rápido a Valores

# Ejemplos Prácticos

# Definición y Acceso
alumno = {
    "nombre": "Ana",
    "edad": 22,
    "curso": "Matemáticas"
}

# Accediendo a valores utilizando claves
nombre_alumno = alumno["nombre"]  # "Ana"
edad_alumno = alumno["edad"]  # 22
print(f"Nombre del alumno: {nombre_alumno}, Edad: {edad_alumno}")

# Modificación de Valores
# Los diccionarios son mutables
# Modificando un valor existente
alumno["edad"] = 23  # La edad ahora es 23
print(f"Edad actualizada: {alumno['edad']}")

# Agregando un nuevo par clave-valor
alumno["ciudad"] = "Barcelona"  # Se añade la clave "ciudad" con el valor "Barcelona"
print(f"Diccionario actualizado con ciudad: {alumno}")

# Eliminando un par clave-valor
del alumno["curso"]  # Se elimina la clave "curso" y su valor
print(f"Diccionario después de eliminar curso: {alumno}")

# Métodos Útiles de los Diccionarios

# keys(): Devuelve una vista de las claves del diccionario.
claves = alumno.keys()  
print(f"Claves del diccionario: {list(claves)}")

# values(): Devuelve una vista de los valores del diccionario.
valores = alumno.values()
print(f"Valores del diccionario: {list(valores)}")

# items(): Devuelve una vista de los pares clave-valor del diccionario.
items = alumno.items()  
print(f"Pares clave-valor: {list(items)}")

# get(): Devuelve el valor para una clave dada, o None si la clave no existe.
curso = alumno.get("curso")  # None, ya que la clave "curso" fue eliminada
print(f"El curso del alumno es: {curso}")

# update(): Actualiza el diccionario con los pares clave-valor de otro diccionario.
alumno.update({"edad": 24, "curso": "Física"})  # Actualiza la edad y añade el curso
print(f"Diccionario después de update: {alumno}")

# Funciones adicionales con Diccionarios

# len(): Devuelve el número de pares clave-valor en el diccionario.
print(f"Cantidad de elementos en el diccionario: {len(alumno)}")

# del: Elimina un par clave-valor usando la clave
del alumno["curso"]  # Eliminar la clave "curso"
print(f"Diccionario después de eliminar el curso: {alumno}")

# clear(): Elimina todos los elementos del diccionario.
alumno.clear()  # Elimina todos los elementos
print(f"Diccionario vacío: {alumno}")

# Ejemplo final de inventario
print(f"Inventario: {inventario}")
inventario.update({"naranjas": 10, "uvas": 8})  # Actualizando y agregando elementos
print(f"Inventario actualizado: {inventario}")
