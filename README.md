# Apache Log Aggregator

## Описание

Агрегатор данных из access логов веб-сервера Apache с сохранением в базу данных.

## Установка

1. Клонируйте репозиторий:

git clone https://github.com/Denoff13333/apache-log-aggregator.git


2. Перейдите в директорию проекта:

Открыть терминал, перейти в нужную дерикторию 

C:\Users\Denil\apache2\apache-log-aggregator


3. Создайте и активируйте виртуальное окружение:

python3 -m venv venv

Set-ExecutionPolicy RemoteSigned -Scope Process

venv\Scripts\activate


4. Установите зависимости:

pip install -r requirements.txt

## Использование

### Парсинг логов

Перейти в нужную дерикторию в моем случае :

cd C:\Users\Denil\apache2\apache-log-aggregator\scripts

и выполнить парсинг

python parse_logs.py

### Просмотр данных

python app/main.py view --ip <IP_ADDRESS> --start <START_DATE> --end <END_DATE>

### Статистика по IP-адресам

python app/main.py stats

## Загрузка проекта на github

git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/Denoff13333/apache-log-aggregator.git
git push -u origin master




