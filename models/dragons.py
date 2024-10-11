from .base import Base 

class Dragon(Base, table=True):
    __tablename__ = "dragons"
    
    name: str
    color: str
    size: str
    breath_weapon: str
    source: str
    summary: str
