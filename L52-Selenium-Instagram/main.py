import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = "/Users/ajithvijayaraj/Development/chromedriver"
DRIVER = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
URL = "https://www.instagram.com/accounts/login/"
user_name = 'somemail@mail.com'
pawd = 'josemlfo-dowdj-lsse'
INSTA_PAGE = "being_sanely_absurd"


class InstaFollowers:
    def __init__(self):
        self.driver = DRIVER
        # self.login()

    def login(self):
        self.driver.get(URL)
        time.sleep(3)
        fb_login_finder = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[5]/button')
        fb_login_finder.click()
        time.sleep(5)
        user_inputs = self.driver.find_elements(by=By.CLASS_NAME, value='inputtext')
        user_inputs[0].send_keys(user_name)
        user_inputs[1].send_keys(pawd)
        time.sleep(2)
        login = self.driver.find_element(by=By.ID, value='loginbutton')
        login.click()

    def find_followers(self):
        # notif = self.driver.find_element(by=By.XPATH,
        #                                  value='/html/body/div[5]/div/div/div/div[3]/button[2]')
        # notif.click()
        # search_box = self.driver.find_element(by=By.XPATH,
        #                                       value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        # search_box.send_keys(INSTA_PAGE)
        # search_box.send_keys(Keys.ENTER)
        self.driver.get("https://www.instagram.com/londonappbrewery")
        # login_finder = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[3]/div/div/div/div/div/div[3]/div[1]/a')
        # login_finder.click()
        time.sleep(2)
        fb_login_finder = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[5]/button')
        fb_login_finder.click()
        user_inputs = self.driver.find_elements(by=By.CLASS_NAME, value='inputtext')
        user_inputs[0].send_keys(user_name)
        user_inputs[1].send_keys(pawd)
        time.sleep(2)
        login = self.driver.find_element(by=By.ID, value='loginbutton')
        login.click()
        time.sleep(15)

        followers = self.driver.find_element(by=By.XPATH,
                                             value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(5)

        modal = self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div/div/div/div[2]')
        for i in range(20):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        for i in range(2, 20):
            button = self.driver.find_element(by=By.XPATH, value=f'/html/body/div[6]/div/div/div/div[2]/ul/div/li[{i}]/div/div[2]/button')
            print(button.text)


ifollow = InstaFollowers()
# ifollow.login()
ifollow.find_followers()
ifollow.follow()
