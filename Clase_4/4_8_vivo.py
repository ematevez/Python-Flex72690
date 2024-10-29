# control_de_flujo.py

# Unidad 4: Control de Flujo en Python

# Actividad 1: Generaciones digitales
# Consigna: Determinar a qué generación pertenece una persona según su año de nacimiento.
# Nota: Si el año no corresponde a ninguna generación conocida, se indica "No existe generación asociada".

# def determinar_generacion(ano_nacimiento):
ano_nacimiento = 1990
# ano_nacimiento = 2015
# ano_nacimiento= 1940

# """
# Determina la generación según el año de nacimiento.
# """
# if 1946 <=  ano_nacimiento <= 1964:
#     print("Baby Boomer")
# elif 1965 <= ano_nacimiento <= 1980:
#     print("Generación X")
# elif 1981 <= ano_nacimiento <= 1996:
#     print("Generación Y")
# elif 1997 <= ano_nacimiento <= 2012:    
#     print("Generación Z")
# elif 2013 <= ano_nacimiento <= 2025:
#     print("Generación Alpha")
# else:
#     print("No existe generación asociada")
    

# Ejemplo de uso:
# determinar_generacion(1990)  # Millennials
# determinar_generacion(2015)  # Generación Alpha
# determinar_generacion(1940)  # No existe generación asociada

# Actividad 2: Crédito Bancario
# Consigna: Aprobar o denegar un crédito bancario en función de la edad, antigüedad en el sistema financiero y los ingresos.

# def aprobar_credito(edad, antiguedad, ingreso):
# edad = 18
# antiguedad = 21
# ingreso = 3000
# """
#     Determina si se aprueba un crédito según criterios de edad, antigüedad y nivel de ingresos.
# """
# if edad >= 18:
#     if antiguedad >= 3 and ingreso >= 2500:
#         print("Crédito aprobado")
#     elif antiguedad < 3 and ingreso > 4000:
#         print("Crédito aprobado")
#     else: 
#         print("Crédito denegado")
# else:
#     print("Crédito denegado")
            

# Ejemplo de uso:
# print(aprobar_credito(15, 10, 1500))  # Crédito denegado
# print(aprobar_credito(20, 5, 3000))   # Crédito aprobado
# print(aprobar_credito(21, 2, 4000))   # Crédito aprobado

# # Actividad 3: Marvel vs. CapCom
# # Consigna: Asignar el grupo correspondiente a un usuario en función de su nombre y su preferencia.

# def asignar_grupo(nombre, preferencia):
#     """
#     Asigna el grupo A o B en función del nombre y preferencia (Marvel o Capcom).
#     """
    
    
    
# # Ejemplo de uso:
# print(asignar_grupo("Alan", "C"))  # Grupo B
# print(asignar_grupo("Carlos", "M"))  # Grupo A
# print(asignar_grupo("Pedro", "C"))  # Grupo A

# # Actividad 4: ¡Solicitud de números al usuario!
# # Consigna: Solicitar números al usuario hasta que ingrese "exit()" y mostrar la suma total acumulada.

# def sumar_numeros():
#     """
#     Solicita al usuario ingresar números y calcula la suma total hasta que el usuario ingrese 'exit()'.
#     """
# suma = 0
# numero = input('Ingrese numero que quiere sumar: ')

# while numero != 'exit':
#     numero = int(numero)
#     suma += numero
#     numero = input('Ingrese numero que quiere sumar: ')
    
# print(f'Suma total: {suma}')
# print('Fin del programa')

# def sumar_numeros():
#     """
#     Solicita al usuario ingresar números y calcula la suma total hasta que el usuario ingrese 'exit()'.
#     """
#     suma_total = 0
#     while True:
#         entrada = input("Ingresa un número (o escribe 'exit()' para finalizar): ")
#         if entrada.lower() == "exit":
#             break
#         else:
#             try:
#                 numero = int(entrada)
#                 suma_total += numero
#                 print(f"Suma paexit()rcial: {suma_total}")
#             except ValueError:
#                 print("Por favor, ingresa un número entero válido.")
#     print(f"Suma total: {suma_total}")

    

# # # Para ejecutar esta función, descomente la línea siguiente
# sumar_numeros()



# # Actividad 5: Sentencia break
# # Consigna: Análisis de un bucle con la sentencia break.

# def ejemplo_break():
#     """
#     Ejemplo de uso de la sentencia break en un bucle while.
#     """
#     x = 5
#     while True:
#         x -= 1
#         print(x)
#         if x == 0:
#             break
#     print("Fin del bucle")

# Ejemplo de uso:
# ejemplo_break()
# # Actividad 6: Canción - Me Gusta
# # Consigna: Imprimir la letra de la canción "Me gusta" de Manu Chao usando un bucle for.

# def imprimir_cancion():
#     """
#     Imprime la letra de la canción 'Me gusta' de Manu Chao usando un bucle for.
#     """
#     letras = [
#         "Me gustan los aviones, me gustas tú",
#         "Me gusta viajar, me gustas tú",
#         "Me gusta la mañana, me gustas tú",
#         "Me gusta el viento, me gustas tú",
#         "Me gusta soñar, me gustas tú",
#         "Me gusta la mar, me gustas tú"
#     ]
    
#     for letra in letras:
#         print(letra)
        
    
# # Ejemplo de uso:
# imprimir_cancion()

# # Cierre y preguntas
# # Resumen de la clase repasando los puntos clave vistos durante la unidad.
# # Espacio para consultas finales.
c = -3
while c < 10:
    c += 1
    if c == 2:
        ...
    print('c vale_pass', c)
    
print("==============================================================")
c = -3
while c < 10:
    c += 1
    if c == 2:
        continue
    print('c vale_contunue', c)    
