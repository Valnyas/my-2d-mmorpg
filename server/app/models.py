from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .database import Base  # Импортируем Base из database

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    x = Column(Float, default=0.0)
    y = Column(Float, default=0.0)
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<Player {self.username}>"

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    item_type = Column(String)
    description = Column(String, nullable=True)

    def __repr__(self):
        return f"<Item {self.name}>"