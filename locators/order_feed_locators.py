from selenium.webdriver.common.by import By

class OrderFeedLocators:
    # Локаторы для ленты заказов
    TOTAL_ORDERS_COUNT = (By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[1]")
    TODAY_ORDERS_COUNT = (By.XPATH, "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")
    IN_PROGRESS_ORDERS = (By.XPATH, "(//li[@class='text text_type_digits-default mb-2'])[6]") 
    ORDER_CARDS = (By.XPATH, "//ul[@class='OrderFeed_list__OLh59']")
    MODAL_WINDOW = (By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']")
