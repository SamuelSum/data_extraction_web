import requests
from bs4 import BeautifulSoup

# URL base para provincia de Cádiz
base_url = "https://www.coches.net/segunda-mano/?arrProvince=11&pg="

# Cabecera para simular un navegador y evitar bloqueos
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'es-ES,es;q=0.9',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Referer': 'https://www.coches.net/',
    'Origin': 'https://www.coches.net/',
}

# Número de páginas a iterar
pages_to_scrape = 5  # Puedes modificar este valor para más páginas

# Iteramos por las páginas
for page in range(pages_to_scrape):
    print(f"Recuperando página {page + 1}...")
    
    # Construimos la URL para la página actual
    url = base_url + str(page)
    
    # Hacemos la petición a la web
    response = requests.get(url, headers=headers)

    # Si la respuesta es correcta (código 200), seguimos
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Buscamos todos los contenedores de los anuncios de coches
        car_ads = soup.find_all("div", class_="mt-AnimationFadeOut mt-ListAds-item mt-CardAd mt-CardBasic")

        # Si no encontramos anuncios en esta página, pasamos a la siguiente
        if not car_ads:
            print("No se encontraron anuncios en esta página.")
            continue

        # Iteramos sobre los anuncios
        for car in car_ads:
            # Extraemos el enlace del coche y su título
            title = car.find("h2", class_="mt-CardAd-infoHeaderTitle").text.strip()
            link = "https://www.coches.net" + car.find("a", class_="mt-CardBasic-titleLink")["href"]

            # Extraemos el precio
            price = car.find("h3", class_="mt-TitleBasic-title").text.strip() if car.find("h3", class_="mt-TitleBasic-title") else "No disponible"

            # Extraemos los detalles (combustible, año, km, cv, ubicación)
            details = car.find_all("li", class_="mt-CardAd-attrItem")
            car_details = [detail.text.strip() for detail in details]

            # Mostramos la información
            print(f"Modelo: {title}")
            print(f"Precio: {price}")
            print(f"Detalles: {', '.join(car_details)}")
            print(f"Enlace: {link}")
            print("-" * 50)

    else:
        print(f"Error al acceder a la web: {response.status_code}")