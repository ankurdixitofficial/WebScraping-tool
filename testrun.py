import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
import time

MAX_RETRIES = 3

def extract(page, state):
    userAgents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    ]
    url = f"https://dealer-locator.cars.tatamotors.com/location/{state}?cot=151&page={page}"
    headers = {'user-Agent': random.choice(userAgents)}
    
    for attempt in range(MAX_RETRIES):
        try:
            data_request = requests.get(url, headers=headers)
            soup = BeautifulSoup(data_request.content, 'html.parser')
            return soup
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve page {page} for state {state}. Retrying... ({attempt+1}/{MAX_RETRIES})")
            time.sleep(5)  # Wait before retrying
    raise Exception(f"Failed after {MAX_RETRIES} retries. Last error: {str(e)}")


def transform(soup,state):
    entrieslist = []
    divs = soup.find_all('div', class_='store-info-box')
    print(divs)
    for item in divs:
        title = item.find('a').text.strip()
        outlet_name = item.find('li', class_='outlet-address')
        address = ''
        city = ''
        phone = ''
        what3words = ''
        State = ''

        if outlet_name:
            info_text = outlet_name.find('div', class_='info-text')
            if info_text:
                address = info_text.find('span').text.strip()

        outlet_no = item.find('li', class_='outlet-phone')
        if outlet_no:
            info_text = outlet_no.find('div', class_='info-text')
            if info_text:
                phone = info_text.find('a').text.strip()

        outlet_what = item.find('li', class_='outlet-what3words')
        if outlet_what:
            info_text = outlet_what.find('div', class_='info-text')
            if info_text:
                what3words = info_text.find('a').text.strip()

        outlet_pin = item.find('li', class_='outlet-address')
        if outlet_pin:
            info_text = outlet_pin.find('div', class_='info-text')
            if info_text:
                address1 = info_text.find('span', class_='merge-in-next')
                if address1:
                    city = address1.find('span').text.strip()

        entries = {
            'title': title,
            'address': address,
            'city': city,
            'phone': phone,
            'what3words': what3words,
            'State': state
        }
        entrieslist.append(entries)

    return entrieslist

def main():
    entrieslist = []
    states = {
        1: 'Andaman-And-Nicobar-Islands', 2: 'Andhra-Pradesh', 3: 'Arunachal-Pradesh', 4: 'Assam', 5: 'Bihar',
        6: 'Chandigarh', 7: 'Chhattisgarh', 8: 'Dadra-And-Nagar-Haveli', 9: 'Delhi', 10: 'Goa', 11: 'Gujarat',
        12: 'Haryana', 13: 'Himachal-Pradesh', 14: 'Jammu-And-Kashmir', 15: 'Jharkhand', 16: 'Karnataka', 
        17: 'Kerala', 18: 'Ladakh', 19: 'Madhya-Pradesh', 20: 'Maharashtra', 21: 'Manipur', 22: 'Meghalaya',
        23: 'Mizoram', 24: 'Nagaland', 25: 'Odisha', 26: 'Puducherry', 27: 'Punjab', 28: 'Rajasthan', 
        29: 'Sikkim', 30: 'Tamil-Nadu', 31: 'Telangana', 32: 'Tripura', 33: 'Uttar-Pradesh', 34: 'Uttarakhand',
        35: 'West-Bengal'
    }

    for j in range(1, 36):
        state = states[j]
        for i in range(1, 50):
            soup = extract(i, state)
            entries = transform(soup,state)
            entrieslist.extend(entries)
    
    df = pd.DataFrame(entrieslist)
    print(df.head())
    df.to_csv('entries.csv', index=False)

if __name__ == "__main__":
    main()
