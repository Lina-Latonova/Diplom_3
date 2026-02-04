from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure
from urls import URL
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = URL

    @allure.step("Найти элемент по локатору: {locator}")
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент не найден: {locator}"
        )

    @allure.step("Найти все элементы по локатору: {locator}")
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Элементы не найдены: {locator}"
        )

    @allure.step("Перейти на сайт")
    def go_to_site(self):
        return self.driver.get(self.base_url)

    @allure.step("Ожидать видимость элемента: {locator}")
    def wait_for_element_visible(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент не виден: {locator}"
        )

    @allure.step("Ожидать кликабельность элемента: {locator}")
    def wait_for_element_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент не кликабелен: {locator}"
        )

    @allure.step("Кликнуть по элементу: {locator}")
    def click_element(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    @allure.step("Ввести текст '{text}' в поле: {locator}")
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Выполнить JavaScript-скрипт")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)
    
    @allure.step("Ожидать исчезновение элемента: {locator}")
    def wait_for_element_invisible(self, locator, time=20):
        try:
            WebDriverWait(self.driver, time).until(
                EC.invisibility_of_element_located(locator),
                message=f"Элемент не исчез: {locator}"
            )
            allure.attach(body=f"Элемент {locator} успешно исчез.", name="wait_for_element_invisible_success", attachment_type=allure.attachment_type.TEXT)
            return True
        except TimeoutException:
            allure.attach(body=f"Элемент {locator} не исчез за {time} секунд.", name="wait_for_element_invisible_timeout", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Ожидать выполнение условия")
    def wait_for_condition(self, condition, time=10, message="Условие не выполнено"):
        return WebDriverWait(self.driver, time).until(
            condition,
            message=message
        )

    @allure.step("Выполнить drag-and-drop из {source_locator} в {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    def wait_for_order_number_change(self, locator, old_value):
        def _predicate(driver):
            element = driver.find_element(*locator)
            return element.text != old_value
        return _predicate