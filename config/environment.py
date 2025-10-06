"""Настройки окружения"""
import os
from dotenv import load_dotenv

load_dotenv()


class EnvironmentConfig:
    """Конфигурация окружения"""

    # Базовые URL
    KINOPOISK_BASE_URL = "https://kinopoiskapiunofficial.tech"
    KINOPOISK_WEB_URL = "https://www.kinopoisk.ru"
    BASE_URL = KINOPOISK_WEB_URL

    # API Endpoints
    API_V2_1 = f"{KINOPOISK_BASE_URL}/api/v2.1"
    API_V2_2 = f"{KINOPOISK_BASE_URL}/api/v2.2"
    API_V1 = f"{KINOPOISK_BASE_URL}/api/v1"

    # Конкретные endpoints
    SEARCH_BY_KEYWORD_URL = f"{API_V2_1}/films/search-by-keyword"
    FILM_DETAILS_URL = f"{API_V2_2}/films"
    FILMS_WITH_FILTERS_URL = f"{API_V2_2}/films"
    PREMIERES_URL = f"{API_V2_2}/films/premieres"
    STAFF_URL = f"{API_V1}/staff"

    # Web URLs
    MEDIA_NEWS_URL = f"{KINOPOISK_WEB_URL}/media/news/"

    # API Key (из переменных окружения)
    API_KEY = os.getenv(
        'KINOPOISK_API_KEY', 'b6f97ee6-e064-4e27-8730-8890da3e1a20')

    # Настройки тестов
    WAIT_TIMEOUT = 15
    IMPLICIT_WAIT = 10
    BROWSER = "chrome"
