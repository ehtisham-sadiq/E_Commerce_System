from .models import Buyer
from app.src.domain.buyer.schemas import BuyerCreate, BuyerUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

class BuyerService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_buyer(self, buyer_data: BuyerCreate) -> Buyer:
        buyer = Buyer(**buyer_data.dict())
        self.db.add(buyer)
        await self.db.commit()
        await self.db.refresh(buyer)
        return buyer

    async def get_buyers(self) -> list[Buyer]:
        result = await self.db.execute(select(Buyer))
        return result.scalars().all()

    async def get_buyer_by_id(self, buyer_id: int) -> Buyer | None:
        return await self.db.get(Buyer, buyer_id)

    async def update_buyer(self, buyer_id: int, buyer_data: BuyerUpdate) -> Buyer | None:
        buyer = await self.get_buyer_by_id(buyer_id)
        if buyer:
            for key, value in buyer_data.dict(exclude_unset=True).items():
                setattr(buyer, key, value)
            await self.db.commit()
            await self.db.refresh(buyer)
            return buyer
        return None

    async def delete_buyer(self, buyer_id: int) -> bool:
        buyer = await self.get_buyer_by_id(buyer_id)
        if buyer:
            await self.db.delete(buyer)
            await self.db.commit()
            return True
        return False
