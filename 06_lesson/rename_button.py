from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

snd = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
snd.send_keys("SkyPro")

el = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
print(el.text)
el.click()

wait = WebDriverWait(driver, 12)
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro"))

print(el.text)

driver.quit()
