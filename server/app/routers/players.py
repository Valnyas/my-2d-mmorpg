from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from ..models import Player

router = APIRouter()

@router.get("/players/count")
async def get_players_count(db: Session = Depends(get_db)):
    count = db.query(func.count(Player.id)).scalar()
    return {"count": count}