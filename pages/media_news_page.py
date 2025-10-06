"""Страница новостей в разделе Медиа"""
from selenium.webdriver.common.by import By
from .base_page import BasePage
from config.environment import EnvironmentConfig
from config.test_data import TestData
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MediaNewsPage(BasePage):
    """Страница новостей"""

    # Локаторы
    NEWS_ARTICLES = (By.XPATH, "//article | //div[contains(@class, "
                     "'news-item')] | //div[contains(@class, 'article')]")
    NEWS_TITLE = (By.XPATH, "//h1[contains(text(), 'Новости')] | //h1[contains"
                  "(text(), 'News')]")
    DATE_ELEMENTS = (By.XPATH, "//*[contains(@class, 'date')] | //time | //*"
                     "[contains(text(), '202')]")

    def __init__(self, driver):
        print("🎬 Начало инициализации MediaNewsPage...")
        super().__init__(driver)
        print(f"🌐 Открываю страницу: {EnvironmentConfig.MEDIA_NEWS_URL}")
        # Открываем страницу новостей напрямую
        self.driver.get(EnvironmentConfig.MEDIA_NEWS_URL)
        print(f"✅ Страница открыта. Текущий URL: {self.driver.current_url}")
        print(f"📖 Заголовок страницы: {self.driver.title}")

    @allure.step("Проверить корректность заголовка страницы")
    def is_correct_title(self):
        """Проверить корректность заголовка страницы"""
        page_title = self.get_page_title()
        print(f"🔍 Проверка заголовка: '{page_title}'")
        expected_title = TestData.UI.MEDIA_NEWS_TITLE
        print(f"🔍 Ожидаемый заголовок: '{expected_title}'")

        result = page_title == expected_title
        print(f"✅ Заголовок корректен: {result}")
        return result

    @allure.step("Получить количество новостных статей")
    def get_news_articles_count(self):
        """Получить количество новостных статей"""
        try:
            articles = self.find_elements(*self.NEWS_ARTICLES, timeout=10)
            count = len(articles)
            print(f"📰 Найдено новостных статей: {count}")
            return count
        except TimeoutException:
            print("⚠ Новостные статьи не найдены")
            return 0

    @allure.step("Получить количество элементов с датами")
    def get_date_elements_count(self):
        """Получить количество элементов с датами"""
        try:
            dates = self.find_elements(*self.DATE_ELEMENTS, timeout=10)
            count = len(dates)
            print(f"📅 Найдено элементов с датами: {count}")
            return count
        except TimeoutException:
            print("⚠ Элементы с датами не найдены")
            return 0

    @allure.step("Проверить корректность URL")
    def is_correct_url(self):
        """Проверить корректность URL"""
        current_url = self.get_current_url().lower()
        print(f"🌐 Текущий URL: {current_url}")
        is_correct = any(keyword in current_url for keyword in [
            "news", "новости", "media"])
        print(f"🌐 URL корректен: {is_correct}")
        return is_correct

    @allure.step("Ожидать полной загрузки страницы")
    def wait_for_full_page_load(self, timeout=30):
        """Ожидать полной загрузки страницы"""
        print("⏳ Ожидаем полной загрузки страницы...")

        # Ждем когда document.readyState будет complete
        self.wait.until(lambda driver: driver.execute_script(
            "return document.readyState") == "complete")

        # Дополнительно ждем когда исчезнут индикаторы загрузки
        loading_indicators = [
            "//div[contains(@class, 'loading')]",
            "//div[contains(@class, 'spinner')]",
            "//div[contains(@class, 'progress')]"
        ]

        for indicator in loading_indicators:
            try:
                # Ждем исчезновения индикаторов загрузки
                WebDriverWait(self.driver, 5).until(
                    EC.invisibility_of_element_located((By.XPATH, indicator))
                )
            except Exception:
                pass  # Если индикатора нет - это нормально

        print("✅ Страница полностью загружена")
