import requests

# La url de la API
url = 'https://jsonplaceholder.typicode.com/users'

# Realizamos la solicitud GET
response = requests.get(url)

# Verificamos si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    print("Solicitud exitosa")
    # Parseamos la respuesta JSON
    users = response.json()
    # Mostramos los datos de los usuarios
    for user in users:
        print(f"Nombre: {user['name']}, Correo: {user['email']}")

elif response.status_code == 404:
    print("Recurso no encontrado")
elif response.status_code == 401:
    print("Se requiere autenticacion")
else:
    print(f"Error en la solicitud: {response.status_code}")        
