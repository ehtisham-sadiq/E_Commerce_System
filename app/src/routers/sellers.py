from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.src.database import get_session
from app.src.domain.seller import service
from app.src.domain.seller.schemas import SellerOut, SellerCreate, SellerUpdate
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/sellers/", response_model=SellerOut, status_code=status.HTTP_201_CREATED)
async def create_seller(seller: SellerCreate, db: Session = Depends(get_session)):
    try:
        return await service.create_seller(db=db, seller=seller)
    except Exception as e:
        logger.error(f"Error creating seller: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/sellers/{seller_id}", response_model=SellerOut)
async def read_seller(seller_id: int, db: Session = Depends(get_session)):
    db_seller = await service.get_seller_by_id(db=db, seller_id=seller_id)
    if db_seller is None:
        logger.warning(f"Seller with ID {seller_id} not found.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seller not found")
    return db_seller

@router.get("/sellers/", response_model=list[SellerOut])
async def read_sellers(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    return await service.get_sellers(db=db, skip=skip, limit=limit)

@router.put("/sellers/{seller_id}", response_model=SellerOut)
async def update_seller(seller_id: int, seller: SellerUpdate, db: Session = Depends(get_session)):
    db_seller = await service.update_seller(db=db, seller_id=seller_id, seller=seller)
    if db_seller is None:
        logger.warning(f"Attempt to update non-existent seller with ID {seller_id}.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seller not found")
    return db_seller

@router.delete("/sellers/{seller_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_seller(seller_id: int, db: Session = Depends(get_session)):
    db_seller = await service.delete_seller(db=db, seller_id=seller_id)
    if db_seller is None:
        logger.warning(f"Attempt to delete non-existent seller with ID {seller_id}.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seller not found")
