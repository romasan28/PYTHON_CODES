import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_full_purchase(driver):
    driver.get("https://www.saucedemo.com/")

    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    assert "inventory.html" in driver.current_url

    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]

    for item in items_to_add:
        button_id = f"add-to-cart-{item.lower().replace(' ', '-')}"
        add_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, button_id))
        )
        add_btn.click()

        remove_id = f"remove-{item.lower().replace(' ', '-')}"
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, remove_id))
        )

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "3", \
        f"Ожидалось 3 товара, получено {cart_badge.text}"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
    )

    driver.find_element(By.ID, "checkout").click()

    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    first_name.send_keys("George")

    driver.find_element(By.ID, "last-name").send_keys("Eremov")
    driver.find_element(By.ID, "postal-code").send_keys("197318")
    driver.find_element(By.ID, "continue").click()

    total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text
    total_value = float(total_text.replace("Total: $", ""))
    expected_total = 58.29
    assert total_value == expected_total, (
        f"Итоговая сумма {total_value}, ожидалась {expected_total}"
        )
