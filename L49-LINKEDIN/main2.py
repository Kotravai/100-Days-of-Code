import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
chrome_driver_path = "/Users/ajithvijayaraj/Development/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

url = "https://www.linkedin.com/login?emailAddress=&fromSignIn=&trk=public_jobs_conversion-modal-signin&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3Ff_AL%3Dtrue%26f_JT%3DF%26f_TPR%3Dr2592000%26geoId%3D105214831%26keywords%3Dinside%2520sales%26location%3DBengaluru%252C%2520Karnataka%252C%2520India"
driver.get(url)

MAIL = "somemail@gmail.com"
PWD = "mksoevliwod;"

user_name = driver.find_element(by=By.ID, value="username")
user_name.send_keys(MAIL)

pawd = driver.find_element(by=By.ID, value="password")
pawd.send_keys(PWD)

login_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
login_button.click()

job_card = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
time.sleep(2)

for i in job_card:
    i.click()
    time.sleep(2)
    apply_button = driver.find_element(by=By.CLASS_NAME, value="jobs-apply-button")
    if apply_button.text == 'Easy Apply':
        apply_button.click()
        time.sleep(2)
        for _ in range(2):
            try:
                next_button1= driver.find_elements(by=By.CSS_SELECTOR, value="footer button")
                next_button1[-1].click()
                time.sleep(3)
            except IndexError:
                dismiss = driver.find_element(by=By.CLASS_NAME, value="mercado-match")
                dismiss.click()
                break
        next_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if next_button.text == "Submit Application":
            next_button.click()
            time.sleep(2)
        else:
            print("Complex application. Not submitted")
            dismiss = driver.find_element(by=By.CLASS_NAME, value="mercado-match")
            dismiss.click()
            time.sleep(1)
            discard = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
            discard.click()

