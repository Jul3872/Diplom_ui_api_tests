"""UI тесты Кинопоиска с использованием Page Object Model"""
from config.test_data import TestData
import allure


class TestKinopoiskUI:
    """Все UI тесты Кинопоиска"""

    @allure.step("Тест 1: Негативный сценарий - поиск несуществующего фильма")
    def test_search_negative_scenario(self, main_page):
        """Тест 1: Негативный сценарий - поиск несуществующего фильма"""
        print("\n🔍 UI Тест 1: Негативный сценарий поиска")

        # Выполняем поиск несуществующего фильма
        search_page = main_page.search_for_film(
            TestData.UI.SEARCH_NEGATIVE_QUERY)

        # Проверяем сообщение об отсутствии результатов
        assert search_page.is_no_results_message_displayed(), "Сообщение "
        "об отсутствии результатов не отображается"
        print("✅ Корректная обработка отсутствия результатов")

    @allure.step("Тест 2: Расширенный поиск с проверкой фильтров: страна, год")
    def test_advanced_search_filters(self, main_page):
        """Тест 2: Расширенный поиск с проверкой фильтров: страна, год"""
        print("\n🎯 UI Тест 2: Расширенный поиск с фильтрами")

        # Переходим в расширенный поиск
        advanced_search_page = main_page.click_advanced_search()

        # Устанавливаем фильтры
        filters = TestData.UI.ADVANCED_SEARCH_FILTERS
        advanced_search_page.set_year_filter(filters['year_from'], filters[
            'year_to'])
        advanced_search_page.set_country_filter(filters['country'])

        # Применяем фильтры
        search_page = advanced_search_page.apply_filters()

        # Проверяем результаты
        assert (search_page.are_results_displayed() or
                search_page.is_no_results_message_displayed()
                ), "Нет результатов и нет сообщения об их отсутствии"
        print("✅ Поиск с фильтрами выполнен успешно")

    @allure.step("Тест поиска фильма по названию (рабочая версия)")
    def test_search_film_by_name_working(self, main_page):
        """Тест поиска фильма по названию (рабочая версия)"""
        print("\n🎬 UI Тест 3: Поиск фильма по названию (рабочая версия)")

        # Используем старый рабочий метод
        film_page = main_page.search_for_film_with_dropdown(
            TestData.UI.SEARCH_FILM_NAME)

        # Проверяем что мы на странице фильма
        current_url = film_page.get_current_url().lower()
        assert "/film/" in current_url, (
            f"Не перешли на страницу фильма. Текущий URL: {current_url}")
        print("✅ Успешный переход на страницу фильма")

        # Проверяем заголовок страницы
        page_title = film_page.get_film_title().lower()
        assert TestData.UI.SEARCH_FILM_NAME.lower() in page_title, (
            f"Название фильма не найдено в заголовке: {page_title}")
        print(f"✅ Заголовок страницы содержит название фильма: "
              f"{film_page.get_film_title()}")

        # Дополнительные проверки страницы фильма
        film_title = film_page.get_film_title()
        if film_title:
            print(f"✅ Название фильма на странице: {film_title}")

    @allure.step("Тест 4: Раздел Новости в разделе Медиа")
    def test_media_news_section(self, media_news_page):
        """Тест 4: Раздел Новости в разделе Медиа"""
        print("\n📰 UI Тест 4: Раздел Новости в Медиа")

        try:
            # Ожидаем полной загрузки страницы
            print("⏳ Ожидаем полной загрузки страницы...")
            media_news_page.wait_for_full_page_load()

            # Проверяем заголовок страницы
            print("🔍 Проверяем заголовок страницы...")
            assert media_news_page.is_correct_title(), "Заголовок страницы "
            "не соответствует ожидаемому"
            print("✅ Заголовок страницы корректен")

            # Проверяем URL
            print("🔍 Проверяем URL страницы...")
            assert media_news_page.is_correct_url(), "URL страницы не "
            "соответствует странице новостей"
            print("✅ URL страницы корректен")

            # Проверяем наличие новостных статей
            print("🔍 Ищем новостные статьи...")
            articles_count = media_news_page.get_news_articles_count()
            assert articles_count > 0, "Новостные статьи не найдены"
            print(f"✅ Найдено новостных статей: {articles_count}")

            # Дополнительная проверка - наличие дат у новостей
            print("🔍 Проверяем наличие дат у новостей...")
            dates_count = media_news_page.get_date_elements_count()
            if dates_count > 0:
                print(f"✅ Найдено элементов с датами: {dates_count}")
            else:
                print("⚠ Элементы с датами не найдены")

            print("🎉 Все проверки страницы новостей пройдены!")

        except Exception as e:
            print(f"❌ Ошибка в тесте: {e}")
            # Делаем скриншот при ошибке
            media_news_page.driver.save_screenshot("media_news_error.png")
            print("📸 Скриншот ошибки сохранен: media_news_error.png")
            raise

    @allure.step("Тест 5: Проверка элементов главной страницы")
    def test_main_page_elements(self, main_page):
        """Тест 5: Проверка элементов главной страницы"""
        print("\n🏠 UI Тест 5: Элементы главной страницы")

        # 1. Проверка логотипа
        assert main_page.is_logo_displayed(), "Логотип не отображается"
        print("✅ Логотип отображается")

        # 2. Проверка поля поиска
        assert main_page.is_search_field_displayed(), "Поле поиска "
        "не отображается"
        print("✅ Поле поиска присутствует")

        # 3. Проверка навигационного меню
        assert main_page.is_navigation_menu_displayed(), "Навигационное "
        "меню не отображается"
        found_items = main_page.verify_navigation_menu_items()
        assert len(found_items) >= 3, (
            f"Слишком мало пунктов меню найдено: {len(found_items)}")
        print(f"✅ Найдено пунктов меню: {len(found_items)}/"
              f"{len(TestData.UI.NAV_MENU_ITEMS)}")

        # 4. Проверка футера
        assert main_page.is_footer_displayed(), "Футер не отображается"
        links_count = main_page.get_footer_links_count()
        assert links_count > 0, "В футере нет ссылок"
        print(f"✅ Футер присутствует, найдено ссылок: {links_count}")

        print("✅ Все элементы главной страницы проверены!")
