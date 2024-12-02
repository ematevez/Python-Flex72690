def leer_csv_sin_pandas(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            # Leer todas las líneas del archivo
            lineas = archivo.readlines()
            
            # Asegurarse de que no está vacío
            if not lineas:
                print("El archivo está vacío.")
                return
            
            # Primera línea: Títulos de las columnas
            titulos = lineas[0].strip().split(",")  # Eliminar saltos de línea y dividir por comas
            print("Títulos de las columnas:")
            print(titulos)
            print()
            
            # Mostrar los primeros 5 registros
            print("Primeros 5 registros:")
            for linea in lineas[1:6]:  # Saltar la primera línea (títulos) y tomar las siguientes 5
                registro = linea.strip().split(",")  # Dividir cada línea en una lista
                print(registro)
    except FileNotFoundError:
        print(f"El archivo '{ruta}' no existe. Por favor verifica la ruta y el nombre.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

# Ruta al archivo cargado
ruta_archivo = 'disney_plus_titles.csv'

# Llamar a la función para leer y mostrar los datos
leer_csv_sin_pandas(ruta_archivo)


"""Explicación del Script:
Abrir el archivo:

Se usa open con la ruta proporcionada.
El modo 'r' es para lectura y 'utf-8' asegura que se manejen caracteres especiales correctamente.
Leer líneas:

readlines() lee todas las líneas del archivo y las guarda en una lista.
Procesar Títulos:

La primera línea contiene los títulos, que se dividen en una lista usando split(",").
Mostrar Registros:

Se itera sobre las líneas desde la segunda hasta la sexta (índices 1:6) para mostrar los primeros 5 registros.
Manejo de Errores:

FileNotFoundError maneja el caso en que el archivo no existe.
Un bloque except Exception captura otros errores inesperados.
Instrucciones para Ejecutar:
Asegúrate de que el archivo disney_plus_titles.csv esté en la ruta especificada.
Ejecuta el script en tu entorno Python.
El script mostrará los títulos de las columnas y los primeros cinco registros.
"""

#!===============================================================
# import pandas as pd

# def mostrar_datos_csv(ruta):
#     try:
#         # Leer el archivo CSV
#         datos = pd.read_csv(ruta)
        
#         # Mostrar las columnas del archivo
#         print("Títulos de las columnas:")
#         print(datos.columns.tolist())  # Convertir los títulos a una lista para mejor presentación
#         print()
        
#         # Mostrar los primeros 5 registros de las primeras 5 columnas
#         print("Primeros 5 registros (5 primeras columnas):")
#         print(datos.iloc[:5, :5])  # Seleccionar las filas y columnas específicas
#     except FileNotFoundError:
#         print(f"El archivo '{ruta}' no existe. Por favor verifica la ruta y el nombre.")
#     except Exception as e:
#         print(f"Ocurrió un error al procesar el archivo: {e}")

# # Ruta al archivo cargado
# ruta_archivo = 'disney_plus_titles.csv'

# # Llamar a la función para leer y mostrar los datos
# mostrar_datos_csv(ruta_archivo)
