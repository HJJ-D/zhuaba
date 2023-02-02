from flask_login import UserMixin
from sqlalchemy import Column, Integer, String

from app import login_manager
from app.libs.error_code import LoginFirst
from app.model.base import Base


class User(UserMixin, Base):
    __tablename__ = 'user'
    fields = ['username']
    username = Column(String(100), primary_key=True)

    @property
    def id(self):
        return self.username

    @staticmethod
    @login_manager.user_loader
    def load_user(id_):
        return User.get_by_id(id_)

    @staticmethod
    @login_manager.unauthorized_handler
    def unauthorized_handler():
        return LoginFirst()