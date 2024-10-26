from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.src.domain.seller.models import Seller
from app.src.domain.seller.schemas import SellerCreate, SellerUpdate
from fastapi import HTTPException

def create_seller(db: Session, seller: SellerCreate) -> Seller:
    db_seller = Seller(**seller.dict())
    try:
        db.add(db_seller)
        db.commit()
        db.refresh(db_seller)
    except IntegrityError:
        db.rollback()  # Rollback the session in case of error
        raise HTTPException(status_code=400, detail="Seller already exists")
    return db_seller

def get_seller_by_id(db: Session, seller_id: int) -> Seller | None: 
    return db.query(Seller).filter(Seller.id == seller_id).first()

def get_sellers(db: Session, skip: int = 0, limit: int = 10) -> list[Seller]:
    return db.query(Seller).offset(skip).limit(limit).all()

def update_seller(db: Session, seller_id: int, seller: SellerUpdate) -> Seller | None:
    db_seller = get_seller_by_id(db, seller_id) 
    if db_seller:
        for key, value in seller.dict(exclude_unset=True).items():
            setattr(db_seller, key, value)
        db.commit()
        db.refresh(db_seller)
        return db_seller
    raise HTTPException(status_code=404, detail="Seller not found")
    
def delete_seller(db: Session, seller_id: int) -> Seller | None:
    db_seller = get_seller_by_id(db, seller_id) 
    if db_seller:
        db.delete(db_seller)
        db.commit()
        return db_seller
    raise HTTPException(status_code=404, detail="Seller not found")
