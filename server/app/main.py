from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI(title="2D MMORPG API", version="0.1.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Время запуска сервера
SERVER_START_TIME = time.time()

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в 2D MMORPG API!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "2D MMORPG Backend"}

@app.get("/api/uptime")
def get_uptime():
    """Возвращает время работы сервера"""
    uptime_seconds = time.time() - SERVER_START_TIME
    hours = int(uptime_seconds // 3600)
    minutes = int((uptime_seconds % 3600) // 60)
    seconds = int(uptime_seconds % 60)
    return {"uptime": f"{hours}ч {minutes}м {seconds}с"}

@app.get("/api/players/count")
def get_players_count():
    """Заглушка для количества игроков"""
    return {"count": 0}