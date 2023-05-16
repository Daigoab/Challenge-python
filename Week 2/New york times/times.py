import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.nytimes.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

articles = soup.find_all( class_= "css-xdandi")

article_data = []

with open("times.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['title', "description"])

    for article in articles[:10]:
        title = article.find('h3', class_='css-on971e').text.strip()
        description = article.find('p', class_='css-9lwb1u').text.strip()
        if title is not None and description is not None:
            article_data.append({'title': title, 'description': description})
        print(article)
        writer.writerow([title, description])
