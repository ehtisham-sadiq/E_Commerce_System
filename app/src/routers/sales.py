from fastapi import APIRouter, HTTPException, Depends
from app.src.domain.sales.schemas import SaleCreate, SaleOut
from app.src.domain.sales.service import SaleService
from app.src.dependencies import SessionDep
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/sales", response_model=SaleOut, tags=["Sales Management"])
async def create_sale(sale: SaleCreate, db: SessionDep):
    sale_service = SaleService(db)
    return await sale_service.create_sale(sale)

@router.get("/sales", response_model=list[SaleOut], tags=["Sales Management"])
async def get_sale(db: SessionDep):
    sale_service = SaleService(db)
    return await sale_service.get_sale()

@router.get("/sales/{sale_id}", response_model=SaleOut, tags=["Sales Management"])
async def get_sale(sale_id: int, db: SessionDep):
    sale_service = SaleService(db)
    sale = await sale_service.get_sale_by_id(sale_id)
    if sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale
