from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):
    """Страница авторизации."""
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open(self):
        """Открыть страницу входа."""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        """
        Выполнить вход.
        Возвращает объект главной страницы магазина.
        """
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        from inventory_page import InventoryPage
        return InventoryPage(self.driver)
