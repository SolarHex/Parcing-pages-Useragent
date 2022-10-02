import requests
from bs4 import BeautifulSoup

URL = 'https://www.securitylab.ru/'
HEADERS =  {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.1.932 Yowser/2.5 Safari/537.36'
    }


def get_html(url,params=None):
    r = requests.get(url, headers=HEADERS,params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div',class_='article-card')
    #print(items)
    
    for i in items:
        revol = soup.find_all('h4',class_='article-card-title')
        print(revol)

    
   # print(soup.get_text())
    
def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('error')
    
parse()