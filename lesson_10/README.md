# Проект автоматизации тестирования (PageObject + Allure)

## Требования
- Python 3.9+
- Установленный Allure Commandline (скачать с [GitHub releases](https://github.com/allure-framework/allure2/releases))
- Браузеры Chrome и Firefox с соответствующими драйверами

## Установка
1. Создайте виртуальное окружение: `python -m venv venv`
2. Активируйте: `venv\Scripts\activate` (Windows) или `source venv/bin/activate` (Linux/macOS)
3. Установите зависимости: `pip install allure-pytest selenium pytest`

## Запуск тестов с генерацией и просмотром Allure-результатов
```bash
pytest --alluredir=allure-results
allure serve allure-results  