from sqlalchemy import Column, Integer, String
from app.src.database import Base

class Buyer(Base):
    __tablename__ = "buyers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact = Column(String)

    def __repr__(self):
        return f"<Buyer(id={self.id}, name={self.name}, contact={self.contact})>"
    