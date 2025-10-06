"""API тесты Кинопоиска"""
from config.environment import EnvironmentConfig
from config.test_data import TestData
import allure


class TestKinopoiskAPI:
    """Все API тесты Кинопоиска"""

    @allure.step("Тест поиска фильма 'Ocean's Thirteen' по ключевым словам")
    def test_search_oceans_thirteen(self, api_client):
        """Тест поиска фильма 'Ocean's Thirteen' по ключевым словам"""
        print("\n🔍 API Тест 1: Поиск по ключевым словам")

        params = {
            'keyword': TestData.API.SEARCH_KEYWORD,
            'page': 1
        }

        response = api_client.get(
            EnvironmentConfig.SEARCH_BY_KEYWORD_URL,
            params=params
        )

        # Основные проверки
        assert response.status_code == 200
        data = response.json()

        # Проверка структуры ответа
        assert data['keyword'] == TestData.API.SEARCH_KEYWORD
        assert data['pagesCount'] == 0
        assert isinstance(data['films'], list)
        assert len(data['films']) > 0

        # Проверка первого фильма в результатах
        film = data['films'][0]
        film_data = TestData.API.SEARCH_FILM_DATA

        # Проверка основных полей фильма
        assert film['filmId'] == film_data['filmId']
        assert film['nameRu'] == film_data['nameRu']
        assert film['nameEn'] == film_data['nameEn']
        assert film['type'] == film_data['type']
        assert film['year'] == film_data['year']
        assert film['filmLength'] == film_data['filmLength']
        assert film['rating'] == film_data['rating']
        assert film['ratingVoteCount'] == film_data['ratingVoteCount']

        print("✅ Поиск по ключевым словам выполнен успешно")

    @allure.step("Тест получения информации о фильме по ID")
    def test_get_film_by_id(self, api_client):
        """Тест получения информации о фильме по ID"""
        print("\n🎬 API Тест 2: Получение данных фильма по ID")

        film_id = TestData.API.SEARCH_FILM_ID

        response = api_client.get(
            f"{EnvironmentConfig.FILM_DETAILS_URL}/{film_id}"
        )

        # Проверка статуса
        assert response.status_code == 200

        data = response.json()

        # Проверка основных идентификаторов
        assert data['kinopoiskId'] == film_id
        assert data['nameRu'] == TestData.API.SEARCH_FILM_DATA['nameRu']
        assert data['nameOriginal'] == TestData.API.SEARCH_FILM_DATA['nameEn']

        # Проверка рейтингов
        assert data['ratingKinopoisk'] == float(
            TestData.API.SEARCH_FILM_DATA['rating'])
        assert (
            data['ratingKinopoiskVoteCount'] ==
            TestData.API.SEARCH_FILM_DATA['ratingVoteCount']
        )

        print("✅ Данные фильма по ID получены успешно")

    @allure.step("Тест получения фильмов с фильтрами")
    def test_films_with_filters(self, api_client):
        """Тест получения фильмов с фильтрами"""
        print("\n🎯 API Тест 3: Поиск с фильтрами")

        params = TestData.API.FILTERS_DATA

        response = api_client.get(
            EnvironmentConfig.FILMS_WITH_FILTERS_URL,
            params=params
        )

        # Проверка статуса
        assert response.status_code == 200

        data = response.json()

        # Проверка структуры ответа
        assert 'total' in data
        assert 'totalPages' in data
        assert 'items' in data

        # Проверка пагинации
        assert data['total'] == 100
        assert data['totalPages'] == 5
        assert isinstance(data['items'], list)
        assert len(data['items']) >= 10

        print("✅ Поиск с фильтрами выполнен успешно")

    @allure.step("Тест получения премьер за январь 2025")
    def test_premieres_january_2025(self, api_client):
        """Тест получения премьер за январь 2025"""
        print("\n📅 API Тест 4: Получение премьер")

        params = TestData.API.PREMIERES_DATA

        response = api_client.get(
            EnvironmentConfig.PREMIERES_URL,
            params=params
        )

        # Проверка статуса
        assert response.status_code == 200

        data = response.json()

        # Проверка структуры ответа
        assert 'total' in data
        assert 'items' in data

        # Проверка пагинации
        assert data['total'] == TestData.API.PREMIERES_DATA['expected_total']
        assert isinstance(data['items'], list)
        assert len(data['items']) > 0

        print("✅ Данные о премьерах получены успешно")

    @allure.step("Тест получения съемочной группы по ID фильма")
    def test_get_staff_by_film_id(self, api_client):
        """Тест получения съемочной группы по ID фильма"""
        print("\n👥 API Тест 5: Получение съемочной группы")

        film_id = TestData.API.STAFF_DATA['film_id']

        response = api_client.get(
            f"{EnvironmentConfig.STAFF_URL}?filmId={film_id}"
        )

        # Проверка статуса
        assert response.status_code == 200

        data = response.json()

        # Проверка что это список
        assert isinstance(data, list)
        assert len(data) > 0

        print("✅ Данные съемочной группы получены успешно")
