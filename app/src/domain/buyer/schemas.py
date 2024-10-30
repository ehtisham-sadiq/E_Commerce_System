from pydantic import BaseModel
from typing import Optional

class BuyerCreate(BaseModel):
    name: str
    contact: str

class BuyerUpdate(BaseModel):
    name: Optional[str] = None
    contact: Optional[str] = None

class BuyerOut(BaseModel):
    id: int
    name: str
    contact: str

    class Config:
        orm_mode = True
