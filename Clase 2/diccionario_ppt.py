"""
Trabajaremos con el notebook de la sesión, específicamente sobre la temática de Diccionarios.

Deberás crear un diccionario que almacene a los ganadores de la Copa Mundial de la FIFA desde el año 1990 al 2018. Y mostrarlo por pantalla.


"""

ganadores_copa_mundial = {
    1990: 'Alemania',
    1994: 'Brasil',
    1998: 'Francia',
    2002: 'Brasil',
    2006: 'Italia',
    2010: 'España',
    2014: 'Alemania',
    2018: 'Francia',
    2022: 'Argentina'

}
# Mostrar el diccionario de ganadores
print(f"Ganadores de la Copa Mundial de la FIFA (1990-2022): {ganadores_copa_mundial}")

print("===============================================================")
for año, pais in ganadores_copa_mundial.items():
    print(f"{año}: {pais}")
