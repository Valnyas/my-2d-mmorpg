#!/bin/bash
# Скрипт запуска для FastAPI на Render

echo "Starting FastAPI application..."
exec uvicorn app.main:app --host 0.0.0.0 --port 10000