# ProCharity_back_2.0

<details>
  <summary>Оглавление</summary>
  <ol>
    <li>
      <a href="#описание">Описание</a>
      <ul>
        <li><a href="#технологии">Технологии</a></li>
      </ul>
    </li>
    <li>
      <a href="#установка-и-запуск">Установка и запуск</a>
      <ul>
        <li><a href="#установка-приложения">Установка приложения</a></li>
        <li><a href="#запуск">Запуск</a></li>
      </ul>
    </li>
    <li><a href="#использование">Использование</a></li>
    <li>
      <a href="#полезная-информация">Полезная информация</a>
      <ul>
        <li><a href="#регистрация-бота-telegram">Регистрация бота Telegram</a></li>
        <li>
          <a href="#режимы-работы-бота">Режимы работы бота</a>
          <ul>
            <li><a href="#запуск-без-api-приложения">Запуск без API приложения</a></li>
            <li><a href="#polling">Polling</a></li>
            <li><a href="#webhook">Webhook</a></li>
          </ul>
        </li>
        <li>
          <a href="#работа-с-базой-данных">Работа с базой данных</a>
          <ul>
            <li><a href="#создание-миграций">Создание миграций</a></li>
            <li><a href="#откат-миграций">Откат миграций</a></li>
          </ul>
        </li>
        <li>
          <a href="#работа-с-poetry">Работа с Poetry</a>
          <ul>
            <li><a href="#активировать-виртуальное-окружение">Активировать виртуальное окружение</a></li>
            <li><a href="#добавить-зависимость">Добавить зависимость</a></li>
            <li><a href="#запустить-скрипт-без-активации-виртуального-окружения">Запустить скрипт без активации виртуального окружения</a></li>
          </ul>
        </li>
        <li><a href="#использование-ngrok">Использование Ngrok</a></li>
        <li><a href="#переменные-окружения-env">Переменные окружения (.env)</a></li>
      </ul>
    </li>
  </ol>
</details>

### Описание

Создание чат-бота в Telegram для платформы интеллектуального волонтерства 
ProCharity (НКО Фонд Друзья).

Сайт [https://procharity.ru/](https://procharity.ru/)

Чат-бот @ProCharity_bot

Платформа представляет собой агрегатор волонтерских заданий от различных 
благотворительных проектов - любой желающий согласно своим желаниям и 
умениям может откликаться на конкретные предложения благотворительных 
проектов о волонтерской помощи, в свою очередь благотворительный проект/фонд 
выбирает из всех откликов подходящих кандидатов.

Чат-бот реализует функционал волонтерской платформы в приложении Telegram - 
с помощью JSON рассылает подписчикам новые появляющиеся задания от фондов.

### Технологии

[![FastAPI][FastAPI-badge]][FastAPI-url]
[![Python-telegram-bot][Python-telegram-bot-badge]][Python-telegram-bot-url]
[![Postgres][Postgres-badge]][Postgres-url]
[![Nginx][Nginx-badge]][Nginx-url]

## Установка и запуск

### Установка приложения

1. Клонировать репозиторий.

    ```shell
    git clone https://github.com/Studio-Yandex-Practicum/ProCharity_back_2.0.git
    cd ProCharity_back_2.0
    ```

2. Установить зависимости и активировать виртуальное окружение.

    ```shell
    poetry install
    poetry shell
    ```

    > **Note**
    > [Документация по установке Poetry](https://python-poetry.org/docs/#installation)

3. Переименовать [`.env.example`](.env.example) в `.env` и задать переменные окружения.

    ```dotenv
    BOT_TOKEN=<Токен аутентификации бота>
    ```

    > **Note**
    > Полный список переменных окружения проекта находится в 
    > разделе "[Переменные окружения (.env)](#переменные-окружения-env)".

    > **Note**
    > Для получения токена аутентификации бота обратитесь к 
    > разделу "[Регистрация бота Telegram](#регистрация-бота-telegram)".

### Запуск

1. Применить миграции базы данных.

    ```shell
    alembic upgrade head
    ```

2. Запустить сервер приложения.

    ```shell
    uvicorn src:app --reload
    ```

## Использование

После выполнения инструкций, описанных в разделе "[Установка и Запуск](#установка-и-запуск)", 
будет запущен FastAPI-сервер по адресу http://localhost:8000.

Также по адресу http://localhost:8000/docs доступна полная документация API.

## Полезная информация

Данный раздел содержит информацию, которая может быть полезна для разработчиков.
Настоятельно рекомендуем каждому прочитать его хотя бы один раз.

### Регистрация бота Telegram

1. Найдите в Telegram бота [@BotFather](https://t.me/botfather) и откройте с ним чат.

2. Напишите ему /newbot.

3. Придумайте и напишите название бота. Оно будет отображаться в контактах и 
чатах. Например, «My Dev Bot».

4. Придумайте и напишите юзернейм. Он используется для упоминания бота и в 
ссылках. Юзернейм должен быть на латинице и обязательно заканчиваться на 
«bot». Например, «my_dev_bot».

5. Готово. BotFather пришлет токен бота — его нужно скопировать в переменную 
окружения BOT_TOKEN (см. в разделе "[Установка и Запуск] (#установка)").

    > **Note**
    > [Документация о боте BotFather](https://core.telegram.org/bots/features#botfather)

### Режимы работы бота

#### Запуск без API приложения

Выполнить скрипт запуска.

```shell
python src/run.py
```

> **Warning**:
> Возможно только в режиме [polling](#polling).

#### Polling

Задать значение переменной окружения (.env).

```dotenv
BOT_WEBHOOK_MODE=False
```

#### Webhook

Задать значение переменным окружения (.env).

```dotenv
BOT_WEBHOOK_MODE=True
APPLICATION_URL=http://example.com  # Пример
```

> **Info**
> Для теста через HTTPS можно использовать Ngrok (см. раздел "[Использование Ngrok](#использование-ngrok)").

### Работа с базой данных

#### Создание миграций

1. Применить существующие миграции:

    ```shell
    alembic upgrade head
    ```

2. Создать новую миграцию:

    ```shell
    alembic revision --autogenerate -m "<Название миграции>"
    ```

    В название миграции указывается
    для какого поля или модели внесены изменения, например:

    * add_shift_model
    * shift_add_field_title
    * shift_remove_field_title

3. Повторить пункт 1, для применения созданной миграции.

#### Откат миграций

Откатить последнюю миграцию:

```shell
alembic downgrade -1
```

### Работа с Poetry

В этом разделе представлены наиболее часто используемые команды.

Подробнее: https://python-poetry.org/docs/cli/

#### Активировать виртуальное окружение

```shell
poetry shell
```

#### Добавить зависимость

```shell
poetry add <package_name>
```

> **Note**
> Использование флага `--dev (-D)` позволяет установить зависимость,
> необходимую только для разработки.
> Это полезно для разделения develop и prod зависимостей.

#### Запустить скрипт без активации виртуального окружения

```shell
poetry run <script_name>.py
```

### Использование Ngrok

Этот раздел будет полезен, если у вас нет доменного имени с установленным 
SSL-сертификатом.

Ngrok — это инструмент, который позволяет создавать временный общедоступный 
адрес (туннель) для вашего локального сервера, находящимся за NAT или 
брандмауэром.

Подробнее: https://ngrok.com/

1. Установить, следуя официальным инструкциям.

    https://ngrok.com/download

2. Запустить туннель.

    ```shell
    ngrok http 80
    ```

3. Задать значение переменной окружения (.env).

    ```dotenv
    APPLICATION_URL=https://1234-56-78-9.eu.ngrok.io  # Пример
    ```

### Переменные окружения (.env)

```dotenv
# Переменные приложения
APPLICATION_URL=  # Домен, на котором развернуто приложение
DEBUG=False  # Включение(True) | Выключение(False) режима отладки
ROOT_PATH=/api/  # Для корректной работы без прокси ставится пустая строка, для работы с прокси "/api/"
BOT_TOKEN=  # Токен аутентификации бота
BOT_WEBHOOK_MODE=False  # Запустить бота в режиме webhook(True) | polling(False)
# Переменные базы данных
POSTGRES_DB=procharity_back_db_local  # Название базы данных
POSTGRES_USER=postgres  # Логин для подключения к базе данных
POSTGRES_PASSWORD=postgres  # Пароль для подключения к базе данных
DB_HOST=localhost  # Название сервиса (контейнера)
DB_PORT=5432  # Порт для подключения к базе данных
```

<!-- MARKDOWN LINKS & BADGES -->

[FastAPI-url]: https://fastapi.tiangolo.com/
[FastAPI-badge]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi

[Python-telegram-bot-url]: https://github.com/python-telegram-bot/python-telegram-bot
[Python-telegram-bot-badge]: https://img.shields.io/badge/python--telegram--bot-2CA5E0?style=for-the-badge

[Postgres-url]: https://www.postgresql.org/
[Postgres-badge]: https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white

[Nginx-url]: https://nginx.org
[Nginx-badge]: https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white~~
