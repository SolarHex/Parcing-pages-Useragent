import requests
from bs4 import BeautifulSoup


url = 'https://www.ozon.ru/product/fitnes-braslet-honor-band-5-chernyy-155530932/?asb=Z%252FXjEU7FQ%252FIpL%252Fv0e01L%252Fk85H7CcVEYEN0j6A5AJS7A%253D&asb2=knL4SB_1AwGpF7g8ixwbMQp1zrmPnLTEIbTJL5sVmcujeitseEcqDRDc_ZWb6o0kB234GhiwY31ySDgRKgH9uQ&sh=KRgsUrXz'
def get_comments():
    
    
    r = requests.get(url=url)
    return r

def get_content(html):
    soup = BeautifulSoup(html, "lxml")
    
    page = soup.find_all(class_='gb4')
    print(page)
    
    comment = soup.find('span',class_='e2u6')
    
    print(comment)
    
#   for iteam in page:
 #       item_text = iteam.text
 #       comment = iteam.find('span',class_='e2u6').text.strip()
 #       
  #      print({comment} | {item_text})

get_comments()

def parse():
    html = get_comments(url)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('error')
    
parse()