from flask_login import UserMixin
from sqlalchemy import Column, String
from werkzeug.security import check_password_hash, generate_password_hash

from app import login_manager
from app.libs.error_code import LoginFirst
from app.model.base import Base


class Driver(UserMixin, Base):
    __tablename__ = 'driver'
    fields = ['license_plate', 'username', 'nickname']
    username = Column(String(100), primary_key=True)
    license_plate = Column(String(100))
    password_ = Column('password', String(200), nullable=False)
    nickname = Column(String(100))

    @property
    def id(self):
        return self.username

    def check_password(self, raw):
        if not self.password_ or not raw:
            return False
        return check_password_hash(self.password_, raw)

    @property
    def password(self):
        return self.password_

    @password.setter
    def password(self, raw):
        self.password_ = generate_password_hash(raw)

    @staticmethod
    @login_manager.user_loader
    def load_user(id_):
        return Driver.get_by_id(id_)

    @staticmethod
    @login_manager.unauthorized_handler
    def unauthorized_handler():
        return LoginFirst()
