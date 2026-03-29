import allure
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    """Фикстура для создания и закрытия драйвера Chrome (по умолчанию)."""
    browser = getattr(request, 'param', 'chrome')
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()