# Используем Python 3.9 как базовый образ
FROM python:3.9-slim

# Устанавливаем необходимые пакеты и зависимости
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    build-essential \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости и gunicorn в одном шаге
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Копируем все файлы проекта
COPY . /app/

# Указываем переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Копируем и добавляем файл entrypoint
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Открываем порт приложения
EXPOSE 8000

# Запускаем entrypoint
ENTRYPOINT ["/entrypoint.sh"]
