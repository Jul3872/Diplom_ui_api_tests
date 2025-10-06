"""Страница фильма"""
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException
import allure


class FilmPage(BasePage):
    """Страница информации о фильме"""

    # Локаторы для страницы фильма
    FILM_TITLE = (By.CSS_SELECTOR, ".film-title, .movie-title, h1")
    FILM_YEAR = (By.CSS_SELECTOR, ".film-year, .year")
    FILM_RATING = (By.CSS_SELECTOR, ".rating, .film-rating")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait.until(lambda driver: self.is_film_page())

    @allure.step("Проверить, что это страница фильма")
    def is_film_page(self):
        """Проверить, что это страница фильма"""
        current_url = self.get_current_url().lower()
        return "/film/" in current_url or "movie" in current_url

    @allure.step("Получить название фильма")
    def get_film_title(self):
        """Получить название фильма"""
        try:
            return self.find_element(*self.FILM_TITLE).text
        except TimeoutException:
            return ""
