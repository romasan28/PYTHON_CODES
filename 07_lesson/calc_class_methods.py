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
        super().__init__(driver)
        self.display_locator = None  # пока не определён

    def _ensure_display_locator(self):
        """Убедиться, что локатор дисплея определён.
        Страница должна быть открыта.
        """
        if self.display_locator is None:
            self.display_locator = self._get_working_display_locator()

    def _get_working_display_locator(self):
        """Определяет рабочий локатор дисплея, ожидая появления элемента."""
        for locator in self.DISPLAY_LOCATORS:
            try:
                # Используем self.find_element с ожиданием из BasePage
                self.find_element(locator)
                return locator
            except Exception:
                continue
        raise Exception("Не удалось найти элемент дисплея")

    def open(self):
        """Открыть страницу калькулятора."""
        base_url = "https://bonigarcia.dev/selenium-webdriver-java/"
        page_url = "slow-calculator.html"
        self.driver.get(base_url + page_url)

    def set_delay(self, seconds):
        """Установить задержку вычислений."""
        self.send_keys(self.DELAY_INPUT, str(seconds))

    def press_button(self, button_text):
        """
        Нажать кнопку с заданным текстом.
        Ищет <span> с текстом и классом 'btn'.
        """
        locator = (
            By.XPATH,
            f"//span[text()='{button_text}' and contains(@class, 'btn')]"
        )
        self.click(locator)

    def get_display_value(self):
        """Получить текущее значение на дисплее."""
        self._ensure_display_locator()
        return self.get_text(self.display_locator)

    def wait_for_result(self, expected_text, timeout=60):
        """Ожидать появления заданного текста на дисплее."""
        self._ensure_display_locator()
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                self.display_locator, expected_text
            )
        )
