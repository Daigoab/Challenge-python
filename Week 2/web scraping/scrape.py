import requests
from bs4 import BeautifulSoup
import csv

url = "http://hojaleaks.com/"

response = requests.get(url)

doc = BeautifulSoup(response.text, "html.parser")

soup = BeautifulSoup(response.content, "html.parser")

images = soup.findAll("img", class_= ["css-eivff4","css-1082qq3"])

with (open("image.csv", "w", newline="")) as file:
    writer = csv.writer(file)
    writer.writerow(["images"])
    for image in images:
        writer.writerow([image["src"]])

headings = doc.find_all("h1", class_ = ["blog-article-card-title css-152kzsv","blog-article-card-title css-5wpeg9"])
summaries = doc.find_all("p", class_="css-ko0c54")

for heading in headings:
    print(heading.text)

for summary in summaries:
    print(summary.text)

with open("data.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Heading", "Summary"])

    for heading, summary in zip(headings, summaries):
        writer.writerow([heading.text, summary.text])

