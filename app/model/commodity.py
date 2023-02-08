from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Float

from app.model.base import Base
from app.model.car import Car

class Commodity(Base):
    __tablename__ = 'commodity'
    fields = ['car_id', 'commodity_id', 'commodity_name', 'price', 'remaining_num', 'image']
    car_id = Column(String(50), ForeignKey(Car.car_id))
    commodity_id = Column(Integer, primary_key=True)
    commodity_name = Column(String(100))
    price = Column(Float)
    remaining_num = Column(Integer)
    image = Column(String(100))
