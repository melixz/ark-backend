#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for PostgreSQL to start..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Применяем миграции, собираем статические файлы
python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"
