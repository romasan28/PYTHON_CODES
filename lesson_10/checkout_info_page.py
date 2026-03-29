import allure
from selenium.webdriver.common.by import By
from base_page import BasePage


class CheckoutInfoPage(BasePage):
    """Страница ввода личных данных для оформления заказа."""

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    @allure.step("Заполнить форму: имя='{first}', фамилия='{last}', индекс='{zip_code}'")
    def fill_info(self, first: str, last: str, zip_code: str):
        """
        Заполнить форму и нажать Continue.

        :param first: имя
        :param last: фамилия
        :param zip_code: почтовый индекс
        :return: объект страницы обзора заказа (CheckoutOverviewPage)
        """
        self.send_keys(self.FIRST_NAME, first)
        self.send_keys(self.LAST_NAME, last)
        self.send_keys(self.POSTAL_CODE, zip_code)
        self.click(self.CONTINUE_BUTTON)
        from checkout_overview_page import CheckoutOverviewPage
        return CheckoutOverviewPage(self.driver)