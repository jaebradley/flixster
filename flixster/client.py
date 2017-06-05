import requests

from flixster.query.parameter_builders import TheaterInformationQueryParameterBuilder
from flixster.query import SearchType


class FlixsterClient:
    BASE_URL = "https://api.flixster.com"
    BASE_V1_URL = "{BASE_URL}/ticketing/api/v1".format(BASE_URL=BASE_URL)
    BASE_V2_URL = "{BASE_URL}/api/v2".format(BASE_URL=BASE_URL)
    OTHER_BASE_URL = "https://www.flixster.com/api"

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_geolocation_information():
        r = requests.get(url="{BASE_V1_URL}/geoip".format(BASE_V1_URL=FlixsterClient.BASE_V1_URL))

        r.raise_for_status()

        return r.json()

    @staticmethod
    def get_theater_information(query):
        query_parameters = TheaterInformationQueryParameterBuilder.build(query)

        r = requests.get(url="{BASE_V2_URL}/ticketing/theaters".format(BASE_V2_URL=FlixsterClient.BASE_V2_URL),
                         params=query_parameters)

        r.raise_for_status()

        return r.json()

    @staticmethod
    def search(term, type=SearchType.ANY, limit=5):
        r = requests.get(url="{BASE_URL}/search".format(BASE_URL=FlixsterClient.OTHER_BASE_URL),
                         params={
                             "q": term,
                             "count": limit,
                             "any": type.value
                         })

        r.raise_for_status()

        return r.json()
