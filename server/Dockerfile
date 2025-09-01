FROM python:3.11-slim-bookworm

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Копируем весь код
COPY . .

# Делаем скрипт запуска исполняемым
RUN chmod +x start.sh

# Используем наш скрипт запуска
CMD ["./start.sh"]