from sqlmodel import Field
from .base import Base

class Rider(Base, table=True):
    __tablename__ = "riders"

    name: str
    species: str
    dragon_id: int = Field(default=None, foreign_key="dragons.id")
