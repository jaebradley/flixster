from unittest import TestCase

from flixster.query import TheaterInformationQuery

from flixster.client import FlixsterClient


class FlixsterClientIntegrationTest(TestCase):
    def test_get_geolocation_information(self):
        geolocation_information = FlixsterClient.get_geolocation_information()
        self.assertIsNotNone(geolocation_information)
        self.assertTrue("area_code" in geolocation_information)
        self.assertTrue("city" in geolocation_information)
        self.assertTrue("country_code" in geolocation_information)
        self.assertTrue("country_name" in geolocation_information)
        self.assertTrue("dma_code")
        self.assertTrue("latitude")
        self.assertTrue("longitude")
        self.assertTrue("metro_code")
        self.assertTrue("postal_code")
        self.assertTrue("region")

    def test_get_theater_information(self):
        query = TheaterInformationQuery()
        theater_information = FlixsterClient.get_theater_information(query)
        self.assertIsNotNone(theater_information)
        self.assertTrue("movies" in theater_information)
        self.assertTrue("presentations" in theater_information)
        self.assertTrue("theaterGroups" in theater_information)
        self.assertTrue("theaters" in theater_information)
        self.assertTrue("traits" in theater_information)