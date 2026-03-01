# test_03_shop.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_full_scenario():

    driver = webdriver.Firefox()
    driver.implicitly_wait(5)

    try:
        # --- Авторизация ---
        driver.get("https://www.saucedemo.com/")

        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username.send_keys("standard_user")

        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        # Проверка успешного входа
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        assert "inventory.html" in driver.current_url

        # --- Добавление товаров ---
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for item in items_to_add:
            button_id = f"add-to-cart-{item.lower().replace(' ', '-')}"
            add_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, button_id))
            )
            add_btn.click()

            # Проверка, что товар добавился (появилась кнопка Remove)
            remove_id = f"remove-{item.lower().replace(' ', '-')}"
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, remove_id))
            )

        # Проверка счётчика корзины
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "3", f"Ожидалось 3 товара, получено {cart_badge.text}"

        # --- Переход в корзину ---
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
        )

        # --- Нажатие Checkout ---
        driver.find_element(By.ID, "checkout").click()

        # --- Заполнение формы ---
        first_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name.send_keys("George")

        last_name = driver.find_element(By.ID, "last-name")
        last_name.send_keys("Eremov")

        postal_code = driver.find_element(By.ID, "postal-code")
        postal_code.send_keys("197318")

        # --- Продолжить ---
        driver.find_element(By.ID, "continue").click()

        # --- Проверка итоговой суммы ---
        # Ждём появления элемента с итогом
        total_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text  # например, "Total: $58.29"

        # Извлекаем число: удаляем "Total: $" и преобразуем в float
        total_value = float(total_text.replace("Total: $", ""))
        expected_total = 58.29

        assert total_value == expected_total, f"Итоговая сумма {total_value}, ожидалась {expected_total}"
        
    finally:
        driver.quit()


if __name__ == "__main__":
    pytest.main([__file__])