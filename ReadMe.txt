#-----------------------------#
 Используется Python 3.12
#-----------------------------#
Docker: python:3.12-alpine3.19
#-----------------------------#

Разрешения на компьютере для запуска виртуального окружения:
-Разрешить скрипты для окружения
 Set-ExecutionPolicy AllSigned
-Запретить скрипты для окружения
 Set-ExecutionPolicy Restricted
-Проверка разрешения
 Get-ExecutionPolicy


Установка виртуального окружения
 py -3 -m venv venv
Запуск виртуального окружения если не установилось по умолчанию
 venv/Scripts/activate


Установка необходимых компонентов для автотестов с нуля:
 pip install selenium pytest webdriver-manager allure-pytest dotenv
 pip freeze > requirements.txt

Установка необходимых компонентов для автотестов из файла:
 pip install -r requirements.txt

Запуск тестов с генерацией файлов для отчета
 pytest --alluredir=allure-results

Генерация Alluer файлов 
 allure generate allure-results --clean -o allure-report 