'''Algunas APIs requieren autenticación, pero hay otras que
nos dejan practicar sin necesidad de claves de acceso.
Vamos a usar reqres.in, una API de prueba diseñada para
experimentar con métodos HTTP
URL base: https://reqres.in/api'''

import requests

url = "https://reqres.in/api/users/675"

response = requests.delete(url)

if response.status_code == 204: # DELETE devuelve 204 No content
    print("Usuario eliminado correctamente")
else:
    print(f"Error : {response.status_code}")