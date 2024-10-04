import requests
from bs4 import BeautifulSoup
import random

userAgents=[
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
]

data_request = requests.get('https://dealer-locator.cars.tatamotors.com/location/delhi?cot=151&v=1.123', headers={'user-Agent': random.choice(userAgents)})


html_text = data_request.text
soup = BeautifulSoup(html_text, 'html.parser' )
#print(soup)
for element in soup.find_all('div', class_='store-info-box'):
        
        outlet_detail = element.find('ul', class_='list-unstyled outlet-detail first')
        print(outlet_detail)
        if outlet_detail:
            #print("outlet-detail found")
            outlet_name = outlet_detail.find('li', class_='outlet-name')
            if outlet_name:
                #print("outlet-name found")
                info_text = outlet_name.find('div', class_='info-text')
                if info_text:
                    #print("info-text found")
                    cname = info_text.find('a').text
                    print(cname)
    
        if outlet_detail:
            #print("outlet-detail found")
            outlet_name = outlet_detail.find('li', class_='outlet-address')
            if outlet_name:
                #print("outlet-address found")
                info_text = outlet_name.find('div', class_='info-text')
                if info_text:
                    #print("info-text found")
                    cname = info_text.find('span').text
                    print(cname)
            #print("outlet-detail found")
            outlet_name = outlet_detail.find('li', class_='outlet-phone')
            if outlet_name:
                #print("outlet-phone found")
                info_text = outlet_name.find('div', class_='info-text')
                if info_text:
                    #print("info-text found")
                    cname = info_text.find('a').text
                    print(cname)
            #print("outlet-detail found")
            outlet_name = outlet_detail.find('li', class_='outlet-what3words')
            if outlet_name:
                #print("outlet-name found")
                info_text = outlet_name.find('div', class_='info-text')
                if info_text:
                    #print("info-text found")
                    cname = info_text.find('a').text
                    print(cname)
            #print("outlet-detail found")
            outlet_name = outlet_detail.find('li', class_='outlet-address')
            if outlet_name:
                #print("outlet-name found")
                info_text = outlet_name.find('div', class_='merge-in-next')
                if info_text:
                    #print("info-text found")
                    cname = info_text.find('a').text
                    print(cname)
   
                
                
    