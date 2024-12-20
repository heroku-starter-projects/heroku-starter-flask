import datetime
import jwt
from sqlalchemy import Column, Integer, Text
from marshmallow import Schema, fields

from app.config import Config

from app.models.base import Base


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    name = fields.Str()
    password = fields.Str()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(Text, unique=True)
    name = Column(Text, nullable=False)
    password = Column(Text, nullable=False)

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    def dump(self):
        return UserSchema().dump(self)

    def generate_token(self):
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=15),
            "iat": datetime.datetime.utcnow(),
            "sub": self.id,
        }

        return jwt.encode(
            payload,
            Config.JWT_SECRET,
            algorithm=Config.JWT_ALGORITHM,
        )
