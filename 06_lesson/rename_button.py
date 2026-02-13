from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(16)
driver.get("http://uitestingplayground.com/textinput")

snd = driver.find_element(By.CSS_SELECTOR, "#newButtonName")

snd.send_keys("SkyPro")
el = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
print(el.text)
el.click()
print(el.text)

driver.quit()