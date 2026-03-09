from selenium.webdriver.common.by import By
from base_page import BasePage


class CheckoutInfoPage(BasePage):
    """Страница ввода личных данных для оформления заказа."""
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def fill_info(self, first, last, zip_code):
        """
        Заполнить форму и нажать Continue.
        Возвращает страницу обзора заказа.
        """
        self.send_keys(self.FIRST_NAME, first)
        self.send_keys(self.LAST_NAME, last)
        self.send_keys(self.POSTAL_CODE, zip_code)
        self.click(self.CONTINUE_BUTTON)
        from checkout_overview_page import CheckoutOverviewPage
        return CheckoutOverviewPage(self.driver)
