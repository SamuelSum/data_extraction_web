'''Algunas APIs requieren autenticación, pero hay otras que
nos dejan practicar sin necesidad de claves de acceso.
Vamos a usar reqres.in, una API de prueba diseñada para
experimentar con métodos HTTP
URL base: https://reqres.in/api'''

import requests

# El id 675 me lo devolvio la respuesta del primer POST a la api
url = "https://reqres.in/api/users/675" 
data = {
    "name": "Samuel Actualizado",
    "job": "Conductor Internacional"
}

response = requests.put(url, json=data)

if response.status_code == 200:
    updated_user = response.json()
    print("Usuario actualizado con éxito")
    print(updated_user)
else:
    print(f"Error: {response.status_code}")