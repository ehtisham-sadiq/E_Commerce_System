from typing import List
from app.src.domain.seller.models import Seller
from app.src.domain.seller.schemas import SellerOut
from fastapi import HTTPException

def convert(seller: Seller) -> SellerOut:
    if seller is None:
        raise HTTPException(status_code=404, detail="Seller not found")
        
    return SellerOut(
        id=seller.id,
        name=seller.name,
        contact_details=seller.contact_details,
        address=seller.address
    )

def convert_many(sellers: List[Seller]) -> List[SellerOut]:
    if not sellers:  # Handle empty list case
        return []
        
    return [convert(seller) for seller in sellers]
