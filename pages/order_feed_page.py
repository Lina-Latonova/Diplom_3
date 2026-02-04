from .base_page import BasePage
import allure
from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class OrderFeedPage(BasePage):

    @allure.step("Получить количество заказов за все время")
    def get_total_orders_count(self):
        element = self.find_element(OrderFeedLocators.TOTAL_ORDERS_COUNT)
        return int(element.text)

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        element = self.find_element(OrderFeedLocators.TODAY_ORDERS_COUNT)
        return int(element.text)

    @allure.step("Получить заказы в работе")
    def get_in_progress_orders(self):
        self.wait_for_element_invisible(OrderFeedLocators.MODAL_WINDOW)
        elements = self.find_elements(OrderFeedLocators.IN_PROGRESS_ORDERS)
        return [element.text for element in elements if element.text]
        
    @allure.step("Получить номера всех заказов")
    def get_order_numbers(self):
        elements = self.find_elements(OrderFeedLocators.ORDER_CARDS)
        return [element.text for element in elements if element.text]
    
    @allure.step("Проверить видимость счетчика заказов за все время")
    def is_total_orders_counter_visible(self):
        try:
            self.wait_for_element_visible(OrderFeedLocators.TOTAL_ORDERS_COUNT, 5)
            return True
        except:
            return False
        
    @allure.step("Ожидать увеличение счетчика заказов за все время")
    def wait_for_total_orders_increase(self, initial_count, time=10):
        try:
            self.wait_for_condition(
                lambda driver: self.get_total_orders_count() > initial_count,
                time,
                "Счетчик заказов за все время не увеличился"
            )
            return True
        except:
            return False
        
    @allure.step("Ожидать увеличение счетчика заказов за сегодня")
    def wait_for_today_orders_increase(self, initial_count, time=15):
        WebDriverWait(self.driver, time).until(
        lambda driver: self.get_total_orders_count() > initial_count
        )
        return True

    @allure.step("Ожидать появление заказа в разделе 'В работе'")
    def wait_for_order_in_progress(self, order_number, time=10):
        try:
            self.wait_for_condition(
                lambda driver: any(order_number in order for order in self.get_in_progress_orders()),
                time, f"Заказ {order_number} не появился в разделе 'В работе'")
            return True
        except TimeoutException:
            return False