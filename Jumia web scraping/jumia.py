import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.jumia.co.ke/"

products = []

for x in range (1, 6):
    response = requests.get(f'https://www.jumia.co.ke/mlp-free-delivery/?page={x}#catalog-listing')
    soup = BeautifulSoup(response.content, "html.parser")
    productlist = soup.find_all('div', class_= 'itm col')
    for item in productlist:
        for link in item.find_all('a', href=True):
            products.append(url + link['href'])

products_list = []

for link in products:
    result = requests.get(link)
    soup = BeautifulSoup(result.content, 'html.parser')
    name = soup.find('h1', class_='-fs20 -pts -pbxs').text.strip()
    price = soup.find('span', class_='-b -ltr -tal -fs24').text.strip()

    try:
        rating = soup.find('div', class_='stars _s _al').text.strip()
    except:
        rating = 'no rating'
    try:
        no_of_ratings = soup.find('a', class_='-plxs _more').text.strip()
    except:
        no_of_ratings = 'unavailable'
    try:
        no_of_reviews = soup.find('h2', class_='-fs14 -m -upp -ptm').text.strip()
    except:
        no_of_reviews = 'unavailable'

    product = {
        'name' : name,
        'rating' : rating,
        'price': price,
        'no_of_ratings' : no_of_ratings,
        'no_of_reviews' : no_of_reviews
    }

    products_list.append(product)

    print(product)

with open('products.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=products[0].keys())
    writer.writeheader()
    for product in products:
        writer.writerow(product)       
