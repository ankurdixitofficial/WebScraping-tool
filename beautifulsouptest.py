from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup

# URL of the target page
url = "https://dealer-locator.cars.tatamotors.com/location/delhi?cot=151&v=1.123&page=1"

# Path to your Edge WebDriver executable
edgedriver_path = 'C:\\path\\to\\msedgedriver.exe'  # Update this path to where your msedgedriver executable is located

# Setting up Edge options for headless mode
options = Options()
options.add_argument("--headless")
options.page_load_strategy = "eager"  # Eager loading strategy to wait for DOMContentLoaded event

# Initialize Edge WebDriver
driver = webdriver.Edge(executable_path=edgedriver_path, options=options)
driver.get(url)

# Explicit wait for the store-info-box elements to be present
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'store-info-box')))

# Get the page source and parse it with BeautifulSoup
html = driver.page_source

# List to store company data
companies = []

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all elements with the class 'store-info-box'
for element in soup.find_all('div', class_='store-info-box'):
    print("store-info-box found")
    # Navigate through the nested structure to find the specific elements
    outlet_detail = element.find('ul', class_='list-unstyled outlet-detail first')
    if outlet_detail:
        print("outlet-detail found")
        outlet_name = outlet_detail.find('li', class_='outlet-name')
        if outlet_name:
            print("outlet-name found")
            info_text = outlet_name.find('div', class_='info-text')
            if info_text:
                print("info-text found")
                cname = info_text.find('a').text
                print(f"Company Name: {cname}")
                companies.append([cname])  # Fixed the variable name here

# Close the WebDriver
driver.quit()

# Convert the list to a DataFrame and save as CSV
df = pd.DataFrame(companies, columns=["Company Name"])
df.to_csv("Companies.csv", index=False)

print("Data extraction complete and saved to Companies.csv")
