import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_fill_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение полей
    driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

    # Нажать Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверки цветов полей
    zip_code_field = driver.find_element(By.CSS_SELECTOR, "#zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class")

    success_fields = [
        "#first-name", "#last-name", "#address", "#e-mail",
        "#phone", "#city", "#country", "#job-position", "#company"
    ]
    for field in success_fields:
        element = driver.find_element(By.CSS_SELECTOR, field)
        assert "alert-success" in element.get_attribute("class")
