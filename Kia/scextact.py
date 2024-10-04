import requests
from bs4 import BeautifulSoup
import random
import time

MAX_RETRIES = 3

def extract():
    userAgents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    ]
    url = f"https://www.kia.com/in/buy/find-a-dealer/result.html?state=AP&city=S99"
    headers = {'user-Agent': random.choice(userAgents)}
    
    for attempt in range(MAX_RETRIES):
        try:
            data_request = requests.get(url, headers=headers)
            soup = BeautifulSoup(data_request.content, 'html.parser')
            return soup
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve page. Retrying... ({attempt+1}/{MAX_RETRIES})")
            time.sleep(5)  # Wait before retrying
    raise Exception(f"Failed after {MAX_RETRIES} retries. Last error: {str(e)}")

def transform(soup):
    divs = soup.find_all('div', class_='dealer-list-wrap mt-sm')
    for div in divs:
        if div:
            outlet_name = div.find_all('ul', class_='dealer-list mt-sm  mb-sm')
            for outlet_n in outlet_name:
                info_text = outlet_n.find('li', class_='dealer-info is-active')
                if info_text:
                    print(info_text.text)
                    address = info_text.find('div', class_='dealer-info-pad')
                    if address:
                        print(address.text)
                        content = address.find('a', class_='dealer-location-link')
                        if content:
                            print(content.text)
                        

if __name__ == "__main__":
    soup = extract()
    transform(soup)
