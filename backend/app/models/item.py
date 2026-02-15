from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    category = Column(String(100), nullable=False, index=True)
    rarity = Column(String(50), nullable=True)
    icon_url = Column(String(500), nullable=True)
