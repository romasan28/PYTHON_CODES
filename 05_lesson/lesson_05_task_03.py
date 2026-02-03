from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)


driver.get("https://the-internet.herokuapp.com/inputs")
search_str = driver.find_element(By.TAG_NAME, "input")
search_str.send_keys("Sky")
sleep(1)
search_str.clear()
sleep(1)
search_str.send_keys("Pro")
sleep(2)
driver.quit()


