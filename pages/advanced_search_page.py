"""Страница расширенного поиска"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
import allure


class AdvancedSearchPage(BasePage):
    """Страница расширенного поиска"""

    # Локаторы
    YEAR_FROM = (By.NAME, "m_act[from_year]")
    YEAR_TO = (By.NAME, "m_act[to_year]")
    COUNTRY_SELECT = (By.NAME, "m_act[country]")
    SEARCH_BUTTON = (By.CLASS_NAME, "el_18.submit.nice_button")
    RESULT_YEAR = (By.CSS_SELECTOR, "span.year")
    RESULT_COUNTRY = (By.CSS_SELECTOR, "span.gray")

    @allure.step("Установить фильтр по годам: от {year_from} до {year_to}")
    def set_year_filter(self, year_from, year_to):
        """Установить фильтр по годам"""
        with allure.step(f"Установить год от: {year_from}"):
            year_from_field = self.find_element(*self.YEAR_FROM)
            self.driver.execute_script("arguments[0].value = '';",
                                       year_from_field)
            year_from_field.send_keys(year_from)

        with allure.step(f"Установить год до: {year_to}"):
            year_to_field = self.find_element(*self.YEAR_TO)
            self.driver.execute_script("arguments[0].value = '';",
                                       year_to_field)
            year_to_field.send_keys(year_to)

    @allure.step("Установить фильтр по стране: {country}")
    def set_country_filter(self, country):
        """Установить фильтр по стране"""
        country_select = Select(self.find_element(*self.COUNTRY_SELECT))
        country_select.select_by_visible_text(country)

    @allure.step("Применить фильтры и выполнить поиск")
    def apply_filters(self):
        """Применить фильтры и выполнить поиск"""
        self.click_element(*self.SEARCH_BUTTON)

        from .search_page import SearchPage
        return SearchPage(self.driver)
