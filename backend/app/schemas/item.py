from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: str | None = None
    category: str
    rarity: str | None = None
    icon_url: str | None = None


class ItemResponse(ItemBase):
    id: int

    model_config = {"from_attributes": True}
