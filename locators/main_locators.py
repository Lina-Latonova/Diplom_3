from selenium.webdriver.common.by import By

class MainLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    BUN_INGREDIENT = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")  # Флюоресцентная булка
    SAUCE_INGREDIENT = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']")  # Соус Spicy-X
    FILLING_INGREDIENT = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa7a']")  # Мясо бессмертных моллюсков


    INGREDIENT_DETAILS_MODAL = (By.XPATH, "(//div[@class='Modal_modal__container__Wo2l_'])[1]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "(//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK'])[1]")
    MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    
    INGREDIENT_COUNTER = (By.XPATH, "(//p[@class='counter_counter__num__3nue1'])[1]")
    

    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")

    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    
    ORDER_MODAL = (By.XPATH,"//div[@class= 'Modal_modal__contentBox__sCy8X pt-30 pb-30']")
    ORDER_NUMBER = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")