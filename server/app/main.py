from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import players

# Создаем таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI(title="2D MMORPG API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутеры
app.include_router(players.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в 2D MMORPG!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "2D MMORPG Backend"}

# Для обслуживания статических файлов (в продакшене)
app.mount("/", StaticFiles(directory="../client", html=True), name="client")