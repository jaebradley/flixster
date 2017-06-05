# Flixster Python Client

## Introduction
Flixster Python Client for identifying movie show times

## Install
`pip install flixster`

## Client

### Geolocation
Flixster API returns geolocation information for a given request

#### HTTP Request
`https://api.flixster.com/ticketing/api/v1/geoip`

#### Example Response
```json
{
    "area_code": 617,
    "city": "Cambridge",
    "country_code": "US",
    "country_name": "United States",
    "dma_code": 506,
    "latitude": 42.364594,
    "longitude": -71.1028,
    "metro_code": 506,
    "postal_code": "02139",
    "region": "MA"
}
```

#### Client Method
The `get_geolocation_information` does not take any arguments and just returns location metadata from Flixster.

### Search

#### HTTP Request
Search celebrities and movies with term "grint" - return one result 

`https://www.flixster.com/api/search/\?q\=grint\&t\=celebrities\&count\=1`

#### Example Response
```json
{
    "celebs": [
        {
            "id": 162655376,
            "name": "Rupert Grint",
            "photo": {
                "profile": "http://resizing.flixster.com/4t26vNdKwrEfgWH1-xNn3GFPw9E=/275x230/v1.cjs0MDgxODtqOzE3MzI4OzIwNDg7Mjc1OzIzMA",
                "thumbnail": "http://resizing.flixster.com/3wf3FQKcgoFMc1FA0oMfuYsCTnk=/80x80/v1.cjs0MDgxODtqOzE3MzI4OzIwNDg7Mjc1OzIzMA"
            },
            "vanity": "rupert-grint"
        }
    ],
    "movies": [
        {
            "affiliate": {},
            "audienceScore": 87,
            "cast": [
                {
                    "id": 162705076,
                    "name": "Rose McGowan"
                },
                {
                    "id": 162652945,
                    "name": "Kurt Russell"
                },
                {
                    "id": 162654720,
                    "name": "Freddy Rodriguez"
                }
            ],
            "id": 460859831,
            "movietype": "Other",
            "mpaa": "R",
            "playbackAvailable": "",
            "poster": {
                "320X480": "http://resizing.flixster.com/RdQHlnR4_rHRcRgu6wGrcjoQ2vs=/319x426/v1.bTsxMTIxNjcyNjtqOzE3NDM1OzIwNDg7MTUzNjsyMDQ4",
                "detailed": "http://resizing.flixster.com/ufhgKUEVJm94I5gy2BwmegeH0HM=/180x240/v1.bTsxMTIxNjcyNjtqOzE3NDM1OzIwNDg7MTUzNjsyMDQ4",
                "mobile": "http://resizing.flixster.com/bjOm2P26Y1xT2ePek83L6AomuGI=/61x91/v1.bTsxMTIxNjcyNjtqOzE3NDM1OzIwNDg7MTUzNjsyMDQ4",
                "profile": "http://resizing.flixster.com/wYdV5W_UW5udF8S_ASLRfdzDxuc=/120x160/v1.bTsxMTIxNjcyNjtqOzE3NDM1OzIwNDg7MTUzNjsyMDQ4",
                "thumbnail": "http://resizing.flixster.com/X6ZTfFZ_5HT-19nl2yFAhh9YC-U=/54x72/v1.bTsxMTIxNjcyNjtqOzE3NDM1OzIwNDg7MTUzNjsyMDQ4"
            },
            "runningTime": "3 hr. 12 min.",
            "storeAvailable": "",
            "synopsis": "Kill Bill director Quentin Tarantino and Sin City director Robert Rodriguez join forces to offer a cinematic tribute to the...",
            "theaterReleaseDate": "Apr 6, 2007",
            "title": "Grindhouse",
            "tomatometer": 83,
            "url": "http://www.flixster.com/movie/grindhouse/",
            "vanity": "grindhouse",
            "year": 2007
        }
    ]
}
```

#### Client Method
The `search` method takes a `term`, a `SearchType` and a `limit`.

The `term` value represents the value to search celebrities and movies for (duh).

The `SearchType` specifies if the both celebrities and movies should be searched for (`SearchType.ANY`, which is the default), or just movies (`SearchType.MOVIES`). Doesn't seem like there's an "only celebrities" option.

The `limit` specifies the number of search results to return for any of the predefined types (celebrities and/or movies). The default value is `5`.

#### Example
```python
from flixster import FlixsterClient, SearchType

# Search for 5 celebrities and 5 movies with the term "grint"
FlixsterClient.search("grint")
```

### Theater Information

#### HTTP Request
Get tickets and showtimes near Boston, MA
`https://api.flixster.com/api/v2/ticketing/theaters?showtimes=true&postal=02125&fullMovieInfo=true&date=20170605&limit=10&vanityPlatform=FLX`

#### Response
```json
{
  "movies": {
    "12889": {
      "actors": [
        {
          "id": 162653968,
          "name": "Jake Gyllenhaal",
          "url": "http://www.flixster.com/actor/jacob-gyllenhaal"
        },
        {
          "id": 162655292,
          "name": "Jena Malone",
          "url": "http://www.flixster.com/actor/jena-malone"
        },
        {
          "id": 162672845,
          "name": "Mary McDonnell",
          "url": "http://www.flixster.com/actor/mary-mcdonnell"
        },
        {
          "id": 162652402,
          "name": "Drew Barrymore",
          "url": "http://www.flixster.com/actor/drew-barrymore"
        },
        {
          "id": 162660861,
          "name": "Patrick Swayze",
          "url": "http://www.flixster.com/actor/patrick-swayze"
        },
        {
          "id": 369835259,
          "name": "Holmes Osborne",
          "url": "http://www.flixster.com/actor/holmes-osborne"
        },
        {
          "id": 162656288,
          "name": "Katharine Ross",
          "url": "http://www.flixster.com/actor/katharine-ross"
        },
        {
          "id": 326300316,
          "name": "Noah Wyle",
          "url": "http://www.flixster.com/actor/noah-wyle"
        },
        {
          "id": 359853495,
          "name": "Beth Grant",
          "url": "http://www.flixster.com/actor/beth-grant"
        },
        {
          "id": 162663906,
          "name": "Maggie Gyllenhaal",
          "url": "http://www.flixster.com/actor/maggie-gyllenhaal"
        }
      ],
      "id": 12889,
      "isLive": true,
      "isOpening": false,
      "mpaa": "R",
      "poster": {
        "bounded320": "http://resizing.flixster.com/_qGpzMcgDezN5A1UDz6hofCNNKM=/319x426/v1.bTsxMTIwODQ5OTtqOzE3NDQzOzIwNDg7MTIwMDsxNjAw",
        "detailed": "http://resizing.flixster.com/riKnr_0GXuWSCkZMBGWQlpbcuuI=/180x240/v1.bTsxMTIwODQ5OTtqOzE3NDQzOzIwNDg7MTIwMDsxNjAw",
        "original": "http://resizing.flixster.com/5p_CEV3HlhUNbPIt7GWZn3nmhRg=/1200x1600/v1.bTsxMTIwODQ5OTtqOzE3NDQzOzIwNDg7MTIwMDsxNjAw",
        "profile": "http://resizing.flixster.com/0WSWntbq7TLSOuq0sVEnkQM9GKk=/120x160/v1.bTsxMTIwODQ5OTtqOzE3NDQzOzIwNDg7MTIwMDsxNjAw",
        "thumbnail": "http://resizing.flixster.com/nohEatSrzXpSAnvd3_G4E_JJtmI=/54x72/v1.bTsxMTIwODQ5OTtqOzE3NDQzOzIwNDg7MTIwMDsxNjAw"
      },
      "releaseDate": "2001-01-19",
      "reviews": {
        "flixster": {
          "average": "3.0986053943634033",
          "likeability": 80,
          "numNotInterested": 13289010,
          "numScores": 12953196,
          "numWantToSee": 4741354,
          "popcornScore": 80
        },
        "rottenTomatoes": {
          "certifiedFresh": true,
          "consensus": "Richard Kelly's debut feature Donnie Darko is a daring, original vision, packed with jarring ideas and intelligence and featuring a remarkable performance from Jake Gyllenhaal as the troubled title character.",
          "rating": 86
        }
      },
      "runningTime": "1 hr. 53 min.",
      "title": "Donnie Darko",
      "trailer": {
        "duration": 141,
        "hd": "http://link.theplatform.com/s/NGweTC/media/c_6YpzAjZDxs",
        "high": "http://link.theplatform.com/s/NGweTC/media/c_6YpzAjZDxs",
        "low": "http://link.theplatform.com/s/NGweTC/media/c_6YpzAjZDxs",
        "med": "http://link.theplatform.com/s/NGweTC/media/c_6YpzAjZDxs",
        "thumbnail": "http://resizing.flixster.com/t-jYcYlvZ6s-Tm505YI2t1L9aqg=/171x128/v1.bjsxNTA3MDgxO2o7MTczODc7MjA0ODsyNDA7MzIw"
      },
      "vanityUrl": "donnie_darko"
    },
    ...
  },
  "presentations": {
    "FOUR_K": {
      "name": "4K Digital"
    },
    "IMAX": {
      "name": "IMAX"
    },
    "IMAX_3D": {
      "name": "IMAX 3D"
    },
    "IMAX_3D_4K": {
      "name": "IMAX 3D 4K Digital"
    },
    "IMAX_4K": {
      "name": "IMAX 4K Digital"
    },
    "STANDARD": {
      "name": "Standard"
    },
    "THREE_D": {
      "name": "3D"
    },
    "THREE_D_4K": {
      "name": "3D 4K Digital"
    }
  },
  "theaterGroups": [
    {
      "code": "LT_MILES_1",
      "name": "Within 1 mile",
      "theaters": [
        326248374,
        322226695
      ]
    },
    {
      "code": "LT_MILES_3",
      "name": "Within 3 miles",
      "theaters": [
        322226750,
        322226679,
        322226711
      ]
    }
  ],
  "theaters": {
    "322226679": {
      "address": {
        "city": "Arlington",
        "distance": "1.8437287250826606",
        "latitude": 42.4057,
        "longitude": -71.1425,
        "state": "Massachusetts",
        "street": "204 Massachusetts Ave",
        "zip": "02474"
      },
      "callablePhone": "781 648-4340",
      "hasFees": true,
      "id": 322226679,
      "map": "https://maps.googleapis.com/maps/api/staticmap?size=320x416&mobile=true&markers=42.4057,-71.1425&key=ABQIAAAAmh60bCh6aRNYTTulPkdt_xQDeg5NCYrtubnm2qs0dCXcP5UNZRQMMYeECRhphsy1A-GrXRMr5mbuVg",
      "movies": [
        {
          "id": 771381404,
          "presentations": [
            {
              "name": "STANDARD",
              "traitGroups": [
                {
                  "performances": [
                    {
                      "code": "S2043386311",
                      "isoDate": "2017-06-03T12:45:00.000-04:00"
                    },
                    {
                      "code": "S2043386312",
                      "isoDate": "2017-06-03T15:00:00.000-04:00"
                    },
                    {
                      "code": "S2043386313",
                      "isoDate": "2017-06-03T17:10:00.000-04:00"
                    },
                    {
                      "code": "S2043386314",
                      "isoDate": "2017-06-03T19:20:00.000-04:00"
                    },
                    {
                      "code": "S2043386315",
                      "isoDate": "2017-06-03T21:30:00.000-04:00"
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "id": 771324803,
          "presentations": [
            {
              "name": "STANDARD",
              "traitGroups": [
                {
                  "performances": [
                    {
                      "code": "S2043386341",
                      "isoDate": "2017-06-03T12:30:00.000-04:00"
                    },
                    {
                      "code": "S2043386342",
                      "isoDate": "2017-06-03T15:45:00.000-04:00"
                    },
                    {
                      "code": "S2043386343",
                      "isoDate": "2017-06-03T16:45:00.000-04:00"
                    },
                    {
                      "code": "S2043386344",
                      "isoDate": "2017-06-03T19:00:00.000-04:00"
                    },
                    {
                      "code": "S2043386345",
                      "isoDate": "2017-06-03T20:00:00.000-04:00"
                    },
                    {
                      "code": "S2043386346",
                      "isoDate": "2017-06-03T22:00:00.000-04:00"
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "id": 771385707,
          "presentations": [
            {
              "name": "STANDARD",
              "traitGroups": [
                {
                  "performances": [
                    {
                      "code": "S2045643011",
                      "isoDate": "2017-06-03T13:30:00.000-04:00"
                    },
                    {
                      "code": "S2045643012",
                      "isoDate": "2017-06-03T16:30:00.000-04:00"
                    },
                    {
                      "code": "S2045643013",
                      "isoDate": "2017-06-03T19:30:00.000-04:00"
                    },
                    {
                      "code": "S2045643014",
                      "isoDate": "2017-06-03T22:15:00.000-04:00"
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "id": 771456300,
          "presentations": [
            {
              "name": "STANDARD",
              "traitGroups": [
                {
                  "performances": [
                    {
                      "code": "S2043386351",
                      "isoDate": "2017-06-03T19:45:00.000-04:00"
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "id": 771447745,
          "presentations": [
            {
              "name": "STANDARD",
              "traitGroups": [
                {
                  "performances": [
                    {
                      "code": "S2043386321",
                      "isoDate": "2017-06-03T13:20:00.000-04:00"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ],
      "name": "Capitol Theatre",
      "phone": "(781) 648-4340",
      "screens": 6,
      "tags": {
        "seating": "GENERAL_ADMISSION_ONLY"
      },
      "ticketSource": "",
      "tickets": false
    },
    ...
  },
  "traits": {}
}
```

#### Client Method
The `get_theater_information` method takes a `TheaterInformationQuery` object that has a `date`, a `return_complete_movie_info`, a `return_show_times`, an optional `movie_id`, and a `limit`.

The `date` value represents a date to lookup show times. Defaults to today.`

The `return_complete_movie_info` is a `boolean` value that represents whether or not to return full movie details as part of the response. Defaults to `True`.

The `return_show_times` is a `boolean` value that represents whether or not to return show time information as part of the response. Defaults to `True`.

The `movie_id` is an optional field that takes a Flixster movie id and will only return information for the given movie.

The `limit` value represents the number of theaters to consider. Defaults to `5`.

#### Example

```python
from Flixster import FlixsterClient, TheaterInformationQuery

# Get show times for today, for all movies, with full movie information, for the closest 5 theaters
query = TheaterInformationQuery()

FlixsterClient.get_theater_information(query)
```
