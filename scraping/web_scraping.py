import requests
from bs4 import BeautifulSoup 
from urllib.request import urlretrieve



def run():
    for i in range(1, 6):
        response = requests.get(f'https://xkcd.com/{i}')
        soup = BeautifulSoup(response.content, 'html.parser')
        image_container = soup.find(id='comic') #Busca el container 'comic'

        image_url = image_container.find('img')['src'] #Entrega la direccion de la imagen
        image_name = image_url.split('/')[-1] #Entrega lo que esta en la ultima diagona (/), que en este caso es el nombre de la imagen
        print(f'Descargando la imagen {image_name}')
        urlretrieve(f'https:{image_url}', image_name)


if __name__ =='__main__':
    run()