import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage


class SlowCalculatorPage(BasePage):
    """Page Object для страницы медленного калькулятора."""

    # Локаторы
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    DISPLAY_LOCATORS = [
        (By.CSS_SELECTOR, "#display"),
        (By.CSS_SELECTOR, ".screen")
    ]

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        :param driver: экземпляр веб-драйвера
        """
        super().__init__(driver)
        self.display_locator = None  # будет определён позже

    def _ensure_display_locator(self) -> None:
        """Убедиться, что локатор дисплея определён (внутренний метод)."""
        if self.display_locator is None:
            self.display_locator = self._get_working_display_locator()

    def _get_working_display_locator(self) -> tuple:
        """
        Определяет рабочий локатор дисплея, ожидая появления элемента.

        :return: кортеж (By, selector) для найденного элемента
        :raises Exception: если ни один локатор не подошёл
        """
        for locator in self.DISPLAY_LOCATORS:
            try:
                self.find_element(locator)
                return locator
            except Exception:
                continue
        raise Exception("Не удалось найти элемент дисплея")

    @allure.step("Открыть страницу медленного калькулятора")
    def open(self) -> None:
        """Открыть страницу калькулятора."""
        base_url = "https://bonigarcia.dev/selenium-webdriver-java/"
        page_url = "slow-calculator.html"
        self.driver.get(base_url + page_url)

    @allure.step("Установить задержку {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """
        Установить задержку вычислений.

        :param seconds: количество секунд задержки
        """
        self.send_keys(self.DELAY_INPUT, str(seconds))

    @allure.step("Нажать кнопку '{button_text}'")
    def press_button(self, button_text: str) -> None:
        """
        Нажать кнопку с заданным текстом.

        :param button_text: текст на кнопке (например, '7', '+', '=')
        """
        locator = (
            By.XPATH,
            f"//span[text()='{button_text}' and contains(@class, 'btn')]"
        )
        self.click(locator)

    @allure.step("Получить значение на дисплее")
    def get_display_value(self) -> str:
        """
        Получить текущее значение на дисплее.

        :return: текст, отображаемый на дисплее
        """
        self._ensure_display_locator()
        return self.get_text(self.display_locator)

    @allure.step("Ожидать появления результата '{expected_text}' (таймаут {timeout} сек)")
    def wait_for_result(self, expected_text: str, timeout: int = 60) -> None:
        """
        Ожидать появления заданного текста на дисплее.

        :param expected_text: ожидаемый текст (например, '15')
        :param timeout: максимальное время ожидания в секундах
        """
        self._ensure_display_locator()
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                self.display_locator, expected_text
            )
        )