import allure
from selenium.webdriver.common.by import By
from base_page import BasePage


class CheckoutOverviewPage(BasePage):
    """Страница обзора заказа с итоговой суммой."""

    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Получить итоговую стоимость")
    def get_total(self) -> float:
        """
        Вернуть итоговую стоимость в виде числа.

        :return: итоговая сумма (float)
        """
        total_text = self.get_text(self.TOTAL_LABEL)
        return float(total_text.replace("Total: $", ""))