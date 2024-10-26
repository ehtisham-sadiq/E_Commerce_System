from sqlalchemy import Column, Integer, String
from app.src.database import Base
from sqlalchemy.orm import relationship

class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_details = Column(String)
    address = Column(String)

    # Define the relationship to Stock
    stocks = relationship("Stock", back_populates="seller")

    def __repr__(self):
        return f"<Seller(id={self.id}, name={self.name}, contact_details={self.contact_details})>"
