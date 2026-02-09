import allure
from .base_page import BasePage
from locators.main_locators import MainLocators

class MainPage(BasePage):
    @allure.step("Кликнуть на кнопку 'Конструктор'")
    def click_constructor(self):        
        self.click_element(MainLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на кнопку 'Лента Заказов'")
    def click_order_feed(self):
        self.wait_for_element_clickable(MainLocators.ORDER_FEED_BUTTON, time=40)
        self.click_element(MainLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть на кнопку 'Личный Кабинет'")
    def click_personal_account(self):
        self.click_element(MainLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Добавить булку в конструктор")
    def add_bun_to_constructor(self):
        self.drag_and_drop(MainLocators.BUN_INGREDIENT, MainLocators.CONSTRUCTOR_DROP_AREA)

    @allure.step("Добавить соус в конструктор")
    def add_sauce_to_constructor(self):
        self.drag_and_drop(MainLocators.SAUCE_INGREDIENT, MainLocators.CONSTRUCTOR_DROP_AREA)

    @allure.step("Добавить начинку в конструктор")
    def add_filling_to_constructor(self):
        self.drag_and_drop(MainLocators.FILLING_INGREDIENT, MainLocators.CONSTRUCTOR_DROP_AREA)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self.click_element(MainLocators.BUN_INGREDIENT)

    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter(self):
        counter = self.find_element(MainLocators.INGREDIENT_COUNTER)
        return int(counter.text)

    @allure.step("Создать заказ")
    def create_order(self):
        self.click_element(MainLocators.ORDER_BUTTON)

    @allure.step("Проверить создание заказа")
    def check_order_creation(self):
        self.wait_for_element_visible(MainLocators.ORDER_MODAL, 15)

    @allure.step("Проверить видимость кнопки оформления заказа")
    def check_order_button_is_visible(self):
        element = self.find_element(MainLocators.ORDER_BUTTON)
        return element.is_displayed()

    @allure.step("Ожидать увеличение счетчика ингредиента")
    def expect_ingredient_counter_increase(self, initial_count, time=40):
        self.wait_for_condition(
            lambda _: self.get_ingredient_counter() > initial_count,
            time=time,
            message="Счетчик ингредиента не увеличился")
        return True
    

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        old_value = self.find_element(MainLocators.ORDER_NUMBER).text

        self.wait_for_condition(
            lambda _: self.find_element(MainLocators.ORDER_NUMBER).text != old_value,
            time=40,
            message="Номер заказа не изменился")

        new_element = self.find_element(MainLocators.ORDER_NUMBER)
        return new_element.text


    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.wait_for_element_clickable(MainLocators.MODAL_CLOSE_BUTTON)
        modal_close_button = self.find_element(MainLocators.MODAL_CLOSE_BUTTON)
        self.execute_script("arguments[0].click();", modal_close_button)
        self.wait_for_element_invisible(MainLocators.MODAL_OVERLAY)

    @allure.step("Проверить видимость модального окна")
    def check_modal_is_visible(self):
        element = self.find_element(MainLocators.INGREDIENT_DETAILS_MODAL)
        return element.is_displayed()
    
    @allure.step("Ожидать исчезновение модального окна")
    def wait_for_modal_invisible(self, time=5):
        self.wait_for_element_invisible(MainLocators.INGREDIENT_DETAILS_MODAL, time)
        allure.attach(body=f"Элемент {MainLocators.INGREDIENT_DETAILS_MODAL} успешно исчез.",
                      name="wait_for_modal_invisible_success", attachment_type=allure.attachment_type.TEXT)
        return True
    
    @allure.step("Закрыть модальное окно через JavaScript")
    def close_modal_by_js(self):
        self.execute_script("""
            var overlay = document.querySelector('.Modal_modal_overlay__x2ZCr');
            if (overlay && overlay.style.display !== 'none') {
                overlay.style.display = 'none';
            }
        """)