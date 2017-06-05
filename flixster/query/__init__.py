from datetime import date
from enum import Enum


class SearchType(Enum):
    ANY = "any"
    MOVIES = "movies"


class TheaterInformationQuery:
    def __init__(self, date=date.today(), return_complete_movie_info=True, return_show_times=True, movie_id=None,
                 limit=5):
        self.date = date
        self.return_complete_movie_info = return_complete_movie_info
        self.return_show_times = return_show_times
        self.movie_id = movie_id
        self.limit = limit

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.__dict__ == other.__dict__
            return NotImplemented

        def __ne__(self, other):
            if isinstance(other, self.__class__):
                return not self.__eq__(other)
            return NotImplemented

        def __hash__(self):
            return hash(tuple(sorted(self.__dict__.items())))
