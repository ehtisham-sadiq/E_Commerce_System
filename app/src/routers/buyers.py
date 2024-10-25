from fastapi import APIRouter, HTTPException, Depends
from app.src.domain.buyer.schemas import BuyerCreate, BuyerUpdate, BuyerOut
from app.src.domain.buyer.service import BuyerService
from app.src.dependencies import SessionDep
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/buyers", response_model=BuyerOut, tags=["Buyers Management"])
async def create_buyer(buyer: BuyerCreate, db: SessionDep):
    buyer_service = BuyerService(db)
    return await buyer_service.create_buyer(buyer)

@router.get("/buyers", response_model=list[BuyerOut], tags=["Buyers Management"])
async def get_buyers(db: SessionDep):
    buyer_service = BuyerService(db)
    return await buyer_service.get_buyers()

@router.get("/buyers/{buyer_id}", response_model=BuyerOut, tags=["Buyers Management"])
async def get_buyer(buyer_id: int, db: SessionDep):
    buyer_service = BuyerService(db)
    buyer = await buyer_service.get_buyer_by_id(buyer_id)
    if buyer is None:
        raise HTTPException(status_code=404, detail="Buyer not found")
    return buyer

@router.put("/buyers/{buyer_id}", response_model=BuyerOut, tags=["Buyers Management"])
async def update_buyer(buyer_id: int, buyer: BuyerUpdate, db: SessionDep):
    buyer_service = BuyerService(db)
    updated_buyer = await buyer_service.update_buyer(buyer_id, buyer)
    if updated_buyer is None:
        raise HTTPException(status_code=404, detail="Buyer not found")
    return updated_buyer

@router.delete("/buyers/{buyer_id}", tags=["Buyers Management"])
async def delete_buyer(buyer_id: int, db: SessionDep):
    buyer_service = BuyerService(db)
    result = await buyer_service.delete_buyer(buyer_id)
    if not result:
        raise HTTPException(status_code=404, detail="Buyer not found")
    return {"detail": "Buyer deleted successfully"}
