from sqlmodel import Field
from .base import Base

class Treasure(Base, table=True):
    __tablename__ = "treasures"

    treasure_type: str
    value: str
    dragon_id: int = Field(default=None, foreign_key="dragons.id")
