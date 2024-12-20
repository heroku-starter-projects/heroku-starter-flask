from sqlalchemy import Column, Integer, String, DateTime, Text, func
from marshmallow import Schema, fields
from geoalchemy2 import Geometry
from sqlalchemy.orm import Session
from sqlalchemy.orm import object_session

from app.models.base import Base


class FoodTruckSchema(Schema):
    locationid = fields.Int()
    applicant = fields.Str()
    facility_type = fields.Str()
    location_description = fields.Str()
    address = fields.Str()
    blocklot = fields.Str()
    block = fields.Str()
    lot = fields.Str()
    permit = fields.Str()
    status = fields.Str()
    food_items = fields.Str()
    location_geo = fields.Str()
    coordinates = fields.Method("get_coordinates")

    def get_coordinates(self, obj):
        session = object_session(obj)  # Get the session for the object
        if session is None:
            return None  # Coordinates cannot be resolved without a session

        lat = session.query(func.ST_Y(obj.coordinates)).scalar()
        lon = session.query(func.ST_X(obj.coordinates)).scalar()

        return {"latitude": lat, "longitude": lon}


class FoodTruck(Base):
    __tablename__ = "food_trucks"

    locationid = Column(Integer, primary_key=True)
    applicant = Column(Text)
    facility_type = Column(String(50))
    location_description = Column(Text)
    address = Column(Text)
    blocklot = Column(String(20))
    block = Column(String(20))
    lot = Column(String(20))
    permit = Column(String(50))
    status = Column(String(50))
    food_items = Column(Text)
    coordinates = Column(Geometry("POINT"))
    schedule = Column(Text)
    dayshours = Column(String(100))
    noise_sent = Column(DateTime)
    approved = Column(DateTime)
    received = Column(DateTime)
    prior_permit = Column(Integer)
    expiration_date = Column(DateTime)
    location_geo = Column(Text)
    fire_prevention_districts = Column(Integer)
    police_districts = Column(Integer)
    supervisor_districts = Column(Integer)
    zip_codes = Column(Integer)
    neighborhoods_old = Column(Integer)

    def dump(self):
        return FoodTruckSchema().dump(self)

    @staticmethod
    def find_closest(
        session: Session, latitude: float, longitude: float, limit: int = 5
    ):
        """
        Finds the closest food trucks to a given latitude and longitude.

        :param session: SQLAlchemy Session object.
        :param latitude: Latitude of the point.
        :param longitude: Longitude of the point.
        :param limit: Number of closest food trucks to return.
        :return: List of closest FoodTruck objects.
        """
        point = func.ST_SetSRID(func.ST_Point(longitude, latitude), 4326)
        return (
            session.query(FoodTruck)
            .order_by(func.ST_Distance(FoodTruck.coordinates, point))
            .limit(limit)
            .all()
        )
