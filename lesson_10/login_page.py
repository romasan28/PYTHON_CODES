import allure
from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):
    """Страница авторизации."""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    @allure.step("Открыть страницу входа")
    def open(self) -> None:
        """Открыть страницу входа."""
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Выполнить вход: username='{username}', password='{password}'")
    def login(self, username: str, password: str):
        """
        Выполнить вход.

        :param username: имя пользователя
        :param password: пароль
        :return: объект главной страницы магазина (InventoryPage)
        """
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        from inventory_page import InventoryPage
        return InventoryPage(self.driver)