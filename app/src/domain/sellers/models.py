from sqlalchemy import Column, Integer, String
from app.src.database import Base

class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_details = Column(String)
    address = Column(String)

    def __repr__(self):
        return f"<Seller(id={self.id}, name={self.name}, contact_details={self.contact_details}, address={self.address})>"
