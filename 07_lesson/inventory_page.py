from selenium.webdriver.common.by import By
from base_page import BasePage


class InventoryPage(BasePage):
    """Главная страница со списком товаров."""
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_to_cart(self, item_name):
        """
        Добавить товар в корзину по его названию.
        Название должно совпадать с отображаемым на сайте.
        """
        item_id = item_name.lower().replace(" ", "-")
        button_locator = (By.ID, f"add-to-cart-{item_id}")
        self.click(button_locator)

    def get_cart_count(self):
        """Вернуть количество товаров в корзине (значение бейджа)."""
        elements = self.driver.find_elements(*self.CART_BADGE)
        if elements:
            return int(elements[0].text)
        return 0

    def go_to_cart(self):
        """Перейти в корзину. Возвращает объект страницы корзины."""
        self.click(self.CART_LINK)
        from cart_page import CartPage
        return CartPage(self.driver)
