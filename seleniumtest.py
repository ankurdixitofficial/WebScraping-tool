import requests
import random
import pandas as pd
import time
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

userAgents=[
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
]
options= webdriver.ChromeOptions()
options.add_argument("--headless")
options.page_load_strategies= "none"
data_request = Chrome(options=options)
data_request.implicitly_wait(5) 

data_request = requests.get('https://dealer-locator.cars.tatamotors.com/location/delhi?cot=151&v=1.123', headers={'user-Agent': random.choice(userAgents)})

#data_request.execute_script("window.scrollTo(0, document.body.scrollHeight);")

box = data_request.find_element(By.CSS_SELECTOR,'div[class="store-info-box"]')
print(box.text)