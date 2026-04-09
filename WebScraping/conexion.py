import requests
from bs4 import BeautifulSoup

def conexion(url,user_agent):
    url = url
    cabecera = {
        "User-Agent": user_agent}
    path = requests.get(url, headers=cabecera)

    if path.status_code == 200:
        soup = BeautifulSoup(path.text, 'html.parser')
        print(path.status_code)
        print('La Conexion a sido un Exito')
        return soup
    else:
        return print('Conexion Fallida ')