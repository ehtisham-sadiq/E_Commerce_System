from pydantic import BaseModel
from typing import Optional

class SellerCreate(BaseModel):
    name: str
    contact_details: str
    address: str

class SellerUpdate(BaseModel):
    name: Optional[str] = None
    contact_details: Optional[str] = None
    address: Optional[str] = None

class SellerOut(BaseModel):
    id: int
    name: str
    contact_details: str
    address: str

    class Config:
        orm_mode = True
