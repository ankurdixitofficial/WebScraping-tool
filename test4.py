import requests
from bs4 import BeautifulSoup
import random
import pandas as pd

def extract(page):
    userAgents=[
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    ]
    url=f"https://dealer-locator.cars.tatamotors.com/location/Delhi?cot=151&page={page}"

    data_request = requests.get(url, headers={'user-Agent': random.choice(userAgents)})
    soup = BeautifulSoup(data_request.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_='store-info-box')
    for item in divs:
        title = item.find('a').text.strip()
        outlet_name = item.find('li', class_='outlet-address')
        address=''
        if outlet_name:
            #print("outlet-address found")
            info_text = outlet_name.find('div', class_='info-text')
            if info_text:
                #print("info-text found")
                address = info_text.find('span').text.strip()
                #print(cname)
        outlet_no = item.find('li', class_='outlet-phone')
        phone=''
        if outlet_no:
                info_text = outlet_no.find('div', class_='info-text')
                if info_text:
                    phone = info_text.find('a').text
                    #print(cname)
        outlet_what = item.find('li', class_='outlet-what3words')
        what3words=''
        if outlet_what:
            #print("outlet-name found")
            info_text = outlet_what.find('div', class_='info-text')
            if info_text:
                #print("info-text found")
                what3words = info_text.find('a').text
        
        outlet_pin = item.find('li', class_='outlet-address')
        city=''
        if outlet_pin:
            #print("outlet-address found")
            info_text = outlet_pin.find('div', class_='info-text')
            if info_text:
                #print("info-text found")
                address1 = info_text.find('span', class_='merge-in-next')
                if address1:
                    city = address1.find('span')
                #print(cname)
        entries = {
            'title': title,
            'address': address,
            'city': city.text,
            'phone': phone,
            'what3words': what3words
        }
        entrieslist.append(entries)
    return

entrieslist=[]


for i in range(1,4):
    
    c=extract(i)
    transform(c)    
    
print(entrieslist)

df = pd.DataFrame(entrieslist)
print(df.head())
df.to_csv('entries.csv')
