import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

def get_news():#href="/news/527174.php"
    headersio = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.1.932 Yowser/2.5 Safari/537.36'
    }
    
    urlio = 'https://www.securitylab.ru/news/'
    
    r = requests.get(url=urlio, headers=headersio)
    
    soup = BeautifulSoup(r.text, 'lxml')
    article_cards = soup.find_all('div', Class='article-card')
    
    for i in article_cards:
        ar_title = i.find('h4', Class='article-card-title').text.strip()
        ar_opisanie = i.find('p').text.strip()
        ar_href = f'https://www.securitylab.ru{i.get("href")}'
        
        ar_time = i.find("time").get('datetime')
        
        print(f"{ar_title} {ar_opisanie} {ar_href} {ar_time}")
        
get_news()