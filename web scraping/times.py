import requests
from bs4 import BeautifulSoup
import csv
# Send GET request to New York Times website
url = "https://www.nytimes.com/"
response = requests.get(url)
# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
# Find HTML elements that contain the article titles and descriptions
articles = soup.find_all("article")
# Create a list to store the article data
article_data = []
# Loop through the first 10 articles and store their title and description in a dictionary
for article in articles[:10]:
    title = article.find("h2").text.strip()
    description = article.find("p").text.strip()
    article_data.append({"title": title, "description": description})
# Write the article data to a CSV file
with open("times.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "description"])
    writer.writeheader()
    writer.writerows(article_data)