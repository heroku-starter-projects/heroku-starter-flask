from flask import g, request
from flask_restful import Resource
from marshmallow import Schema, fields, validate
import pydash as _

from app.middlewares.validation import validate_query
from app.models.food_truck import FoodTruck


class FoodTrucksRequestSchema(Schema):
    latitude = fields.Float(required=True, validate=validate.Range(min=-90, max=90))
    longitude = fields.Float(required=True, validate=validate.Range(min=-180, max=180))
    limit = fields.Int(missing=5, validate=validate.Range(min=1))
    radius = fields.Float(missing=5, validate=validate.Range(min=0.1))


class FoodTrucks(Resource):

    @validate_query(FoodTrucksRequestSchema())
    def get(self):
        """
        Endpoint to find the closest food trucks to a given latitude and longitude.
        """
        # Get query parameters
        latitude, longitude, limit, radius = _.at(
            g.args, "latitude", "longitude", "limit", "radius"
        )

        # Find closest food trucks within the radius
        closest_trucks = FoodTruck.find_closest_in_memory(
            g.session, latitude, longitude, limit, radius
        )

        result = []
        for truck, distance in closest_trucks:
            truck_dict = truck.dump()
            truck_dict["distance"] = distance
            result.append(
                _.pick(
                    truck_dict, ["locationid", "applicant", "coordinates", "distance"]
                )
            )

        return {"closest_food_trucks": result}, 200


class FoodTrucksPostgis(Resource):

    @validate_query(FoodTrucksRequestSchema())
    def get(self):
        """
        Endpoint to find the closest food trucks to a given latitude and longitude.

        Query Parameters:
        - `latitude` (float): Latitude of the location.
        - `longitude` (float): Longitude of the location.
        - `limit` (int, optional): Maximum number of results to return. Default is 5.
        - `radius` (float, optional): Maximum distance (in kilometers) to include. Default is 5 km.

        Returns:
        - JSON response containing the closest food trucks and their distances.
        """
        # Get query parameters
        latitude, longitude, limit, radius = _.at(
            g.args, "latitude", "longitude", "limit", "radius"
        )

        # Find closest food trucks within the radius
        closest_trucks = FoodTruck.find_closest(
            g.session, latitude, longitude, limit, radius
        )

        result = []
        for truck, distance in closest_trucks:
            truck_dict = truck.dump()
            truck_dict["distance"] = distance
            result.append(
                _.pick(
                    truck_dict, ["locationid", "applicant", "coordinates", "distance"]
                )
            )

        return {"closest_food_trucks": result}, 200
