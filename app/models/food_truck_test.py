import unittest
from app.models.food_truck import FoodTruck, Base
from app.config import Config
from app.helpers.database import generate_connection_string, sqlalchemy_session
import pydash as _


class FoodTruckTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up database connection
        cls.session = sqlalchemy_session(generate_connection_string())

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    # python -m unittest app.models.food_truck_test.FoodTruckTestCase.test_100_find_closest -v
    def test_100_find_closest(self):
        # Coordinates for the test
        test_lat = 35.17370598710992
        test_long = -114.00505988023178

        # Call the find_closest method
        closest_trucks = FoodTruck.find_closest(
            self.session,
            test_lat,
            test_long,
            limit=5,
        )

        # Validate the results
        assert len(closest_trucks) <= 5, "Should return at most 5 results"
        expected_results = [
            {
                "applicant": "Park's Catering",
                "coordinates": {
                    "latitude": 37.730906150359694,
                    "longitude": -122.37330257748522,
                },
            },
            {
                "applicant": "Park's Catering",
                "coordinates": {
                    "latitude": 37.73213495192223,
                    "longitude": -122.37539807856734,
                },
            },
            {
                "applicant": "Singh Brothers Ice Cream",
                "coordinates": {
                    "latitude": 37.72943828845401,
                    "longitude": -122.37665780072307,
                },
            },
            {
                "applicant": "Park's Catering",
                "coordinates": {
                    "latitude": 37.726382932182176,
                    "longitude": -122.37843478266778,
                },
            },
            {
                "applicant": "Liang Bai Ping",
                "coordinates": {
                    "latitude": 37.72578913981244,
                    "longitude": -122.37897271962358,
                },
            },
        ]
        actual_results = []
        for truck in closest_trucks:
            assert isinstance(
                truck, FoodTruck
            ), "Result should be an instance of FoodTruck"
            truck_dict = truck.dump()
            actual_results.append(_.pick(truck_dict, ["applicant", "coordinates"]))

        assert actual_results == expected_results, actual_results
