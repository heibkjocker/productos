import requests
from bs4 import BeautifulSoup


def conservar_numeros(lista):
    lista_de_numeros = [c for c in lista if c.isnumeric()]
    return lista_de_numeros
def get_productos_elcomercioElectrico():
    response = requests.get("https://comercioelectrico.com/index.php/page/1/?s&post_type=product")
    soup = BeautifulSoup(response.content, "html.parser")
    paginas = soup.find_all('a', class_="page-numbers")
    lista_paginas = []
    for p in paginas:
        lista_paginas.append(p.get_text(strip=True))
    solo_numeros = conservar_numeros(lista_paginas)
    ultima_pagina = solo_numeros[-1]
    lista = []
    lista_precios = []

    for i in range(0, int(ultima_pagina)):
        URL = f"https://comercioelectrico.com/index.php/page/{i}/?s&post_type=product"
        print(URL)
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, "html.parser")

        productos = soup.find_all('h2', class_="woocommerce-loop-product__title")
        precios = soup.find_all('bdi')


        for item in productos:
            lista.append(item.get_text(strip=True))
        for p in precios:
            lista_precios.append(p.get_text(strip=True))

    return lista, lista_precios

if __name__ == "__main__":
    etiquetas, precios = get_productos_elcomercioElectrico()
    print(etiquetas)
    print(precios)

