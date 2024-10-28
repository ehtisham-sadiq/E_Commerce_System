from pydantic import BaseModel
from datetime import date

class SaleBase(BaseModel):
    car_id: int
    seller_id: int
    buyer_id: int
    sale_date: date
    price: float

class SaleCreate(SaleBase):
    pass

class SaleOut(SaleBase):
    id: int

    class Config:
        orm_mode = True
