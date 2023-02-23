from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from app.model.base import Base
from app.model.commodity import Commodity
from app.model.user import User


class Purchase_History(Base):
    __tablename__ = 'purchase_history'
    fields = ['id', 'username', 'date', 'commodity_id', 'num']
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), ForeignKey(User.username))
    date = Column(DateTime)
    commodity_id = Column(Integer, ForeignKey(Commodity.commodity_id))
    num = Column(Integer)
