import os
import sys
# To run from cmd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from django.test import Client
from django.urls import reverse


class TestClouds(unittest.TestCase):
    """Test endpoint to get list of cloud providers"""
    def setUp(self):
        """Use django test client"""
        self.client = Client()
        self.url = reverse('clouds')
        munich_coords = (48.13743, 11.57549)

        self.coordinates = {
            'latitude': munich_coords[0],
            'longitude': munich_coords[1]
        }

    def test_get_all(self):
        """Test all bookings returned"""
        response = self.client.get(self.url, data=self.coordinates, content_type='application/json').json()
        self.assertTrue(len(response) > 1, 'No data found')

    def test_get_by_aws(self):
        """Test filter by aws provider"""
        data = {'provider': 'aws'}
        data.update(self.coordinates)
        response = self.client.get(self.url, data=data, content_type='application/json').json()
        self.assertTrue(response[0]['cloud_name'].startswith(data['provider']), 'Cannot filter with provider aws')

    def test_get_by_google(self):
        """Test filter by google provider"""
        data = {'provider': 'google'}
        data.update(self.coordinates)
        response = self.client.get(self.url, data=data, content_type='application/json').json()
        self.assertTrue(response[0]['cloud_name'].startswith(data['provider']), 'Cannot filter with provider google')

    def test_get_by_nearest(self):
        """Test filter by nearest region"""
        data = {'provider': 'all', 'nearest': 'true'}
        data.update(self.coordinates)
        response = self.client.get(self.url, data=data, content_type='application/json').json()
        self.assertTrue(len(response) < 6, 'Cannot filter with nearest flag')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
