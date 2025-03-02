'''Algunas APIs requieren autenticación, pero hay otras que
nos dejan practicar sin necesidad de claves de acceso.
Vamos a usar reqres.in, una API de prueba diseñada para
experimentar con métodos HTTP
URL base: https://reqres.in/api'''

import requests

# Usamos el id que nos devolvio el post.
url = "https://reqres.in/api/users/675"
data = {
    "job": "Serpentologo"
}

response = requests.patch(url, json=data)

if response.status_code == 200:
    partially_updated_user = response.json()
    print("Trabajo actualizado con exito")
    print(partially_updated_user)
else:
    print(f"Error: {response.status_code}")