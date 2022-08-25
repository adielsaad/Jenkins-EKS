import unittest
import requests


class UnitTest(unittest.TestCase):
    def test_is_weather_up(self):
        self.assertEqual(requests.get("http://52.23.195.175:5000").status_code, 200)

