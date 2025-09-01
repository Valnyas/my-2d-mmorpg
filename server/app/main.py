from fastapi import FastAPI

# Создаем экземпляр приложения - переменная должна называться "app"
app = FastAPI(title="2D MMORPG API")

@app.get("/")
def read_root():
    return {"message": "2D MMORPG Server is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}