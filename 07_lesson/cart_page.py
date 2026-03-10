from selenium.webdriver.common.by import By
from base_page import BasePage


class CartPage(BasePage):
    """Страница корзины."""
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def proceed_to_checkout(self):
        """Нажать кнопку Checkout. Возвращает страницу ввода данных."""
        self.click(self.CHECKOUT_BUTTON)
        from checkout_info_page import CheckoutInfoPage
        return CheckoutInfoPage(self.driver)
