from unittest import TestCase

from datetime import date

from flixster.query.parameter_builders import TheaterInformationQueryParameterBuilder
from flixster.query import TheaterInformationQuery


class TestQueryParameterBuilder(TestCase):
    query_date = date(year=2017, month=1, day=1)
    return_complete_movie_info = "return complete movie info"
    limit = "limit"
    return_show_times = "return show times"

    def test_should_build_without_movie_id(self):
        query_without_movie_id = TheaterInformationQuery(date=self.query_date,
                                                         return_complete_movie_info=self.return_complete_movie_info,
                                                         return_show_times=self.return_show_times,
                                                         movie_id=None,
                                                         limit=self.limit)
        expected = {
            "date": self.query_date.strftime("%Y%m%d"),
            "deviceType": TheaterInformationQueryParameterBuilder.ROTTEN_TOMATOES_CODE,
            "fullMovieInfo": self.return_complete_movie_info,
            "limit": self.limit,
            "showTimes": self.return_show_times,
            "vanityPlatform": TheaterInformationQueryParameterBuilder.ROTTEN_TOMATOES_CODE
        }

        self.assertEqual(expected, TheaterInformationQueryParameterBuilder.build(query_without_movie_id))

    def test_should_build_with_movie_id(self):
        query_with_movie_id = TheaterInformationQuery(date=self.query_date,
                                                         return_complete_movie_info=self.return_complete_movie_info,
                                                         return_show_times=self.return_show_times,
                                                         movie_id="movie id",
                                                         limit=self.limit)

        expected = {
            "date": self.query_date.strftime("%Y%m%d"),
            "deviceType": TheaterInformationQueryParameterBuilder.ROTTEN_TOMATOES_CODE,
            "fullMovieInfo": self.return_complete_movie_info,
            "limit": self.limit,
            "showTimes": self.return_show_times,
            "vanityPlatform": TheaterInformationQueryParameterBuilder.ROTTEN_TOMATOES_CODE,
            "movie": "movie id"
        }

        self.assertEqual(expected, TheaterInformationQueryParameterBuilder.build(query_with_movie_id))
