import requests
from bs4 import BeautifulSoup

URL = f"https://www.avito.ru/moskva/kvartiry/sdam/posutochno/-ASgBAgICAkSSA8gQ8AeSUg?cd=1&f=ASgBAgECAkSSA8gQ8AeSUgFFqC0feyJmcm9tIjoyMDIxMTIwMywidG8iOjIwMjExMjA0fQ"
HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.1.932 Yowser/2.5 Safari/537.36'
}


def get_html(url,params=None):
    r = requests.get(url, headers=HEADERS,params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    #apartaments = soup.find('div',class_='iva-item-priceStep-QN8Kl').text.strip()
    apartaments = soup.find_all('div',{'class' : 'iva-item-titleStep-_CxvN'})
    
    print(apartaments)
    
    
def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('error')
    
parse()