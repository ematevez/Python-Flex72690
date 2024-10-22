# Introducción a los Diccionarios en Python
# Los diccionarios son estructuras de datos que almacenan pares clave-valor.
# Son útiles cuando necesitas asociar valores con identificadores únicos.

# Ejemplo de diccionario:
colores = {"amarillo": "yellow", "azul": "blue", "verde": "green"}

# 1. Método get()
# El método get() se usa para obtener el valor asociado a una clave.
# Si la clave no existe, devuelve un valor por defecto que se puede especificar.
print("=== Método get() ===")
print(colores.get("amarillo"))  # Devuelve "yellow"
print(colores.get("rojo", "no hay clave rojo"))  # Devuelve el valor por defecto "no hay clave rojo"
print()  # Línea en blanco para separar salidas

# 2. Método keys()
# El método keys() devuelve una vista con todas las claves del diccionario.
print("=== Método keys() ===")
print(colores.keys())  # Devuelve dict_keys(['amarillo', 'azul', 'verde'])
print()  # Línea en blanco para separar salidas

# 3. Método values()
# El método values() devuelve una vista con todos los valores del diccionario.
print("=== Método values() ===")
print(colores.values())  # Devuelve dict_values(['yellow', 'blue', 'green'])
print()  # Línea en blanco para separar salidas

# 4. Método items()
# El método items() devuelve todos los pares clave-valor como tuplas dentro de una vista.
print("=== Método items() ===")
print(colores.items())  # Devuelve dict_items([('amarillo', 'yellow'), ('azul', 'blue'), ('verde', 'green')])
print()  # Línea en blanco para separar salidas

# Iterar sobre items()
print("=== Iterando sobre items() ===")
for clave, valor in colores.items():
    print(f"La clave es {clave} y el valor es {valor}")
print()  # Línea en blanco para separar salidas

# 5. Añadir y modificar elementos en un diccionario
# Si una clave ya existe, su valor se actualiza. Si no, se añade un nuevo par clave-valor.
print("=== Añadir y modificar elementos ===")
colores["rojo"] = "red"  # Añadiendo un nuevo par clave-valor
colores["verde"] = "green light"  # Modificando un valor existente
print(colores)  # Debería incluir ahora "rojo": "red" y el valor de "verde" modificado
print()  # Línea en blanco para separar salidas

# 6. Eliminar elementos del diccionario
# Usamos pop() para eliminar un elemento y devolver su valor.
# Si la clave no existe, pop() puede devolver un valor por defecto.
print("=== Eliminar elementos con pop() ===")
valor_eliminado = colores.pop("azul", "no existe")  # Elimina la clave "azul"
print(f"Elemento eliminado: {valor_eliminado}")
print(colores)  # El diccionario ya no debería incluir la clave "azul"
print()  # Línea en blanco para separar salidas

# También puedes usar del para eliminar directamente un par clave-valor.
print("=== Eliminar usando del ===")
del colores["amarillo"]  # Elimina "amarillo"
print(colores)  # El diccionario solo debería tener "verde" y "rojo"
print()  # Línea en blanco para separar salidas

# 7. Verificar si una clave existe en el diccionario
# Podemos usar el operador `in` para verificar si una clave está presente.
print("=== Verificar si existe una clave ===")
if "rojo" in colores:
    print("La clave 'rojo' existe en el diccionario.")
else:
    print("La clave 'rojo' no existe en el diccionario.")
print()  # Línea en blanco para separar salidas

# 8. Limpiar el diccionario
# El método clear() elimina todos los elementos del diccionario.
print("=== Limpiar el diccionario ===")
colores.clear()
print(colores)  # Debería devolver un diccionario vacío: {}
print()

# 9. Copiar un diccionario
# El método copy() permite hacer una copia superficial del diccionario.
print("=== Copiar un diccionario ===")
nuevos_colores = {"blanco": "white", "negro": "black"}
copia_colores = nuevos_colores.copy()
print(copia_colores)  # Debería devolver {'blanco': 'white', 'negro': 'black'}


"""
Explicación de temas agregados:
Añadir y modificar elementos: Explico cómo agregar o modificar elementos en un diccionario usando la sintaxis de acceso por clave.
Eliminar elementos: Uso del método pop() para eliminar elementos y también cómo usar del para eliminarlos.
Verificar si una clave existe: Explicación sobre cómo verificar la presencia de una clave en el diccionario usando in.
Limpiar el diccionario: Uso del método clear() para vaciar un diccionario.
Copiar un diccionario: Explicación del método copy() para duplicar un diccionario.

"""