"""Базовый класс для всех страниц"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.environment import EnvironmentConfig
from selenium.webdriver.common.by import By
import allure


class BasePage:
    """Базовый класс страницы"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EnvironmentConfig.WAIT_TIMEOUT)
        self.base_url = EnvironmentConfig.BASE_URL

    @allure.step("Открыть страницу {url}")
    def open(self, url=""):
        """Открыть страницу"""
        self.driver.get(self.base_url + url)

    @allure.step("Найти элемент {value} по {by}")
    def find_element(self, by, value, timeout=None):
        """Найти элемент с ожиданием"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver,
                                                               timeout)
        return wait.until(EC.presence_of_element_located((by, value)))

    @allure.step("Найти элементы {value} по {by}")
    def find_elements(self, by, value, timeout=None):
        """Найти элементы с ожиданием"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver,
                                                               timeout)
        return wait.until(EC.presence_of_all_elements_located((by, value)))

    @allure.step("Кликнуть на элемент {value} по {by}")
    def click_element(self, by, value, timeout=None):
        """Кликнуть на элемент с ожиданием кликабельности"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver,
                                                               timeout)
        element = wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    @allure.step("Ввести текст {text} в элемент {value} по {by}")
    def send_keys(self, by, value, text, timeout=None):
        """Ввести текст в элемент"""
        element = self.find_element(by, value, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Проверить наличие элемента {value} по {by}")
    def is_element_present(self, by, value, timeout=None):
        """Проверить наличие элемента"""
        try:
            self.find_element(by, value, timeout)
            return True
        except TimeoutException:
            return False

    @allure.step("Проверить наличие текста {text} на странице")
    def is_text_present(self, text, timeout=None):
        """Проверить наличие текста на странице"""
        try:
            self.find_element(By.XPATH, f"//*[contains(text(), '{text}')]",
                              timeout)
            return True
        except TimeoutException:
            return False

    @allure.step("Принять куки если появляется окно")
    def accept_cookies_if_present(self):
        """Принять куки если появляется окно"""
        cookie_selectors = [
            (By.XPATH, "//button[contains(text(), 'Принять')]"),
            (By.XPATH, "//button[contains(text(), 'Согласен')]"),
            (By.XPATH, "//button[contains(text(), 'Принять все')]")
        ]

        for by, selector in cookie_selectors:
            try:
                cookie_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((by, selector))
                )
                cookie_button.click()
                print("✓ Куки приняты")
                return True
            except TimeoutException:
                continue
        return False

    @allure.step("Получить заголовок страницы")
    def get_page_title(self):
        """Получить заголовок страницы"""
        return self.driver.title

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url
