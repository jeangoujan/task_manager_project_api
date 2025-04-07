# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем зависимости для Poetry
RUN pip install --upgrade pip && \
    pip install poetry

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем pyproject.toml и poetry.lock для установки зависимостей
COPY pyproject.toml poetry.lock /app/

# Устанавливаем зависимости через Poetry
RUN poetry install --no-root

# Копируем весь проект в контейнер
COPY . /app/

# Открываем порт 8000 для Django
EXPOSE 8000

# Команда для запуска сервера
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
