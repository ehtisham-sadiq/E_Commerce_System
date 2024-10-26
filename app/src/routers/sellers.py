from fastapi import APIRouter, HTTPException, Depends
from app.src.domain.sellers.schemas import SellerCreate, SellerUpdate, SellerOut
from app.src.domain.sellers.service import SellerService
from app.src.dependencies import SessionDep

router = APIRouter()

@router.post("/sellers", response_model=SellerOut, tags=["Sellers Management"])
async def create_seller(seller: SellerCreate, db: SessionDep):
    seller_service = SellerService(db)
    return await seller_service.create_seller(seller)

@router.get("/sellers", response_model=list[SellerOut], tags=["Sellers Management"])
async def get_sellers(db: SessionDep):
    seller_service = SellerService(db)
    return await seller_service.get_sellers()

@router.get("/sellers/{seller_id}", response_model=SellerOut, tags=["Sellers Management"])
async def get_seller(seller_id: int, db: SessionDep):
    seller_service = SellerService(db)
    seller = await seller_service.get_seller_by_id(seller_id)
    if seller is None:
        raise HTTPException(status_code=404, detail="Seller not found")
    return seller

@router.put("/sellers/{seller_id}", response_model=SellerOut, tags=["Sellers Management"])
async def update_seller(seller_id: int, seller: SellerUpdate, db: SessionDep):
    seller_service = SellerService(db)
    updated_seller = await seller_service.update_seller(seller_id, seller)
    if updated_seller is None:
        raise HTTPException(status_code=404, detail="Seller not found")
    return updated_seller

@router.delete("/sellers/{seller_id}", tags=["Sellers Management"])
async def delete_seller(seller_id: int, db: SessionDep):
    seller_service = SellerService(db)
    result = await seller_service.delete_seller(seller_id)
    if not result:
        raise HTTPException(status_code=404, detail="Seller not found")
    return {"detail": "Seller deleted successfully"}
