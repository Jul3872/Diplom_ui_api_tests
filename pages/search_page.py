"""Страница поиска"""
from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure


class SearchPage(BasePage):
    """Страница результатов поиска"""

    # Локаторы
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div.search_results.search_results_"
                      "last, div.element, .search_results > div")
    NO_RESULTS_MESSAGE = (By.XPATH, "//*[contains(text(), "
                          "'ничего не найдено')]")
    DROPDOWN_RESULTS = (By.XPATH, "//div[contains(@class, "
                        "'styles_groupsContainer__JKMOw') or contains(@class, "
                        "'kinopoisk-header-suggest__groups-container')]")
    FIRST_RESULT = (By.XPATH, ".//a")

    @allure.step("Проверить отображение результатов")
    def are_results_displayed(self):
        """Проверить отображение результатов"""
        return self.is_element_present(*self.SEARCH_RESULTS, timeout=10)

    @allure.step("Проверить сообщение об отсутствии результатов")
    def is_no_results_message_displayed(self):
        """Проверить сообщение об отсутствии результатов"""
        return self.is_text_present("ничего не найдено"
                                    ) or self.is_element_present(
                                        *self.NO_RESULTS_MESSAGE)
