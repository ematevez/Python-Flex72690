"""
Descripción de la actividad:

En esta actividad, podrás poner en práctica lo aprendido. Usaremos Visual Studio Code.

Crea dos listas lista_1 y lista_2, con cualquier elemento que quieras. Realiza los siguientes puntos usando las funciones integradas ya vistas y el método slice [ : ] Imprime la lista correspondiente luego de cada punto.

Añade a la lista_1 el <int> 456789 y luego el <str> "Hola Mundo"
Luego añade a la lista_2 el <str> "Hola y adiós", y luego el <int> 5555
Genera una lista_3 con todos los elementos de la lista_1 sin considerar el último elemento [:]
Genera una lista_4 con todos los elementos de la lista_2 menos el primero y el último elemento [:]
Finalmente, genera una lista_5 con los elementos de la lista_4 y de la lista_3 

"""
#Creamos listas
lista_1 = [1,2,3,4,5]
lista_2 = ["auto", "35","64","caramelo"]

#Añade a la lista_1 el <int> 456789 y luego el <str> "Hola Mundo"
lista_1.append(456789)
lista_1.append("Hola mundo")
print("Lista 1 despues de agregar los elementos:", lista_1)

#Luego añade a la lista_2 el <str> "Hola y adiós", y luego el <int> 5555
lista_2.append("Hola y adios")
lista_2.append(555)
print("Lista 2 despues de agregar los elementos:", lista_2)

# Genera una lista_3 con todos los elementos de la lista_1 sin considerar el último elemento [:]
#Dos maneras diferentes de obtener el mismo resultado
lista_3 = lista_1[:6]
print("Lista 3 sin el último elemento de lista_1:", lista_3)
lista_33 = lista_1[:-1]
print("Lista 3 sin el último elemento de lista_1:", lista_33)

# Genera una lista_4 con todos los elementos de la lista_2 menos el primero y el último elemento [:]
#Dos maneras diferentes de obtener el mismo resultado
lista_4 = lista_2[1:-1]
print("Lista 4 sin el primer y el último elemento de lista_2:", lista_4)
lista_44 = lista_2[1:5]
print("Lista 4 sin el primer y el último elemento de lista_2:", lista_44)

# Finalmente, genera una lista_5 con los elementos de la lista_4 y de la lista_3 
lista_5 = lista_4 +  lista_3
print("Lista 5 combinando lista_3 y lista_4:", lista_5)


lista_6 =  lista_2 + lista_1 
print("Lista 6 combinando lista_1 y lista_2:", lista_6)