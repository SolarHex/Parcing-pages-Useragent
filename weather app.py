import requests
from bs4 import BeautifulSoup
import json

def get_weather():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.1.932 Yowser/2.5 Safari/537.36"
    }
    
    url = 'https://www.avito.ru/moskva/kvartiry/prodam-ASgBAgICAUSSA8YQ?cd=1'

    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    
    cards = soup.find_all('div',class_='iva-item-body-R_Q9c')
    #print(cards)
    
    for data in cards:
        time_is = data.find('div',class_='iva-item-titleStep-_CxvN').text.strip()
        degrees = data.find('span',class_='price-price-BQkOZ').text.strip()

        
        print({time_is} | {degrees})
        
        Apartaments = {
            'apartament is:' : time_is,
            'Cost is :' : degrees
            
        }
        
    with open('Apartaments.json','w') as f:
        json.dump(Apartaments,f,indent=4,ensure_ascii=False)
        

def main():
    get_weather()
    
    
if __name__ == "__main__":
    main()