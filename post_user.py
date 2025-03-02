'''Algunas APIs requieren autenticación, pero hay otras que
nos dejan practicar sin necesidad de claves de acceso.
Vamos a usar reqres.in, una API de prueba diseñada para
experimentar con métodos HTTP
URL base: https://reqres.in/api'''

import requests 

url = "https://reqres.in/api/users"
data = {
    "name": "Samuel",
    "job": "Chófer de pruebas"
}

response = requests.post(url, json=data)

if response.status_code == 201:
    user = response.json()
    print("Usuario creado con éxito")
    print(user)
else:
    print(f"Error: {response.status_code}")