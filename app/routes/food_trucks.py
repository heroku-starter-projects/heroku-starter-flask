from flask import g, request
from flask_restful import Resource

from app.middlewares.auth import requires_auth
from app.models.food_truck import FoodTruck
import pydash as _


class FoodTrucks(Resource):

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
        latitude = request.args.get("latitude", type=float)
        longitude = request.args.get("longitude", type=float)
        limit = request.args.get("limit", default=5, type=int)
        radius = request.args.get("radius", default=5, type=float)

        # Validate inputs
        if latitude is None or longitude is None:
            return {"error": "latitude and longitude are required parameters"}, 400

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
        latitude = request.args.get("latitude", type=float)
        longitude = request.args.get("longitude", type=float)
        limit = request.args.get("limit", default=5, type=int)
        radius = request.args.get("radius", default=5, type=float)

        # Validate inputs
        if latitude is None or longitude is None:
            return {"error": "latitude and longitude are required parameters"}, 400

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
