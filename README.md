# Django Task Manager
Простой и эффективный менеджер задач на Django с функционалом для командной работы.
С использованием SQLite и Стандартной аутентификацией.
## Содержание
- [Технологии](#технологии)
- [Установка и запуск](#установка-и-запуск)
- [Функционал](#функционал)
- [Контакты](#контакты)

## Технологии
- [Python 3.8+](https://www.python.org/)
- [Django 4.0+](https://docs.djangoproject.com/en/5.2/)
- [SQLite3](https://sqlite.org/)
- [Django стандартная аутентификация](https://docs.djangoproject.com/en/5.2/topics/auth/)

## Установка и запуск
1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/django-task-manager.git
cd django-task-manager
```
2. Создайте виртуальное окружение и активируйте его:

```bash
python -m venv venv
source venv/bin/activate  #Для Linux/Mac
#или
venv\Scripts\activate  #Для Windows
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Примените миграции:
```bash
python manage.py migrate
```
5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```
6. Создайте суперпользователя:
```bash
python manage.py runserver
```
7. Откройте браузер и перейдите по адресу http://localhost:8000
## Функционал
### Проекты
- Создание и управление проектами
- Назначение участников проектов
- Просмотр всех задач проекта
### Задачи
- Создание задач с описанием, приоритетом и сроком выполнения
- Назначение исполнителей задач
- Изменение статусов задач
### Пользователи
- Система аутентификации
- Профили пользователей
- Просмотр назначенных задач
### Структура базы данных
Проект использует следующие основные модели:
   - Пользователи (стандартная модель Django User)
   - Проекты (Project)
   - Задачи (Task)
   - Статусы задач (Status)

## Контакты
Егор Иванков - grivankob@gmail.com