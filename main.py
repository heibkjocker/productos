import requests
from bs4 import BeautifulSoup

URL = "https://comercioelectrico.com/index.php/page/1/?s&post_type=product"

def get_productos_elcomercioElectrico():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    productos = soup.find_all('h2', class_="woocommerce-loop-product__title")
    precios = soup.find_all('bdi')
    paginas = soup.find_all('nav', class_="woocommerce-pagination")
    lista = []
    lista_precios = []
    lista_paginas = []
    for item in productos:
        lista.append(item.get_text(strip=True))
    for i in precios:
        lista_precios.append(i.get_text(strip=True))
    return lista, lista_precios

if __name__ == "__main__":
    print(get_productos_elcomercioElectrico())
