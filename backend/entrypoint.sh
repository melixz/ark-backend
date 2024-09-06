#!/bin/bash

# Проверка на существование виртуального окружения
if [ ! -d "/opt/backend/.venv" ]; then
    echo "Virtual environment not found. Creating..."
    python -m venv /opt/backend/.venv
fi

# Активируем виртуальное окружение
source /opt/backend/.venv/bin/activate

# Применяем миграции
python manage.py migrate

# Собираем статические файлы
python manage.py collectstatic --noinput

# Запускаем uwsgi
exec uwsgi --http :8000 --module backend.wsgi
