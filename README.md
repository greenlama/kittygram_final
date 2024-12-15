[![Main Kittygram workflow](https://github.com/greenlama/kittygram_final/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/greenlama/kittygram_final/actions/workflows/main.yml)

# Проект Kittygram

Kittygram - это социальная сеть для владельцев кошек, где можно делиться фотографиями своих питомцев, базовой информацией о них, их достижениями.

## Основные функции

- **Регистрация и аутентификация:** Пользователи могут создать учетную запись и входить с помощью неё в систему.
- **Публикация фото:** Пользователи могут загружать фотографии своих кошек.
- **Указание базовых параметров:** Пользователи могут указать такие базовые параметры, как имя, возраст и цвет кошки, а также достижения своих питомцев

## Используемые технологии

Python 3.9, Django 3.2.16, JWT, PostgreSQL, Docker, Docker Compose, Nginx

## Развертывание проекта

Деплой проекта выполняется автоматически с помощью GitHub Actions. Для деплоя необходимо предварительно указать на репозитории переменные окружения с помощью secrets.
Список секретов:
- DOCKER_USERNAME
- DOCKER_PASSWORD
- HOST
- USER
- SSH_KEY
- SSH_PASSPHRASE
- TELEGRAM_TO
- TELEGRAM_TOKEN

## Подготовка переменных окружения

На сервере, где будет происходить деплой, необходимо создать в домашнем каталоге пользователя директорию `kittygram`. В каталоге `kittygram` создать файл `.env` со следующими переменными окружения (значения переменных указываются самостоятельно):
```
POSTGRES_DB=kittygram
POSTGRES_USER=kittygram_user
POSTGRES_PASSWORD=kittygram_password
DB_NAME=kittygram
SECRET_KEY=secret
DEBUG=True
ALLOWED_HOSTS=localhost
```

## Автор

[Наиль Камалеев](https://github.com/greenlama)
