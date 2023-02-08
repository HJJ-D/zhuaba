from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime

from app.model.base import Base
from app.model.user import User
from app.model.commodity import Commodity
from app.model.car import Car

class Purchase_History(Base):
    __tablename__ = 'purchase_history'
    fields = ['id', 'car_id', 'username', 'date', 'commodity_id', 'num']
    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(String(50), ForeignKey(Car.car_id))
    username = Column(String(100), ForeignKey(User.username))
    date = Column(String(100))
    commodity_id = Column(Integer, ForeignKey(Commodity.commodity_id))
    num = Column(Integer)