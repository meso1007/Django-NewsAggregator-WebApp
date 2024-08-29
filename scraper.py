import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")

articles = soup.find_all('h2', class_='sc-4fedabc7-3 dsoipF')
articles += soup.find_all('h2', class_='sc-4fedabc7-3 zTZri')

print(f"Found {len(articles)} articles")   #It show how many article it found

news_data = []  #Empty Array
for article in articles:
    title = article.get_text()
    link = article.find_parent('a')['href']
    if not link.startswith('http'):
        link = 'https://www.bbc.com' + link
    news_data.append({
        "title": title,
        "link": link
    })

for news in news_data:
    print(f"Title: {news['title']}")
    print(f"Link: {news['link']}\n")
