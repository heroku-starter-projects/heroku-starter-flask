from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text
from marshmallow import Schema, fields

Base = declarative_base()


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    name = fields.Str()
    password = fields.Str()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(Text)
    name = Column(Text)
    password = Column(Text)

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    def dump(self):
        return UserSchema().dump(self)
