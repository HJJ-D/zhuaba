from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Float

from app.model.base import Base
from app.model.driver import Driver

class Car(Base):
    __tablename__ = 'car'
    fields = ['car_id', 'driver_id', 'driver_name', 'car_model']
    car_id = Column(String(50), primary_key=True)
    driver_id = Column(String(50), ForeignKey(Driver.driver_id))
    driver_name = Column(String(50))
    car_model = Column(String(100))
