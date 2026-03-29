from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех Page Object."""

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        """
        Инициализация базовой страницы.

        :param driver: экземпляр веб-драйвера
        :param timeout: максимальное время ожидания (в секундах)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        """
        Ожидание и поиск одного элемента.

        :param locator: кортеж (By, selector)
        :return: найденный веб-элемент
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator: Tuple[str, str]) -> None:
        """
        Ожидание кликабельности и клик по элементу.

        :param locator: кортеж (By, selector)
        """
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator: Tuple[str, str], text: str) -> None:
        """
        Очистка поля и ввод текста.

        :param locator: кортеж (By, selector)
        :param text: текст для ввода
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: Tuple[str, str]) -> str:
        """
        Получение текста элемента.

        :param locator: кортеж (By, selector)
        :return: текстовое содержимое элемента
        """
        return self.find_element(locator).text