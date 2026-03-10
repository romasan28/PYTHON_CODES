import pytest
from selenium import webdriver
from calc_class_methods import SlowCalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    """
    Тест проверяет работу медленного калькулятора с задержкой 45 секунд.
    Шаги:
    1. Открыть страницу.
    2. Установить задержку 45.
    3. Нажать 7, +, 8, =.
    4. Проверить, что через 45 секунд результат равен 15.
    """
    page = SlowCalculatorPage(driver)
    page.open()
    page.set_delay(45)
    page.press_button("7")
    page.press_button("+")
    page.press_button("8")
    page.press_button("=")
    page.wait_for_result("15")
    assert page.get_display_value() == "15", "Результат не равен 15"
