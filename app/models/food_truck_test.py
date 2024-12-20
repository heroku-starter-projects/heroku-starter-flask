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

        # Coordinates for the test
        cls.test_lat = 35.17370598710992
        cls.test_long = -114.00505988023178
        cls.expected_results = [
            {
                "applicant": "Park's Catering",
                "coordinates": {
                    "latitude": 37.730906150359694,
                    "longitude": -122.37330257748522,
                },
                "distance": 800,
            },
            {
                "applicant": "Park's Catering",
                "coordinates": {
                    "latitude": 37.73213495192223,
                    "longitude": -122.37539807856734,
                },
                "distance": 800,
            },
            {
                "applicant": "Singh Brothers Ice Cream",
                "coordinates": {
                    "latitude": 37.72943828845401,
                    "longitude": -122.37665780072307,
                },
                "distance": 800,
            },
            {
                "applicant": "Park's Catering",
                "coordinates": {
                    "latitude": 37.726382932182176,
                    "longitude": -122.37843478266778,
                },
                "distance": 800,
            },
            {
                "applicant": "Liang Bai Ping",
                "coordinates": {
                    "latitude": 37.72578913981244,
                    "longitude": -122.37897271962358,
                },
                "distance": 800,
            },
        ]

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    # python -m unittest app.models.food_truck_test.FoodTruckTestCase.test_100_find_closest -v
    def test_100_find_closest(self):

        # Call the find_closest method
        closest_trucks = FoodTruck.find_closest(
            self.session,
            self.test_lat,
            self.test_long,
            limit=5,
            radius=8000,
        )

        # Validate the results
        assert len(closest_trucks) <= 5, "Should return at most 5 results"

        actual_results = []
        for truck, distance in closest_trucks:
            assert isinstance(
                truck, FoodTruck
            ), "Result should be an instance of FoodTruck"
            truck_dict = truck.dump()
            truck_dict["distance"] = distance
            actual_results.append(
                _.pick(truck_dict, ["applicant", "coordinates", "distance"])
            )
            actual_results[-1]["distance"] = int(actual_results[-1]["distance"])

        assert actual_results == self.expected_results, actual_results

    # python -m unittest app.models.food_truck_test.FoodTruckTestCase.test_101_find_closest_by_distance -v
    def test_101_find_closest_by_distance(self):

        # Call the find_closest method
        closest_trucks = FoodTruck.find_closest(
            self.session,
            self.test_lat,
            self.test_long,
            limit=5,
            radius=800.5051578101001,
        )

        # Validate the results
        assert len(closest_trucks) <= 5, "Should return at most 5 results"

        actual_results = []
        for truck, distance in closest_trucks:
            assert isinstance(
                truck, FoodTruck
            ), "Result should be an instance of FoodTruck"
            truck_dict = truck.dump()
            truck_dict["distance"] = distance
            actual_results.append(
                _.pick(truck_dict, ["applicant", "coordinates", "distance"])
            )
            actual_results[-1]["distance"] = int(actual_results[-1]["distance"])

        assert actual_results == self.expected_results[:3], actual_results

    # python -m unittest app.models.food_truck_test.FoodTruckTestCase.test_200_find_closest_in_memory -v
    def test_200_find_closest_in_memory(self):
        # Call the find_closest method
        closest_trucks = FoodTruck.find_closest_in_memory(
            self.session,
            self.test_lat,
            self.test_long,
            limit=5,
            radius=8000,
        )

        # Validate the results
        assert len(closest_trucks) <= 5, "Should return at most 5 results"

        actual_results = []
        for truck, distance in closest_trucks:
            assert isinstance(
                truck, FoodTruck
            ), "Result should be an instance of FoodTruck"
            truck_dict = truck.dump()
            truck_dict["distance"] = distance
            actual_results.append(
                _.pick(truck_dict, ["applicant", "coordinates", "distance"])
            )
            actual_results[-1]["distance"] = int(actual_results[-1]["distance"])

        assert actual_results == self.expected_results, actual_results

    # python -m unittest app.models.food_truck_test.FoodTruckTestCase.test_200_find_closest_in_memory -v
    def test_200_find_closest_in_memory(self):
        # Call the find_closest method
        closest_trucks = FoodTruck.find_closest_in_memory(
            self.session,
            self.test_lat,
            self.test_long,
            limit=5,
            radius=8000,
        )

        # Validate the results
        assert len(closest_trucks) <= 5, "Should return at most 5 results"

        actual_results = []
        for truck, distance in closest_trucks:
            assert isinstance(
                truck, FoodTruck
            ), "Result should be an instance of FoodTruck"
            truck_dict = truck.dump()
            truck_dict["distance"] = distance
            actual_results.append(
                _.pick(truck_dict, ["applicant", "coordinates", "distance"])
            )
            actual_results[-1]["distance"] = int(actual_results[-1]["distance"])

        assert actual_results == self.expected_results, actual_results

    # python -m unittest app.models.food_truck_test.FoodTruckTestCase.test_201_find_closest_in_memory_by_distance -v
    def test_201_find_closest_in_memory_by_distance(self):
        # Call the find_closest method
        closest_trucks = FoodTruck.find_closest_in_memory(
            self.session,
            self.test_lat,
            self.test_long,
            limit=5,
            radius=800.7553519017798,
        )

        # Validate the results
        assert len(closest_trucks) <= 5, "Should return at most 5 results"

        actual_results = []
        for truck, distance in closest_trucks:
            assert isinstance(
                truck, FoodTruck
            ), "Result should be an instance of FoodTruck"
            truck_dict = truck.dump()
            truck_dict["distance"] = distance
            actual_results.append(
                _.pick(truck_dict, ["applicant", "coordinates", "distance"])
            )
            actual_results[-1]["distance"] = int(actual_results[-1]["distance"])

        assert actual_results == self.expected_results[:3], actual_results
