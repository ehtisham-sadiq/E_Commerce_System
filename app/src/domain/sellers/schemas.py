from pydantic import BaseModel

class SellerCreate(BaseModel):
    name: str
    contact_details: str
    address: str

class SellerUpdate(BaseModel):
    name: str | None = None
    contact_details: str | None = None
    address: str | None = None

class SellerOut(BaseModel):
    id: int
    name: str
    contact_details: str
    address: str

    class Config:
        orm_mode = True
