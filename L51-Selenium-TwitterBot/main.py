import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "/Users/ajithvijayaraj/Development/chromedriver"
driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
PROMISED_DOWN = 50
PROMISED_UP = 5
TWITTER_EMAIL = 'somemail@ymail.com'
TWITTER_PASSWORD = 'asie_sliemvd'


class InternetSpeedTwBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
        self.up = PROMISED_UP
        self.down = PROMISED_DOWN

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        time.sleep(20)
        go_button = self.driver.find_element(by=By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        # print(go_button.text)
        go_button.click()
        time.sleep(80)
        down = self.driver.find_element(by=By.XPATH,
                                        value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        up = self.driver.find_element(by=By.XPATH,
                                      value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        return [down.text, up.text]

    def tweet_at_provider(self):
        # down = self.get_internet_speed()[0]
        down = 15
        # up = self.get_internet_speed()[1]
        self.driver.get('https://twitter.com/i/flow/login')
        mail = self.driver.find_element(by=By.CSS_SELECTOR,
                                        value='input')
        mail.send_keys(TWITTER_EMAIL)
        mail.send_keys(Keys.ENTER)
        # next_button = self.driver.find_element(by=By.XPATH,
        #                                        value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div')
        # next_button.click()
        time.sleep(5)
        password = self.driver.find_element(by=By.XPATH,
                                            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_button = self.driver.find_element(by=By.XPATH,
                                                value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        tweet_button.click()
        if down < PROMISED_DOWN:
            type_area = self.driver.find_element(by=By.XPATH,
                                                 value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div')
            type_area.send_keys(f"@Jio The internet speed is {down}")


bot = InternetSpeedTwBot()
bot.tweet_at_provider()
