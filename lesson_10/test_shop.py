import allure
import pytest
from selenium import webdriver
from login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
class TestShop:

    @allure.title("Полный сценарий покупки трёх товаров")
    @allure.description("Авторизация, добавление товаров, оформление заказа, проверка итоговой суммы")
    def test_full_purchase(self, driver):
        login_page = LoginPage(driver)

        with allure.step("Открыть страницу и авторизоваться"):
            login_page.open()
            inventory_page = login_page.login("standard_user", "secret_sauce")

        items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        with allure.step("Добавить товары в корзину"):
            for item in items:
                inventory_page.add_to_cart(item)

        with allure.step("Проверить количество товаров в корзине"):
            assert inventory_page.get_cart_count() == 3, \
                "Неверное количество товаров в корзине"

        with allure.step("Перейти в корзину и начать оформление"):
            cart_page = inventory_page.go_to_cart()
            checkout_info_page = cart_page.proceed_to_checkout()

        with allure.step("Заполнить форму доставки"):
            checkout_overview_page = checkout_info_page.fill_info(
                "George", "Eremov", "197318"
            )

        with allure.step("Получить итоговую сумму и сравнить с ожидаемой"):
            total = checkout_overview_page.get_total()
            expected_total = 58.29
            assert total == expected_total, \
                f"Итоговая сумма {total}, ожидалась {expected_total}"