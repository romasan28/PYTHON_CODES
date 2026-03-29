import allure
import pytest
from selenium import webdriver
from calc_class_methods import SlowCalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
class TestSlowCalculator:

    @allure.title("Проверка вычисления 7+8 с задержкой 45 секунд")
    @allure.description("Устанавливаем задержку, нажимаем кнопки, ожидаем результат 15")
    def test_slow_calculator(self, driver):
        page = SlowCalculatorPage(driver)

        with allure.step("Открыть страницу и установить задержку 45 секунд"):
            page.open()
            page.set_delay(45)

        with allure.step("Выполнить действия: 7 + 8 ="):
            page.press_button("7")
            page.press_button("+")
            page.press_button("8")
            page.press_button("=")

        with allure.step("Проверить результат на дисплее"):
            page.wait_for_result("15")
            result = page.get_display_value()
            assert result == "15", f"Ожидалось 15, получено {result}"