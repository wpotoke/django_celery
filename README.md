# Django Celery Project

Этот проект демонстрирует интеграцию Django с Celery для обработки фоновых задач. Проект использует Redis в качестве брокера задач и для хранения результатов.

## Содержание

- [Технологии](#%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8)
- [Запуск проекта](#%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
- [Функциональность](#%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C)
- [Команда проекта](#%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B0-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)

## Технологии

- Django
- Celery
- Redis
- PostgreSQL

## Запуск проекта

1. Установите зависимости:
    
    bash
    
    Копировать код
    
    `pip install -r requirements.txt`
    
2. Запустите Redis и Celery:
    
    bash
    
    Копировать код
    
    `redis-server celery -A django_celery worker -l info`
    
3. Запустите сервер Django:
    
    bash
    
    Копировать код
    
    `python manage.py runserver`
    

## Функциональность

- Отправка фоновых задач через Celery.
- Кэширование с использованием Redis.
- Поддержка PostgreSQL для хранения данных.

## Команда проекта

- **[Морозов Данила](https://t.me/amigos_mixtapes)** — Back-End Engineer
