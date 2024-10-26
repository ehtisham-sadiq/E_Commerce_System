from app.src.domain.sellers.models import Seller
from app.src.domain.sellers.schemas import SellerOut

class SellerConverter:
    @staticmethod
    def convert(seller: Seller) -> SellerOut:
        return SellerOut.from_orm(seller)

    @staticmethod
    def convert_many(sellers: list[Seller]) -> list[SellerOut]:
        return [SellerConverter.convert(seller) for seller in sellers]
