"""Главная страница Кинопоиска"""
from selenium.webdriver.common.by import By
from .base_page import BasePage
from config.test_data import TestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class MainPage(BasePage):
    """Главная страница Кинопоиска"""

    # Локаторы
    LOGO = (By.CSS_SELECTOR, "img.styles_img__uFl47, "
            ".kinopoisk-header-logo__img, [data-tid='logo']")
    SEARCH_FIELD = (By.CSS_SELECTOR, "input.styles_inputActive__mIqMs, "
                    "input.kinopoisk-header-search-form-input__input, "
                    "[name='kp_query']")
    NAV_MENU = (By.CSS_SELECTOR, "div.styles_sticky__tX8W_")
    MAIN_SLIDER = (By.CSS_SELECTOR, ".styles_root__slider__hU96X, .slider")
    FOOTER = (By.CSS_SELECTOR, "footer, [data-tid='footer']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-tid='login-button'], "
                    ".styles_root__auth__a1b2c, .header__login")
    ADVANCED_SEARCH_LINK = (By.CSS_SELECTOR, "a.styles_advancedSearch__gn_09")
    MEDIA_SECTION = (By.XPATH, "//a[contains(@href, '/media/') or "
                     "contains(text(), 'Медиа')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.open()
        self.accept_cookies_if_present()

    @allure.step("Проверить отображение логотипа")
    def is_logo_displayed(self):
        """Проверить отображение логотипа"""
        return self.find_element(*self.LOGO).is_displayed()

    @allure.step("Проверить отображение поля поиска")
    def is_search_field_displayed(self):
        """Проверить отображение поля поиска"""
        return self.find_element(*self.SEARCH_FIELD).is_displayed()

    @allure.step("Проверить отображение навигационного меню")
    def is_navigation_menu_displayed(self):
        """Проверить отображение навигационного меню"""
        return self.find_element(*self.NAV_MENU).is_displayed()

    @allure.step("Получить текст навигационного меню")
    def get_navigation_menu_text(self):
        """Получить текст навигационного меню"""
        return self.find_element(*self.NAV_MENU).text

    @allure.step("Проверить отображение футера")
    def is_footer_displayed(self):
        """Проверить отображение футера"""
        return self.find_element(*self.FOOTER).is_displayed()

    @allure.step("Получить количество ссылок в футере")
    def get_footer_links_count(self):
        """Получить количество ссылок в футере"""
        footer = self.find_element(*self.FOOTER)
        return len(footer.find_elements(By.TAG_NAME, "a"))

    @allure.step("Кликнуть на расширенный поиск")
    def click_advanced_search(self):
        """Кликнуть на расширенный поиск"""
        self.click_element(*self.ADVANCED_SEARCH_LINK)
        from .advanced_search_page import AdvancedSearchPage
        return AdvancedSearchPage(self.driver)

    @allure.step("Выполнить поиск фильма")
    def search_for_film(self, film_name):
        """Выполнить поиск фильма"""
        search_field = self.find_element(*self.SEARCH_FIELD)
        search_field.clear()
        search_field.send_keys(film_name)
        search_field.submit()

        from .search_page import SearchPage
        return SearchPage(self.driver)

    @allure.step("Проверить наличие пунктов меню")
    def verify_navigation_menu_items(self):
        """Проверить наличие пунктов меню"""
        menu_text = self.get_navigation_menu_text()
        found_items = [
            item for item in TestData.UI.NAV_MENU_ITEMS if item in menu_text]
        return found_items

    @allure.step("Выполнить поиск фильма с ожиданием выпадающего списка")
    def search_for_film_with_dropdown(self, film_name):
        """Выполнить поиск фильма с ожиданием выпадающего списка"""
        # Находим поле поиска - используем более надежные локаторы
        search_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//input[@placeholder='Фильмы, "
                                        "сериалы, персоны' or " +
                                        "contains(@class, 'search') or " +
                                        "@name='kp_query']"))
        )

        # Вводим название фильма
        search_input.clear()
        search_input.send_keys(film_name)
        print(f"✓ Введен поисковый запрос: '{film_name}'")

        # Ждем появления выпадающих результатов
        try:
            dropdown_results = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  "//div[contains(@class, "
                                                  "'styles_"
                                                  "groupsContainer__JKMOw')"
                                                  " or contains(@class, "
                                                  "'kinopoisk-header-"
                                                  "suggest__groups-container')"
                                                  "]"))
            )

            # Проверяем что в результатах есть искомый фильм
            results_text = dropdown_results.text.lower()
            assert film_name.lower() in results_text
            print("✓ Выпадающие результаты поиска отображаются")

            # Выбираем первый элемент из выпадающего списка
            first_result = dropdown_results.find_element(By.XPATH, ".//a")
            first_result.click()

            # Ждем загрузки страницы фильма
            WebDriverWait(self.driver, 15).until(
                lambda driver: "/film/" in driver.current_url
            )

            print("✓ Переход на страницу фильма выполнен")

            from .film_page import FilmPage
            return FilmPage(self.driver)

        except TimeoutException:
            print("⚠ Выпадающие результаты не появились")
            # Если нет выпадающего списка, выполняем обычный поиск
            search_input.submit()
            from .search_page import SearchPage
            return SearchPage(self.driver)
