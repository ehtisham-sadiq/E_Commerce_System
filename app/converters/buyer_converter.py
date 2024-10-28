from app.src.domain.buyer.models import Buyer
from app.src.domain.buyer.schemas import BuyerOut


class BuyerConverter:
    @staticmethod
    def convert(buyer: Buyer) -> BuyerOut:
        return BuyerOut.from_orm(buyer)

    @staticmethod
    def convert_many(buyers: list[Buyer]) -> list[BuyerOut]:
        return [BuyerConverter.convert(buyer) for buyer in buyers]
