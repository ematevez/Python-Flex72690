import os
import msvcrt  # Solo funciona en Windows; para otros SO usa el módulo 'getch' de `curses`
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# Funciones de las opciones (actualmente en blanco)
def opcion1():
    print(Fore.BLUE + "Opción 1 seleccionada.")
    # Aquí puedes agregar el código de la opción 1

def opcion2():
    print(Fore.GREEN + "Opción 2 seleccionada.")
    # Aquí puedes agregar el código de la opción 2

def opcion3():
    print(Fore.RED + "Opción 3 seleccionada.")
    # Aquí puedes agregar el código de la opción 3

def opcion4():
    print(Fore.YELLOW + "Opción 4 seleccionada.")
    # Aquí puedes agregar el código de la opción 4

def opcion5():
    print(Fore.MAGENTA + "Opción 5 seleccionada.")
    # Aquí puedes agregar el código de la opción 5

def menu_principal():
    """
    Muestra el menú principal y gestiona la selección del usuario.
    """
    while True:
        # Limpiar la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')

        # Mostrar el menú con colores
        print(Fore.BLUE + "1. Opción 1")
        print(Fore.GREEN + "2. Opción 2")
        print(Fore.RED + "3. Opción 3")
        print(Fore.YELLOW + "4. Opción 4")
        print(Fore.MAGENTA + "5. Opción 5")
        print(Fore.WHITE + "0. Salir (o presione Esc)")

        # Solicitar entrada del usuario
        print(Fore.CYAN + "\nSeleccione una opción: ")
        seleccion = msvcrt.getch().decode('utf-8')  # Captura de teclado en Windows
        # seleccion = input("\nSeleccione una opción: ") #Para el que tiene linux o mac
            
        # Manejar selección
        if seleccion == '1':
            opcion1()
        elif seleccion == '2':
            opcion2()
        elif seleccion == '3':
            opcion3()
        elif seleccion == '4':
            opcion4()
        elif seleccion == '5':
            opcion5()
        elif seleccion == '0' or seleccion == '\x1b':  # Esc = '\x1b'
            print("Saliendo del programa...")
            break
        else:
            print(Fore.RED + "Opción no válida. Intente nuevamente.")

        # Pausa para volver al menú
        print("\nPresione cualquier tecla para volver al menú...")
        msvcrt.getch()  # Espera a que el usuario presione una tecla

# Ejecutar el menú principal
menu_principal()

"""
Explicación del código
Colores: Usamos colorama para cambiar los colores en la terminal, asignando un color a cada opción.
Funciones de opciones: Las funciones opcion1() a opcion5() están vacías para que puedas completarlas más tarde.
Menú principal:
msvcrt.getch() captura teclas sin necesidad de presionar Enter, facilitando la entrada de datos.
0 o Esc salen del programa.
Pausa: Tras seleccionar una opción, el programa muestra un mensaje para volver al menú principal.
Nota: msvcrt solo está disponible en Windows.

"""
"""
    Convierte entre milímetros y metros, dependiendo de los argumentos recibidos.
    Parámetros:
        args: Puede ser uno o tres argumentos.
    Si recibe un argumento, se considera como milímetros y se convierte a metros, centímetros y milímetros.
    Si recibe tres argumentos, se considera como metros, centímetros y milímetros y se convierte a milímetros.
    Ejemplo:
        - convertir_medida(1500) -> (1.5, 0.0, 0.0)
        - convertir_medida(1, 50, 0) -> 1050
"""
