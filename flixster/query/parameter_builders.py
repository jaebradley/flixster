class TheaterInformationQueryParameterBuilder:
    ROTTEN_TOMATOES_CODE = "RTO"

    @staticmethod
    def build(query):
        parameters = {
            "date": query.date.strftime("%Y%m%d"),
            "deviceType": TheaterInformationQueryParameterBuilder.ROTTEN_TOMATOES_CODE,
            "fullMovieInfo": query.return_complete_movie_info,
            "limit": query.limit,
            "showtimes": query.return_show_times,
            "vanityPlatform": TheaterInformationQueryParameterBuilder.ROTTEN_TOMATOES_CODE
        }

        if query.movie_id is not None:
            parameters["movie"] = query.movie_id

        return parameters
