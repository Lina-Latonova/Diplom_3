import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", 
                     help="Выбор браузера: chrome или firefox")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    
    if browser == "chrome":
        options = ChromeOptions() 
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        # Автоматическое получение и установка ChromeDriver
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        
        # Автоматическое получение и установка Geckodriver
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        driver.set_window_size(1920, 1080)
    
    else:
        raise ValueError(f"Браузер {browser} не поддерживается")
    
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def main_page(driver):
    return MainPage(driver)

@pytest.fixture(scope="function")
def login(main_page):
    main_page.go_to_site()
    main_page.click_personal_account()
    login_page = LoginPage(main_page.driver)
    login_page.login("galina_aqa_tester@gmail.com", "galina1234")
    main_page.click_constructor()


@pytest.fixture(scope="function")
def order_feed_page(driver):
    page = OrderFeedPage(driver)
    page.go_to_site()
    return page