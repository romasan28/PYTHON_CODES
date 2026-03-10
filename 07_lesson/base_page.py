from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех Page Object."""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Ожидание и поиск одного элемента."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Ожидание кликабельности и клик по элементу."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        """Очистка поля и ввод текста."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Получение текста элемента."""
        return self.find_element(locator).text
