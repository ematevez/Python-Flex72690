"""
No hay 3.8 es un video de cierre de unidad

Solución Paso a Paso

Crear una lista original: Se crea una lista inicial que contiene números, algunos de los cuales son duplicados.

Borrar los elementos duplicados: Se utiliza un conjunto (set) para eliminar duplicados, ya que los conjuntos no permiten elementos repetidos.

Ordenar la lista de mayor a menor: Se convierte el conjunto de nuevo a lista y se ordena.

Eliminar todos los números impares: Se itera sobre la lista y se eliminan los números impares usando un bucle for y remove().

Realizar la suma de todos los números que quedan: Se usa la función sum() para calcular la suma de los elementos restantes.

Añadir la suma como primer elemento de la lista: Se utiliza insert(0, suma) para añadir la suma al principio de la lista.

Devolver la lista modificada: La función devuelve la lista final.

Comprobar la suma: Se verifica que la suma de los elementos a partir del segundo concuerda con el primer número de la lista.

"""

def procesar_lista(lista_original):
    # Paso 1: Borrar los elementos duplicados
    lista_sin_duplicados = list(set(lista_original))
    
    # Paso 2: Ordenar la lista de mayor a menor
    lista_sin_duplicados.sort(reverse=True)
    
    # Paso 3: Eliminar todos los números impares
    for num in lista_sin_duplicados[:]:  # Iterar sobre una copia de la lista
        if num % 2 == 1:  # Si es impar
            lista_sin_duplicados.remove(num)
    
    # Paso 4: Realizar la suma de todos los números que quedan
    suma = sum(lista_sin_duplicados)
    
    # Paso 5: Añadir la suma como primer elemento de la lista
    lista_sin_duplicados.insert(0, suma)
    
    # Paso 6: Comprobar la suma
    suma_comprobacion = sum(lista_sin_duplicados[1:])
    print(f"Suma verificada: {suma_comprobacion} == {lista_sin_duplicados[0]}")
    
    return lista_sin_duplicados

# Alternativa 1: Usando comprensión de listas
def procesar_lista_comprension(lista_original):
    lista_sin_duplicados = list(set(lista_original))
    lista_sin_duplicados.sort(reverse=True)
    
    # Eliminar números impares usando comprensión de listas
    lista_sin_impares = [num for num in lista_sin_duplicados if num % 2 == 0]
    
    suma = sum(lista_sin_impares)
    lista_sin_impares.insert(0, suma)
    
    suma_comprobacion = sum(lista_sin_impares[1:])
    print(f"Suma verificada (comprensión): {suma_comprobacion} == {lista_sin_impares[0]}")
    
    return lista_sin_impares

#! Alternativa 2: Usando filter para eliminar impares muy dificil no imposible
def procesar_lista_filter(lista_original):
    lista_sin_duplicados = list(set(lista_original))
    lista_sin_duplicados.sort(reverse=True)
    
    # Usar filter para eliminar números impares
    lista_sin_impares = list(filter(lambda x: x % 2 == 0, lista_sin_duplicados))
    
    suma = sum(lista_sin_impares)
    lista_sin_impares.insert(0, suma)
    
    suma_comprobacion = sum(lista_sin_impares[1:])
    print(f"Suma verificada (filter): {suma_comprobacion} == {lista_sin_impares[0]}")
    
    return lista_sin_impares


def alternativa(listanumeros):
    #que en algun numero,
    for numero in listanumeros:
        #calcular residuo de numero sobre 2, 
        if numero % 2 == 1:
            listanumeros.remove(numero)
            print(f" removiendo {numero} por ser impar")
        #mientras que haya algun numero repetido -con un count mayor a uno-
        while listanumeros.count(numero) > 1:
            #remover la ultima incidencia de ese numero           
            listanumeros.remove(numero)
            print(f"removiendo duplicado de  {numero}. lista parcialmente depurada {listanumeros}") 
    listanumeros.sort(reverse=True)
    print(f"lista depurada {listanumeros}")








# Lista inicial
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

# Ejecutar las funciones
print("============================================================")
print("Resultado con procesamiento estándar:")
resultado = procesar_lista(lista)
print(f"Lista modificada: {resultado}\n")
print("============================================================")
print("Resultado con comprensión de listas:")
resultado_comprension = procesar_lista_comprension(lista)
print(f"Lista modificada: {resultado_comprension}\n")
print("============================================================")
print("Resultado con filter:")
resultado_filter = procesar_lista_filter(lista)
print(f"Lista modificada: {resultado_filter}\n")
print("============================================================")
print("Resultado by OMAR:")
alternativa(lista)



"""
Explicación de Cada Función
procesar_lista: Implementa el proceso estándar utilizando bucles.
procesar_lista_comprension: Utiliza comprensión de listas para eliminar los números impares.
procesar_lista_filter: Utiliza filter para filtrar los números impares.
Cada función imprime la suma verificada y devuelve la lista modificada. Esto proporciona tres enfoques diferentes para resolver la misma tarea, ayudando a entender diferentes técnicas de Python.

"""