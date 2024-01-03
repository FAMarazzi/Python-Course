import requests, json
# nuevo_usuario={
#                 "id": 11,
#                 "name": "Leonora Roger",
#                 "username": "Racigret",
#                 "email": "Sincerely@alwayz.biz",
#                 "address": {
#                     "street": "Kura Street",
#                     "suite": "Apt. 626",
#                     "city": "Greenworld",
#                     "zipcode": "1827",
#                     "geo": {
#                             "lat": "-31.3159",
#                             "lng": "82.1496"
#                             }
#                 },
#                 "phone": "2115-14221-511",
#                 "website": "onedayiwill.org",
#                 "company": {
#                     "name": "Lina Beach",
#                     "catchPhrase": "We are yours",
#                     "bs": "supreme"
#                     }
#                 }  

nuevo_usuario={
    'id': 101,
    'title': 'Broder',
    'body': 'Un capo el broder, saludos',
    'userId': 11
  }
headers = {
    "Content-Type": "application/json"
}

url="https://jsonplaceholder.typicode.com"

def obtener_informacion():
    try:
        response=requests.get(f"{url}/users")
        
        response.raise_for_status()
        datos=response.json()
        return datos
    except requests.exceptions.HTTPError as errh:
        # Manejar errores HTTP, por ejemplo, 404 Not Found, 500 Internal Server Error, etc.
        print(f"Error HTTP: {errh}")
    except requests.exceptions.ConnectionError as errc:
        # Manejar errores de conexión, por ejemplo, el servidor no está disponible
        print(f"Error de conexión: {errc}")
    except requests.exceptions.Timeout as errt:
        # Manejar errores de tiempo de espera
        print(f"Tiempo de espera agotado: {errt}")
    except requests.exceptions.RequestException as e:
        # Manejar cualquier otro error de solicitud (por ejemplo, conexión fallida, tiempo de espera, etc.)
        print(f"Error en la solicitud: {e}")
def mostrar_datos(cantidad=3):
    for dato in range(3):
        print("\n")
        print(f"ID: {datos[dato]['id']}")
        print(f"Name: {datos[dato]['name']}")
        print(f"Username: {datos[dato]['username']}")
        print(f"Email: {datos[dato]['email']}")
    print("\n")

def crear_usuario(usuario):
    try:
        response=requests.post(f"{url}/posts", data=json.dumps(usuario), headers=headers)
        response.raise_for_status()
        print(response.status_code)
        datos=response.json()
        return datos
    except requests.exceptions.RequestException as e:
        # Manejar cualquier error genérico de solicitud
        print(f"Error en la solicitud: {e}")

def modificar_usuario(id, usuario_actualizado):
    try:
        response=requests.patch(f"{url}/posts/{id}", json=usuario_actualizado)
        response.raise_for_status()
        print(response.status_code)
        datos=response.json()
        return datos
    except requests.exceptions.RequestException as e:
        # Manejar cualquier error genérico de solicitud
        print(f"Error en la solicitud: {e}")
        
while(True):
    entrada=int(input("""¿Buenas tardes, aquí puede interactuar con los usuarios de JsonPlaceHolder. Que desea hacer?
    1. Imprimir la información de los primeros 3 usuarios.
    2. Crear un nuevo usuario.
    3. Reemplazar todos los datos de un usuario
    4. Modificar un dato de algún usuario
    5. Eliminar usuario.
    6. Cerrar programa.\n"""))
    if(entrada==1):
        datos=obtener_informacion()
        mostrar_datos()
    elif(entrada==2):
        usuario_creado=crear_usuario(nuevo_usuario)
        print("Los datos del usuario se han cargado correctamente:\n")
        print(f"ID: {usuario_creado["id"]}")
        print(f"Title: {usuario_creado["title"]}")
        print(f"Body: {usuario_creado["body"]}")
        print(f"userId: {usuario_creado['userId']}")
        print("\n")
    elif(entrada==4):
        user_id=input("Qué ID deseas modificar?")
        dato=input("Que dato deseas modificar?")
        nuevo_valor=input("Ingresa el nuevo valor para ese dato")
        usuario_actualizado=dict.fromkeys([dato], nuevo_valor)
        respuesta=modificar_usuario(user_id, usuario_actualizado)
        print(respuesta)
        
        
    elif(entrada==6):
        break
