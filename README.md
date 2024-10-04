# Проект Kittygram

## Описание

Kittygram — это социальная сеть, предназначенная для обмена фотографиями любимых питомцев, в частности котов и кошек, а также для публикации их достижений. Проект реализован с использованием контейнеризации и CI/CD на платформе GitHub Actions.

Kittygram представляет собой полностью рабочее приложение, в состав которого входят бэкенд на Django и фронтенд на React.

## Основные функции проекта:

- Регистрация и авторизация пользователей.
- Возможность добавления нового питомца или редактирования информации о существующем.
- Добавление и редактирование достижений питомцев.
- Просмотр записей и достижений других пользователей.

API Kittygram разработан с использованием Django REST Framework и TokenAuthentication для аутентификации, с подключением библиотеки Djoser.

Проект разводится в нескольких Docker-контейнерах. В контейнере бэкенда настроен WSGI-сервер Gunicorn. Автоматизация тестирования и развертывания проекта осуществляется с помощью GitHub Actions.

## Проверка проекта автотестами

Для локального выполнения тестов создайте виртуальное окружение, установите зависимости из backend/requirements.txt и выполните команду pytest в корневой директории проекта.

## Настройка CI/CD

Развертывание проекта на удалённом сервере осуществляется через CI/CD с использованием GitHub Actions. В рамках workflow:

- Проверяется соответствие кода бэкенда стандартам PEP8.
- Настроено автоматическое тестирование как фронтенда, так и бэкенда.
- В случае успешного прохождения тестов образы обновляются на Docker Hub.
- Обновляются образы на сервере и происходит перезапуск приложения с использованием Docker Compose.
- Выполняются команды для сборки статики, её переноса в volume и выполнения миграций.
- Отправляется уведомление в Telegram о успешном завершении развертывания.

Пример этого workflow сохранён в файле kittygram_workflow.yml в корневом каталоге проекта. При необходимости его можно перенести в .github/workflows/main.yml для запуска.

Сохраните следующие переменные с необходимыми значениями в секретах GitHub Actions:

```
DOCKER_USERNAME - логин в Docker Hub
DOCKER_PASSWORD - пароль для Docker Hub
SSH_KEY - закрытый SSH-ключ для доступа к продакшен-серверу
SSH_PASSPHRASE - passphrase для этого ключа
USER - username для доступа к продакшен-серверу
HOST - адрес хоста для доступа к продакшен-серверу
TELEGRAM_TO - ID своего телеграм-аккаунта
TELEGRAM_TOKEN - токен Telegram-бота
```

Файл docker-compose.yml для локального запуска проекта и файл docker-compose.production.yml для запуска проекта на облачном сервере находятся в корневой директории проекта.

### Стек: 
- Python 3.9.
- Django 3.2.3
- Django Rest Framework 3.12.4
- PostgreSQL
- Docker
- Nginx
- Gunicorn
- GitHub Actions

## Запуск проекта в dev-режиме:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Sasha-Parshintcev/kittygram_final.git
```

Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```

Если у вас Linux/macOS
```
source venv/bin/activate
```
Если у вас windows
```
source venv/scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Задайте учётные данные БД в .env файле, используя .env.example:

```
POSTGRES_USER=логин
POSTGRES_PASSWORD=пароль
POSTGRES_DB=название БД
DB_HOST=название хоста
DB_PORT=5432
SECRET_KEY=django_settings_secret_key
DEBUG=False
ALLOWED_HOSTS=127.0.0.1, localhost
```

Запустить Docker Compose с дефолтной конфигурацией (docker-compose.yml):

Выполнить сборку контейнеров: 
```
sudo docker compose up -d --build
```

Применить миграции:
```
sudo docker compose exec backend python manage.py migrate
```

Создать суперпользователя:
```
sudo docker compose exec backend python manage.py createsuperuser
```

Собрать файлы статики:
```
sudo docker compose exec backend python manage.py collectstatic
```

Скопировать файлы статики в /backend_static/static/ backend-контейнера:
```
sudo docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
```

Перейти по адресу:
```
127.0.0.1:8000
```

## Примеры запросов:

Пример GET-запроса на просмотр списка достижений. 
GET .../api/achievements/
```
[
    {
        "id": 1,
        "achievement_name": "громко бегает по квартире в 5 утра"
    },
    {
        "id": 2,
        "achievement_name": "слишком красив"
    }
]
```

Пример POST-запроса на добавление нового котика.
POST .../api/cats/
```
{
    "name": "Тыгыдык",
    "color": "#FF8C00",
    "birth_year": 2024
}
```

Пример ответа:
```
{
    "id": 1,
    "name": "Тыгыдык",
    "color": "darkorange",
    "birth_year": 2024,
    "achievements": ["громко бегает по квартире в 5 утра"],
    "owner": 2,
    "age": 0,
    "image": null
}
```

## Проект разработан:
 - [Sasha-Parshintcev (в роли Python-разработчика)](https://github.com/Sasha-Parshintcev)