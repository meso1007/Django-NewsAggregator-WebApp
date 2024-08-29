import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_news_data():
    URL = "https://www.bbc.com/news"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = soup.find_all('h2', class_='sc-4fedabc7-3 dsoipF')
    articles += soup.find_all('h2', class_='sc-4fedabc7-3 zTZri')

    news_data = []
    for article in articles:
        title = article.get_text()
        link = article.find_parent('a')['href']
        divParent = article.find_parent("div", {"data-testid": "card-text-wrapper"})
        des = divParent.find("p", {"data-testid": "card-description"}).get_text() if divParent else None
        if not link.startswith('http'):
            link = 'https://www.bbc.com' + link
        
        image_url = get_article_image(link)
        date = get_article_date(link)
        
        news_item = {
            "title": title,
            "link": link,
            "des": des,
            "date": date,
            "image": image_url
        }
        news_data.append(news_item)
    
    # 最初の要素を取り出して最後に追加
    if news_data:
        reversed_news_data = news_data[1:] + [news_data[0]]
    else:
        reversed_news_data = []

    return {
        'news_data': news_data,
        'reversed_news_data': reversed_news_data 
    }

def get_article_image(article_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(article_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    img_tags = soup.find_all('img')
    highest_resolution_url = None

    for img_tag in img_tags:
        if 'srcset' in img_tag.attrs:
            srcset_values = img_tag['srcset'].split(',')
            srcset_values = [srcset.strip().split(' ') for srcset in srcset_values]
            srcset_values.sort(key=lambda x: int(x[1].replace('w', '')), reverse=True)  # Sort by width in descending order
            img_url = srcset_values[0][0]
            if not img_url.startswith('http'):
                img_url = urljoin(article_url, img_url)
            highest_resolution_url = img_url
            break
        elif 'src' in img_tag.attrs:
            img_url = img_tag['src']
            if not img_url.startswith('http'):
                img_url = urljoin(article_url, img_url)
            highest_resolution_url = img_url

    return highest_resolution_url

def get_article_date(article_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(article_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    time_tags = soup.find_all('time')
    if time_tags:
        return time_tags[0].get_text(strip=True)
    
    return 'Date not found'
