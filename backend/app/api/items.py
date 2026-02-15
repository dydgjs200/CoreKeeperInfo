from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.item import Item
from app.schemas.item import ItemResponse

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=list[ItemResponse])
def get_items(
    category: str | None = None,
    search: str | None = None,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=50, ge=1, le=100),
    db: Session = Depends(get_db),
):
    query = db.query(Item)
    if category:
        query = query.filter(Item.category == category)
    if search:
        query = query.filter(Item.name.ilike(f"%{search}%"))
    return query.offset(skip).limit(limit).all()


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    return db.query(Item).filter(Item.id == item_id).first()
