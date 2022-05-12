import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

FORM_LINK = "https://forms.gle/gt16g5Y4VZfRp2qt8"
ZILLOW_URL = "http://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.63314284277344%2C%22east%22%3A-122.15935744238281%2C%22south%22%3A37.61147499616678%2C%22north%22%3A37.990714765631296%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

# response = requests.get(ZILLOW_URL)
# contents = response.text
# soup = BeautifulSoup(contents, "html.parser")
# address = []
# rent = []
# property_link = []
# address = [add.text for add in soup.find_all(name='ul li')]
# print(address)

chrome_driver_path = "/Users/ajithvijayaraj/Development/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get(ZILLOW_URL)

whole_data = driver.find_elements(by=By.CLASS_NAME, value="list-card-addr")
address = [link.text for link in whole_data]
links_all = driver.find_elements(by=By.CLASS_NAME, value="list-card-link")
links = [link.get_attribute('href') for link in links_all]

print(links)
print(address)

price_all = driver.find_elements(by=By.CLASS_NAME, value="list-card-price")
prices = [add.text for add in price_all]
print(prices)

def form_filler(links, prices, address):
    driver.get(FORM_LINK)
    time.sleep(20)
    for i in range(len(prices)):
        add = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        add.send_keys(address[i])
        time.sleep(1)
        pri= driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        pri.send_keys(prices[i])
        time.sleep(2)
        link = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link.send_keys(links[2*i])
        time.sleep(2)
        submit=driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submit.click()
        time.sleep(3)
        new_entry = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        new_entry.click()
        time.sleep(4)

form_filler(links,prices,address)


