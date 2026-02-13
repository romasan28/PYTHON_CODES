from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

#el = driver.find_element(By.CSS_SELECTOR, "p#text")
wait = WebDriverWait(driver, 12)
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.lead"), "Done" ))
print(driver.find_element(By.CSS_SELECTOR, "p.lead").text)

lst = driver.find_elements(By.CSS_SELECTOR, "img")
imeg = lst[3]
txt = imeg.get_attribute("src")
print(txt)

driver.quit()