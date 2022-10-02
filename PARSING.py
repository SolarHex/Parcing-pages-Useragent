import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

def get_news():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.1.932 Yowser/2.5 Safari/537.36'
    }
    
    url = 'https://www.securitylab.ru/news/'
    
    r = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(r.text,'lxml')
    
    article_cards = soup.find_all('a', class_='article-card')
    
    for article in article_cards:
        article_title = article.find('h2',class_='article-card-title').text.strip()
        art_dec = article.find('p').text.strip()
        article_url = f'https://www.securitylab.ru{article.get("href")}'
        
        print({article_title}  |  {article_url})
        
get_news()