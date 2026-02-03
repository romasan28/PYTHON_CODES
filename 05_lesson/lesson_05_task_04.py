from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)


driver.get("https://the-internet.herokuapp.com/login")
login = driver.find_element(By.XPATH, "//input[@name ='username']")
login.send_keys("tomsmith")
password = driver.find_element(By.XPATH, "//input[@type ='password' and @name ='password']")
password.send_keys("SuperSecretPassword!")
btn_login = driver.find_element(By.XPATH, "//button[@class ='radius' and @type ='submit']")
btn_login.click()
green_message = driver.find_element(By.XPATH, "//div[@id='flash']")
print(green_message.text)

driver.quit()