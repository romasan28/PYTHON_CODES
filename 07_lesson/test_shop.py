import pytest
from selenium import webdriver
from login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_full_purchase(driver):
    """
    Тест полного сценария покупки:
    - авторизация,
    - добавление трёх товаров,
    - переход в корзину,
    - оформление заказа,
    - проверка итоговой суммы.
    """
    login_page = LoginPage(driver)
    login_page.open()
    inventory_page = login_page.login("standard_user", "secret_sauce")

    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for item in items:
        inventory_page.add_to_cart(item)

    assert inventory_page.get_cart_count() == 3, (
        "Неверное количество товаров в корзине"
    )

    cart_page = inventory_page.go_to_cart()
    checkout_info_page = cart_page.proceed_to_checkout()
    checkout_overview_page = checkout_info_page.fill_info(
        "George", "Eremov", "197318"
    )

    total = checkout_overview_page.get_total()
    expected_total = 58.29
    assert total == expected_total, (
        f"Итоговая сумма {total}, ожидалась {expected_total}"
    )
