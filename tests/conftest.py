"""Общие фикстуры для API и UI тестов"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.environment import EnvironmentConfig


@pytest.fixture
def driver():
    """Фикстура для инициализации браузера для UI тестов"""
    if EnvironmentConfig.BROWSER.lower() == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(
            f"Браузер {EnvironmentConfig.BROWSER} не поддерживается")

    driver.implicitly_wait(EnvironmentConfig.IMPLICIT_WAIT)

    yield driver

    driver.quit()


@pytest.fixture
def main_page(driver):
    """Фикстура для главной страницы"""
    from pages.main_page import MainPage
    page = MainPage(driver)
    print(f"✅ MainPage создана, URL: {driver.current_url}")
    return page
    # from pages.main_page import MainPage
    # return MainPage(driver)


@pytest.fixture
def media_news_page(driver):
    """Фикстура для страницы новостей"""
    from pages.media_news_page import MediaNewsPage
    page = MediaNewsPage(driver)
    print(f"✅ MediaNewsPage создана, URL: {driver.current_url}")
    return page
    # from pages.media_news_page import MediaNewsPage
    # return MediaNewsPage(driver)


@pytest.fixture
def api_headers():
    """Фикстура для заголовков API"""
    headers = {
        'accept': 'application/json',
        'X-API-KEY': EnvironmentConfig.API_KEY
    }
    return headers


@pytest.fixture
def api_client(api_headers):
    """Фикстура для API клиента"""
    import requests
    session = requests.Session()
    session.headers.update(api_headers)
    return session
