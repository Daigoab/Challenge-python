import requests
from bs4 import BeautifulSoup
import csv

url = "http://hojaleaks.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

images = soup.findAll("img", class_= ["css-eivff4","css-1082qq3"])

with (open("scrape.csv", "w", newline="")) as file:
    writer = csv.writer(file)
    writer.writerow(["images"])
    for image in images:
        writer.writerow([image["src"]])

headings = soup.findAll("h1", class_=["blog-article-card-title css-152kzsv","blog-article-card-title css-5wpeg9"])

with (open("header.csv", "w")) as file:
    writer = csv.writer(file)
    writer.writerow(["Headings"])
    for heading in headings:
        writer.writerow([heading.text])
