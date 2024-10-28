from app.src.domain.sales.models import Sale
from app.src.domain.sales.schemas import SaleOut


class SaleConverter:
    @staticmethod
    def convert(sale: Sale) -> SaleOut:
        return SaleOut.from_orm(sale)

    @staticmethod
    def convert_many(sales: list[Sale]) -> list[SaleOut]:
        return [SaleConverter.convert(sale) for sale in sales]
