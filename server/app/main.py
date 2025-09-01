from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base  # Теперь импорт должен работать
from . import models  # Важно: импортируем модели для создания таблиц

# Создаем таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI(title="2D MMORPG API", version="0.1.0")

# CORS для разработки
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Для продакшена укажите конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в 2D MMORPG API!"}

@app.get("/health")
def health_check():
    return {
        "status": "healthy", 
        "service": "2D MMORPG Backend",
        "version": "0.1.0"
    }

# Простой эндпоинт для теста базы данных
@app.get("/test-db")
def test_db():
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        return {"database": "connected"}
    except Exception as e:
        return {"database": "error", "message": str(e)}

# Для обслуживания статических файлов (в продакшене)
# app.mount("/", StaticFiles(directory="../client", html=True), name="client")