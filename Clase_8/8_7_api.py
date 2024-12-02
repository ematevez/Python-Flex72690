import requests
import json

# URL de la Fake API (JSONPlaceholder)
url = "https://jsonplaceholder.typicode.com/posts"

def obtener_datos_y_guardar():
    try:
        # Obtener datos de la API
        respuesta = requests.get(url)
        
        # Comprobar si la respuesta es exitosa (código 200)
        if respuesta.status_code == 200:
            datos = respuesta.json()  # Convertir la respuesta a JSON

            # Mostrar los primeros 5 registros por pantalla
            print("Primeros 5 registros de la API:")
            for i, item in enumerate(datos[:5]):
                print(f"{i+1}. {item}")
            
            # Guardar los datos en un archivo .txt
            with open("datos_api.txt", "w") as archivo_txt:
                for item in datos:
                    archivo_txt.write(f"{item}\n")
            print("\nDatos guardados en 'datos_api.txt'.")
            
            # Guardar los datos en un archivo .json
            with open("datos_api.json", "w") as archivo_json:
                json.dump(datos, archivo_json, indent=4)
            print("Datos guardados en 'datos_api.json'.")
        
        else:
            print("Error: No se pudo obtener los datos de la API.")
    
    except Exception as e:
        print(f"Error al obtener o guardar los datos: {e}")

# Llamar a la función para obtener los datos y guardarlos
obtener_datos_y_guardar()


