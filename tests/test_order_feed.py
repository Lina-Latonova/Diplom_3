import pytest
import allure

class TestOrderFeed:
    @allure.feature("Лента заказов")
    @allure.story("Счетчики заказов")
    @allure.title("Проверка увеличения счетчика 'Выполнено за всё время'")
    def test_total_orders_counter_increase(self, login, order_feed_page, main_page):
        main_page.click_order_feed()
        initial_total = order_feed_page.get_total_orders_count()

        main_page.click_constructor()
        main_page.add_bun_to_constructor()
        main_page.add_sauce_to_constructor()
        main_page.add_filling_to_constructor()
        main_page.create_order()

        main_page.get_order_number()
       
        main_page.close_modal()
        main_page.click_order_feed()

        assert order_feed_page.wait_for_total_orders_increase(initial_total)

    @allure.feature("Лента заказов")
    @allure.story("Счетчики заказов")
    def test_today_orders_counter_increase(self, login, main_page, order_feed_page):
        main_page.click_order_feed()
        initial_today = order_feed_page.get_today_orders_count()
    
        main_page.click_constructor()
        main_page.add_bun_to_constructor()
        main_page.add_sauce_to_constructor()
        main_page.add_filling_to_constructor()
        main_page.create_order()
       
        main_page.get_order_number()

        main_page.close_modal()
        main_page.click_order_feed()
      
        assert order_feed_page.wait_for_today_orders_increase(initial_today)

    @allure.feature("Лента заказов")
    @allure.story("Заказы в работе")
    @allure.title("Проверка отображения заказа в разделе 'В работе'")
    def test_order_in_progress_section(self, login, main_page, order_feed_page):
        main_page.add_bun_to_constructor()
        main_page.add_filling_to_constructor()
        main_page.create_order()
        
        order_number = main_page.get_order_number()
              
        main_page.close_modal()
        main_page.click_order_feed()
        
        assert order_feed_page.wait_for_order_in_progress(order_number)
        