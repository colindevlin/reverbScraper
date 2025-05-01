from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

website = 'https://reverb.com/'
path = '/Users/colindevlin/IdeaProjects/scraperz/chromedriver/chromedriver'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "site-search__controls__input"))
)

input_element = driver.find_element(By.CLASS_NAME, "site-search__controls__input")
input_element.clear()
input_element.send_keys("PRS Silver Sky SE evergreen" + Keys.ENTER)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "rc-listing-grid__item"))
)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "rc-listing-card__title"))
)

listings = driver.find_elements(By.CLASS_NAME, "rc-listing-grid__item")

guitars = []

for listing in listings:
    try:
        title_element = listing.find_element(By.CLASS_NAME, "rc-listing-card__title")
        price_element = listing.find_element(By.CLASS_NAME, "rc-listing-card__price")
        title = title_element.text
        price = price_element.text

        guitars.append({
            'title': title,
            'price': price
        })

    except Exception as e:
        print(f"Skipping a listing due to error: {e}")

driver.quit()

for guitar in guitars:
    print(f"{guitar['title']} - {guitar['price']}")