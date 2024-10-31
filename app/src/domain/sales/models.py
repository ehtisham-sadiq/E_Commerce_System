from sqlalchemy import Column, Integer, Date, Float
from app.src.database import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, index=True)
    seller_id = Column(Integer)
    buyer_id = Column(Integer)
    sale_date = Column(Date)
    price = Column(Float)

    def __repr__(self):
        return (
            f"<Sale(id={self.id}, car_id={self.car_id}, seller_id={self.seller_id}, "
            f"buyer_id={self.buyer_id}, sale_date={self.sale_date}, price={self.price})>"
        )
