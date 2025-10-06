# Diplom_ui_api_tests Galochkina Yuliya

## Автоматизация тестирования на python

### Шаги
1. Склонировать проект 'git clone https://github.com/Jul3872/Diplom_ui_api_tests.git'
2. Установить зависимости
3. Запустить тесты 'pytest':
- pytest - все тесты
- pytest tests/ui/ - только ui тесты
- pytest tests/api/ - только api тесты
4. Создать отчетность
- pytest --alluredir=allure-results - Запуск тестов с сбором данных для Allure
- allure generate allure-files -o allure-report - генерация отчета
5. Открыть отчет 'allure open allure-report'

### Стек
- pytest
- selenium
- requests
- allure
- config

### Структура:

# Структура проекта

- config/ # Конфигурационные файлы
  - __init__.py
  - environment.py # Настройки окружения и URL
  - test_data.py # Тестовые данные
- pages/ # Page Object модели
  - __init__.py
  - base_page.py # Базовый класс для страниц
  - main_page.py # Главная страница
  - search_page.py # Страница поиска
  - advanced_search_page.py # Расширенный поиск
  - film_page.py # Страница фильма
  - media_news_page.py # Страница новостей
- tests/ # Тесты
  - __init__.py
  - conftest.py # Фикстуры pytest
  - api/ # API тесты
    - __init__.py
    - test_api_kinopoisk.py
  - ui/ # UI тесты
    - __init__.py
    - test_ui_kinopoisk.py
- requirements.txt # Зависимости проекта
- README.md # Документация

### Библиотеки
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests
- pip install flake8
