import pytest
import allure

class TestConstructor:
    @allure.feature("Конструктор бургеров")
    @allure.story("Навигация по разделам")
    @allure.title("Проверка перехода в раздел Конструктор")
    def test_click_constructor(self, login, main_page):
        _ = login
        # Проверяем переход в конструктор из ленты заказов
        main_page.click_order_feed()
        main_page.click_constructor()
        
        # Убеждаемся, что кнопка оформления заказа видна
        assert main_page.check_order_button_is_visible()

    @allure.feature("Конструктор бургеров")
    @allure.story("Навигация по разделам")
    @allure.title("Проверка перехода в раздел Лента заказов")
    def test_click_order_feed(self, login, order_feed_page, main_page):
        _ = login
        main_page.click_order_feed()
        assert order_feed_page.is_total_orders_counter_visible()

    @allure.feature("Конструктор бургеров")
    @allure.story("Детали ингредиентов")
    @allure.title("Проверка открытия модального окна с деталями ингредиента")
    def test_ingredient_modal_open(self, login, main_page):
        _ = login
        main_page.click_ingredient()
        assert main_page.check_modal_is_visible()

    @allure.feature("Конструктор бургеров")
    @allure.story("Детали ингредиентов")
    @allure.title("Проверка закрытия модального окна")
    def test_ingredient_modal_close(self, login, main_page):
        _ = login
        main_page.add_bun_to_constructor()
        main_page.add_filling_to_constructor()
        main_page.create_order()
        
        main_page.get_order_number()
              
        main_page.close_modal()
        
        assert main_page.wait_for_modal_invisible()

    @allure.feature("Конструктор бургеров")
    @allure.story("Счетчики ингредиентов")
    @allure.title("Проверка увеличения счетчика ингредиента")
    def test_ingredient_counter_increase(self, login, main_page):
        _ = login
        initial_count = main_page.get_ingredient_counter()
        main_page.add_bun_to_constructor()
        assert main_page.expect_ingredient_counter_increase(initial_count)