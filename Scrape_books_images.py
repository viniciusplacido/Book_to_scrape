import requests
from bs4 import BeautifulSoup
import re


base_url = 'https://books.toscrape.com/catalogue/'

product_links = []

for x in range(1, 51):
    r = requests.get(f'https://books.toscrape.com/catalogue/page-{x}.html')
    soup = BeautifulSoup(r.text, 'html.parser')

    product_list = soup.find_all('div', class_='image_container')
    for image_container in product_list:
        for link in image_container.find_all('a', href=True):
            product_links.append(base_url + link['href'])

book_list = []
for link in product_links:
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')

    name = soup.find('div', class_='item active').find('img')['alt']
    name1 = re.sub("[^0-9a-zA-Z']+", ' ', name)
    image_url = soup.find('div', class_='item active').find('img')['src'].replace('../../',
                                                                                  'http://books.toscrape.com/')
    with open(name1[0:50] + '.jpg', 'wb') as f:
        im = requests.get(image_url)
        f.write(im.content)
