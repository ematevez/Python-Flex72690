
# Ejemplos didácticos de métodos de cadenas en Python

# upper() - Convierte todos los caracteres de la cadena a mayúsculas
cadena = "Hola Mundo"
print('upper():', cadena.upper())  # HOLA MUNDO

# lower() - Convierte todos los caracteres de la cadena a minúsculas
print('lower():', cadena.lower())  # hola mundo

# capitalize() - Convierte el primer carácter de la cadena a mayúscula y el resto a minúsculas
cadena = "hola mundo"
print('capitalize():', cadena.capitalize())  # Hola mundo

# title() - Convierte el primer carácter de cada palabra a mayúscula y el resto a minúsculas
print('title():', cadena.title())  # Hola Mundo

# count() - Cuenta cuántas veces aparece una subcadena en la cadena
cadena = "Hola mundo, hola universo"
print('count("hola"):', cadena.count("hola"))  # 1 (sensible a mayúsculas)

# find() - Devuelve el índice de la primera aparición de una subcadena en la cadena
cadena = "Hola mundo"
print('find("mundo"):', cadena.find("mundo"))  # 5

# rfind() - Devuelve el índice de la última aparición de una subcadena en la cadena
cadena = "Hola mundo, hola universo"
print('rfind("hola"):', cadena.rfind("hola"))  # 12

# split() - Divide la cadena en una lista utilizando el separador especificado
cadena = "Hola mundo"
print('split():', cadena.split())  # ['Hola', 'mundo']

# join() - Une una lista de cadenas utilizando la cadena como separador
lista = ["Hola", "mundo"]
print('join():', " ".join(lista))  # Hola mundo

# strip() - Elimina los caracteres especificados (por defecto, espacios) desde el principio y el final de la cadena
cadena = "   Hola mundo   "
print('strip():', cadena.strip())  # "Hola mundo"

# replace() - Reemplaza todas las apariciones de una subcadena por otra subcadena
cadena = "Hola mundo"
print('replace("mundo", "universo"):', cadena.replace("mundo", "universo"))  # Hola universo
