# calculator.py
from colorama import Fore, Style

class Calculator:
    def __str__(self):
        return f"{Fore.BLUE}Soy una calculadora{Style.RESET_ALL}"

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError(f"{Fore.RED}No se puede dividir entre cero.{Style.RESET_ALL}")
        return a / b

    def average(self, a, b, c, d):
        return (a + b + c + d) / 4
