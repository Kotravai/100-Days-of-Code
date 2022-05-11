from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/Users/ajithvijayaraj/Development/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("https://www.python.org/")

# price = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr[1]/td[2]/span[1]/span[1]')
event_names = driver.find_elements(by=By.CLASS_NAME, value="medium-widget.event-widget li a")
event_times = driver.find_elements(by=By.CLASS_NAME, value="medium-widget.event-widget time")
# print(event_names)

events = {}

for n in range(len(event_names)):
    events[n] = {
        "name": event_names[n].text,
        "date": event_times[n].text
    }

print(events)

# k = price.text.split('\n')
#
# event_set = k[2:]
# print(event_set)
#
# name = []
# date = []
#
# for i in range(len(event_set)):
#     if i % 2 == 0:
#         date.append(event_set[i])
#     else:
#         name.append(event_set[i])
#
# event_dict = {}
#
# final_dict = {event_dict[i]:{'name': name[i], 'date': date[i]} for i in range(len(event_set))}
#
# print(event_dict)
# print(final_dict)


driver.quit()
