import requests
import json

url="https://jsonplaceholder.typicode.com"
datos_limpios=[]

# def obtener_post():
#     response_id=requests.get(f"{url}/posts/{id}")
#     response_id.raise_for_status()
#     datos_id=response_id.json()
#     print(datos_id)
    
def obtener_posts(id=None):
    try:
        #mando petición get
        if(id):
            response=requests.get(f"{url}/posts/{id}")         
        else:
            response= requests.get(f'{url}/posts')
        #verifico si fue exitosa
        #exitosa significa que el estado es 200, de no ser así, lanza una excepción
        response.raise_for_status()
        #lo guardo si fue exitosa
        print(type(response))
        datos=response.json()
        print(type(datos))
        return datos

    except requests.exceptions.HTTPError as errh:
        # Manejar errores HTTP, por ejemplo, 404 Not Found, 500 Internal Server Error, etc.
        print(f"Error HTTP: {errh}. No existe el id {id}")
    except requests.exceptions.ConnectionError as errc:
        # Manejar errores de conexión, por ejemplo, el servidor no está disponible
        print(f"Error de conexión: {errc}")
    except requests.exceptions.Timeout as errt:
        # Manejar errores de tiempo de espera
        print(f"Tiempo de espera agotado: {errt}")
    except requests.exceptions.RequestException as e:
        # Manejar cualquier otro error de solicitud (por ejemplo, conexión fallida, tiempo de espera, etc.)
        print(f"Error en la solicitud: {e}")

def mostrar_resultados(datos, cantidad=1):
    if cantidad==1:
        print("---------------\n")
        print(f"ID: {datos['id']}")
        print(f"Title: {datos['title']}")
        print(f"Body: {datos['body']}")
    else:
        for dato in range(cantidad):
            print("---------------\n")
            print(f"ID: {datos[dato]['id']}")
            print(f"Title: {datos[dato]['title']}")
            print(f"Body: {datos[dato]['body']}")
    print("---------------\n")
datos=obtener_posts()    
mostrar_resultados(datos, 5)

while(True):
    try:
        id_post=int(input("¿Desea visualizar alguna publicación específica? Ingrese el ID: "))
        
        datos_id=obtener_posts(id_post)
        
        mostrar_resultados(datos_id)
        break
    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese sólo números")
    except Exception as e:
        print(f"Error: {e}")

    #datos_limpios.append(datos[dato])
#print(datos_limpios)
       
# with open("uso_apis\\datos.json", "w") as archivo_json:
#     json.dump(datos, archivo_json, indent=2)
