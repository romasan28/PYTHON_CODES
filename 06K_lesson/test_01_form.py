import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture
def driver():
    driver = webdriver.Edge()
    yield driver
    driver.quit()

def test_data_types_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Ждём появления первого поля
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "first-name"))
    )

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    # Заполнение формы
    for name, value in fields.items():
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.NAME, name))
        )
        element.clear()
        if value:
            element.send_keys(value)

    # Отправка (нажатие submit)
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Проверка результата для zip-code (красный)
    zip_result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "zip-code"))
    )
    assert "alert-danger" in zip_result.get_attribute("class"), \
        "Поле Zip code должно быть красным (alert-danger)"

    # Проверка остальных полей (зелёные)
    for name in fields:
        if name == "zip-code":
            continue
        result_elem = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, name))
        )
        assert "alert-success" in result_elem.get_attribute("class"), \
            f"Поле {name} должно быть зелёным (alert-success)"