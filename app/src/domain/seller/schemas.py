from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class SellerBase(BaseModel):
    name: str = Field(..., description="The name of the seller")
    contact_details: EmailStr = Field(..., description="The contact details of the seller, must be a valid email")
    address: Optional[str] = Field(None, description="The address of the seller")

class SellerCreate(SellerBase):
    pass

class SellerUpdate(BaseModel):
    name: Optional[str] = Field(None, description="Updated name of the seller")
    contact_details: Optional[EmailStr] = Field(None, description="Updated contact details of the seller, must be a valid email")
    address: Optional[str] = Field(None, description="Updated address of the seller")

class SellerOut(SellerBase):
    id: int = Field(..., description="Unique identifier of the seller")

    class Config:
        from_attributes = True
