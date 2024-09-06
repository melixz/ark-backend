# backend/backend.dockerfile
FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /opt/backend

# Устанавливаем pip и обновляем его
RUN python -m pip install --upgrade pip

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости глобально в системное окружение контейнера
RUN pip install -r requirements.txt

# Копируем весь проект
COPY . .

# Экспонируем порт
EXPOSE 8000

# Применяем миграции и запускаем сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
