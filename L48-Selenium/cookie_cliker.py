from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = "/Users/ajithvijayaraj/Development/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("http://orteil.dashnet.org/experiments/cookie/")
game_end = time.time()+60
power_up_time = time.time() + 5

cookie = driver.find_element(by=By.ID, value="cookie")

while True:
    if time.time() > game_end:
        speed = driver.find_element(by=By.ID, value="cps")
        print(f"The {speed.text}")
        break
    else:
        cookie.click()
        if int(time.time()) == int(power_up_time):
            right_panel = driver.find_elements(by=By.CSS_SELECTOR, value="#rightPanel b")
            full_panel = [right_panel[i].text.split('-')[0].replace(" ", "") for i in range(len(right_panel) - 1)]
            power_up = [right_panel[i].text.split('-')[1].replace(",", "") for i in range(len(right_panel)-1)]
            for i in reversed(range(len(power_up))):
                score = driver.find_element(by=By.ID, value="money")
                if int(score.text) > int(power_up[i]):
                    add_on = driver.find_element(by=By.ID, value=f"buy{full_panel[i]}")
                    add_on.click()
                    power_up_time += 5


