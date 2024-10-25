from pydantic import BaseModel

class BuyerCreate(BaseModel):
    name: str
    contact: str

class BuyerUpdate(BaseModel):
    name: str | None = None
    contact: str | None = None

class BuyerOut(BaseModel):
    id: int
    name: str
    contact: str

    class Config:
        orm_mode = True
