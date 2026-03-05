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


def test_slow_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")
    assert delay_input.get_attribute("value") == "45", \
           "Задержка не установилась"

    wait_click = WebDriverWait(driver, 10)

    btn_7 = wait_click.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[text()='7' and contains(@class, 'btn')]"
            )
        )
    )
    btn_7.click()

    btn_plus = wait_click.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[text()='+' and contains(@class, 'btn')]"
            )
        )
    )
    btn_plus.click()

    btn_8 = wait_click.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[text()='8' and contains(@class, 'btn')]"
            )
        )
    )
    btn_8.click()

    btn_equals = wait_click.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[text()='=' and contains(@class, 'btn')]"
            )
        )
    )
    btn_equals.click()

    try:
        driver.find_element(By.CSS_SELECTOR, "#display")
        result_locator = (By.CSS_SELECTOR, "#display")
    except Exception:
        result_locator = (By.CSS_SELECTOR, ".screen")

    result_wait = WebDriverWait(driver, 60)
    result_wait.until(
        EC.text_to_be_present_in_element(result_locator, "15")
    )

    displayed_text = driver.find_element(*result_locator).text
    assert displayed_text == "15", (
        f"Ожидалось 15, получено '{displayed_text}'"
    )
