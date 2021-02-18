import requests
from bs4 import BeautifulSoup
import pandas as pd



base_url = 'https://books.toscrape.com/catalogue/'

product_links = []

for x in range(1, 51):
    r = requests.get(f'https://books.toscrape.com/catalogue/page-{x}.html')
    soup = BeautifulSoup(r.content, 'lxml')

    product_list = soup.find_all('div', class_='image_container')
    for image_container in product_list:
        for link in image_container.find_all('a', href=True):
            product_links.append(base_url + link['href'])

book_list = []
for link in product_links:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')

    title = soup.find('h1').text
    category = soup.find('ul', class_='breadcrumb').find_all('li')[2].text.strip()
    number_available = soup.find('table', class_='table table-striped').find_all('td')[5].text
    review_rating = soup.find('div', class_='col-sm-6 product_main').find_all('p')[2]['class'][1]
    price_including_tax = soup.find('table', class_='table table-striped').find_all('td')[2].text
    price_excluding_tax = soup.find('table', class_='table table-striped').find_all('td')[3].text
    universal_product_code = soup.find('table', class_='table table-striped').find_all('td')[0].text
    image_url = soup.find('div', class_='item active').find('img')['src'].replace('../../',
                                                                                  'http://books.toscrape.com/')
    try:
        product_description = soup.find('p', class_='').text.strip()
    except:
        product_description = 'No description'

    book_details = {'Title': title, 'Category': category, 'Price Inc Tax': price_including_tax,
                    'Price Exc Tax:': price_excluding_tax, 'Number Available': number_available,
                    'Review Rating': review_rating, 'Description': product_description,
                    'Universal Product Code': universal_product_code, 'Image Url': image_url,
                    }
    book_list.append(book_details)

df = pd.DataFrame(book_list)
df.to_csv('Scrape_book.csv')
data = pd.read_csv('Scrape_book.csv')
data_category_range = data['Category'].unique()
data_category_range = data_category_range.tolist()

for i, value in enumerate(data_category_range):
    data[data['Category'] == value].to_csv(r'Category_'+str(value)+r'.csv', index=False, na_rep='N/A')
