from sqlalchemy import Column, Integer, String, Float

from app.model.base import Base


class Commodity(Base):
    __tablename__ = 'commodity'
    fields = ['commodity_id', 'commodity_name', 'price', 'remaining_num', 'image']
    commodity_id = Column(Integer, primary_key=True, autoincrement=True)
    commodity_name = Column(String(100))
    price = Column(Float)
    remaining_num = Column(Integer)
    image = Column(String(100))
