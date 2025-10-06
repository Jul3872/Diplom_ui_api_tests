"""Тестовые данные для API и UI тестов"""


class TestData:
    """Тестовые данные"""

    # API тесты
    class API:
        # Поиск по ключевым словам
        SEARCH_KEYWORD = "Ocean's Thirteen"
        SEARCH_FILM_ID = 251879
        SEARCH_FILM_DATA = {
            'filmId': 251879,
            'nameRu': "Тринадцать друзей Оушена",
            'nameEn': "Ocean's Thirteen",
            'type': "FILM",
            'year': "2007",
            'filmLength': "02:02",
            'rating': "7.7",
            'ratingVoteCount': 173866,
            'description_keywords': ["Дэнни Оушена", "Лас-Вегасе"],
            'countries': ["США"],
            'genres': ["криминал", "триллер"]
        }

        # Фильтры
        FILTERS_DATA = {
            'countries': 1,        # США
            'genres': 8,           # Биография
            'order': 'RATING',
            'type': 'ALL',
            'ratingFrom': 10,
            'ratingTo': 10,
            'yearFrom': 2025,
            'yearTo': 2025,
            'page': 1
        }

        # Премьеры
        PREMIERES_DATA = {
            'year': 2025,
            'month': 'JANUARY',
            'expected_total': 60,
            'first_film': {
                'kinopoiskId': 5047471,
                'nameRu': "Волшебник Изумрудного города. Дорога "
                "из жёлтого кирпича",
                'year': 2024,
                'countries': ["Россия"],
                'genres': ["фэнтези", "приключения", "семейный"]
            }
        }

        # Съемочная группа
        STAFF_DATA = {
            'film_id': 251879,
            'first_person': {
                'staffId': 27407,
                'nameRu': "Стивен Содерберг",
                'nameEn': "Steven Soderbergh",
                'professionText': "Режиссеры",
                'professionKey': "DIRECTOR"
            }
        }

    # UI тесты
    class UI:
        # Поисковые запросы
        SEARCH_FILM_NAME = "Матрица"
        SEARCH_NEGATIVE_QUERY = "НесуществующийФильм12345"
        # SEARCH_TV_CHANNEL = "Первый канал"
        # SEARCH_CHANNELS = ["НТВ", "Россия 1", "ТНТ", "СТС"]

        # Фильтры расширенного поиска
        ADVANCED_SEARCH_FILTERS = {
            'year_from': '2020',
            'year_to': '2023',
            'country': 'США'
        }

        # Ожидаемые тексты
        MEDIA_NEWS_TITLE = "Читать последние новости кино на Кинопоиске"
        NO_RESULTS_TEXT = "ничего не найдено"

        # Навигационные элементы
        NAV_MENU_ITEMS = [
            "Главная", "Онлайн-кинотеатр", "Фильмы", "Сериалы",
            "Телеканалы", "Спорт", "Подписки", "Билеты в кино"
        ]

    # Заголовки для API
    HEADERS = {
        'accept': 'application/json',
        'X-API-KEY': None  # Будет установлено из environment
    }
