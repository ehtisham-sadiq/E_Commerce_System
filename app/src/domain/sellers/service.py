from .models import Seller
from app.src.domain.sellers.schemas import SellerCreate, SellerUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

class SellerService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_seller(self, seller_data: SellerCreate) -> Seller:
        seller = Seller(**seller_data.dict())
        self.db.add(seller)
        await self.db.commit()
        await self.db.refresh(seller)
        return seller

    async def get_sellers(self) -> list[Seller]:
        result = await self.db.execute(select(Seller))
        return result.scalars().all()

    async def get_seller_by_id(self, seller_id: int) -> Seller | None:
        return await self.db.get(Seller, seller_id)

    async def update_seller(self, seller_id: int, seller_data: SellerUpdate) -> Seller | None:
        seller = await self.get_seller_by_id(seller_id)
        if seller:
            for key, value in seller_data.dict(exclude_unset=True).items():
                setattr(seller, key, value)
            await self.db.commit()
            await self.db.refresh(seller)
            return seller
        return None

    async def delete_seller(self, seller_id: int) -> bool:
        seller = await self.get_seller_by_id(seller_id)
        if seller:
            await self.db.delete(seller)
            await self.db.commit()
            return True
        return False
