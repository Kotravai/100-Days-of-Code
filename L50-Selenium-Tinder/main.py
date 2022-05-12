import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "/Users/ajithvijayaraj/Development/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

url = "https://tinder.com"
user_name = 'koilnie342'
pawd = 'Kecsis-syjmyr-2jikdo'
driver.get(url)

time.sleep(2)
login_button = driver.find_elements(by=By.CSS_SELECTOR, value='header a')
login_button[-1].click()

options = driver.find_elements(by=By.CSS_SELECTOR, value="button")
for i in options:
    if i.text == "I accept":
        i.click()
        break

wait = WebDriverWait(driver, 10)
original_window = driver.current_window_handle
assert len(driver.window_handles) == 1
time.sleep(2)

options = driver.find_elements(by=By.CSS_SELECTOR, value="button")
for i in options:
    if "options" in i.text or "FACEBOOK" in (i.text):
        i.click()
        break

wait.until(EC.number_of_windows_to_be(2))

for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        facebook_login = driver.find_elements(by=By.CLASS_NAME, value='inputtext')
        facebook_login[0].send_keys(user_name)
        facebook_login[1].send_keys(pawd)
        login = driver.find_element(by=By.CLASS_NAME, value="uiButton")
        login.click()

wait.until(EC.number_of_windows_to_be(1))
driver.switch_to.window(original_window)
time.sleep(6)

location = driver.find_element(by=By.XPATH, value='//*[@id="q1954245907"]/div/div/div/div/div[3]/button[1]')
location.click()
time.sleep(5)

notif = driver.find_element(by=By.XPATH,value='//*[@id="q1954245907"]/div/div/div/div/div[3]/button[2]')
notif.click()
time.sleep(11)

like = driver.find_elements(by=By.CSS_SELECTOR, value='span')
for _ in range(3):
    for i in like:
        if i.text == 'LIKE':
            i.click()
            time.sleep(3)
            break







