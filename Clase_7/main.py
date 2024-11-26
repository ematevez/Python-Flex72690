# main.py
from calculator import Calculator
from colorama import Fore, Style

def main():
    calc = Calculator()
    print(calc)  # Imprime "Soy una calculadora" en azul

    print(f"{Fore.YELLOW}Calculadora avanzada{Style.RESET_ALL}")
    print(f"{Fore.CYAN}1. Sumar{Style.RESET_ALL}")
    print(f"{Fore.CYAN}2. Restar{Style.RESET_ALL}")
    print(f"{Fore.CYAN}3. Multiplicar{Style.RESET_ALL}")
    print(f"{Fore.CYAN}4. Dividir{Style.RESET_ALL}")
    print(f"{Fore.CYAN}5. Promedio de 4 números{Style.RESET_ALL}")

    try:
        option = int(input(f"{Fore.GREEN}Elige una opción (1-5): {Style.RESET_ALL}"))
        
        if option == 5:  # Promedio de 4 números
            nums = []
            for i in range(4):
                num = float(input(f"{Fore.GREEN}Introduce el número {i + 1}: {Style.RESET_ALL}"))
                nums.append(num)
            result = calc.average(*nums)
            print(f"{Fore.MAGENTA}Resultado: {result}{Style.RESET_ALL}")
        else:
            num1 = float(input(f"{Fore.GREEN}Introduce el primer número: {Style.RESET_ALL}"))
            num2 = float(input(f"{Fore.GREEN}Introduce el segundo número: {Style.RESET_ALL}"))

            if option == 1:
                result = calc.add(num1, num2)
                print(f"{Fore.MAGENTA}Resultado: {result}{Style.RESET_ALL}")
            elif option == 2:
                result = calc.subtract(num1, num2)
                print(f"{Fore.MAGENTA}Resultado: {result}{Style.RESET_ALL}")
            elif option == 3:
                result = calc.multiply(num1, num2)
                print(f"{Fore.MAGENTA}Resultado: {result}{Style.RESET_ALL}")
            elif option == 4:
                result = calc.divide(num1, num2)
                print(f"{Fore.MAGENTA}Resultado: {result}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Opción no válida.{Style.RESET_ALL}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
