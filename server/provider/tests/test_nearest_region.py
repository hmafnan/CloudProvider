import os
import sys
# To run from cmd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from provider import views


class TestNearestRegion(unittest.TestCase):
    """Test nearest distance"""
    def setUp(self):
        """Use coordinates of different cities"""
        self.munich_coords = (48.13743, 11.57549)
        self.passau_coords = (48.5665, 13.4312)
        self.berlin_coords = (52.535152, 13.390206)
        self.london_coords = (51.509865, -0.118092)

    def test_distance(self):
        """Test nearest distances from Munich"""
        near = views.haversine(self.munich_coords, self.passau_coords)
        far = views.haversine(self.munich_coords, self.berlin_coords)
        farther = views.haversine(self.munich_coords, self.london_coords)

        self.assertTrue(near < far, 'Incorrect distance returned')
        self.assertTrue(near < farther, 'Incorrect distance returned')
        self.assertTrue(far < farther, 'Incorrect distance returned')

    def tearDown(self):
        pass
