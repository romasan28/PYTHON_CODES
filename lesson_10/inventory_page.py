import allure
from selenium.webdriver.common.by import By
from base_page import BasePage


class InventoryPage(BasePage):
    """Главная страница со списком товаров."""

    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    @allure.step("Добавить товар '{item_name}' в корзину")
    def add_to_cart(self, item_name: str) -> None:
        """
        Добавить товар в корзину по его названию.

        :param item_name: название товара (как на сайте)
        """
        item_id = item_name.lower().replace(" ", "-")
        button_locator = (By.ID, f"add-to-cart-{item_id}")
        self.click(button_locator)

    @allure.step("Получить количество товаров в корзине")
    def get_cart_count(self) -> int:
        """
        Вернуть количество товаров в корзине (значение бейджа).

        :return: количество товаров
        """
        elements = self.driver.find_elements(*self.CART_BADGE)
        if elements:
            return int(elements[0].text)
        return 0

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        """
        Перейти в корзину.

        :return: объект страницы корзины (CartPage)
        """
        self.click(self.CART_LINK)
        from cart_page import CartPage
        return CartPage(self.driver)