# test_02_calc.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    try:
        # 1. Открыть страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # 2. Установить задержку 45 секунд
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")
        # Убедимся, что значение действительно установилось
        assert delay_input.get_attribute("value") == "45", "Задержка не установилась"

        # 3. Нажать кнопки: 7, +, 8, =
        wait_click = WebDriverWait(driver, 10)

        # Кнопка "7"
        btn_7 = wait_click.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='7' and contains(@class, 'btn')]"))
        )
        btn_7.click()

        # Кнопка "+"
        btn_plus = wait_click.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='+' and contains(@class, 'btn')]"))
        )
        btn_plus.click()

        # Кнопка "8"
        btn_8 = wait_click.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='8' and contains(@class, 'btn')]"))
        )
        btn_8.click()

        # Кнопка "="
        btn_equals = wait_click.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='=' and contains(@class, 'btn')]"))
        )
        btn_equals.click()

        # 4. Ожидаем появления результата 15 на дисплее
        # Сначала проверим, есть ли элемент с id="display". Если нет, используем .screen.
        try:
            driver.find_element(By.CSS_SELECTOR, "#display")
            result_locator = (By.CSS_SELECTOR, "#display")
        except:
            result_locator = (By.CSS_SELECTOR, ".screen")

        result_wait = WebDriverWait(driver, 60)
        result_wait.until(
            EC.text_to_be_present_in_element(result_locator, "15")
        )

        # Дополнительная проверка
        displayed_text = driver.find_element(*result_locator).text
        assert displayed_text == "15", f"Ожидалось 15, но получено '{displayed_text}'"

    finally:
        driver.quit()


if __name__ == "__main__":
    pytest.main([__file__])