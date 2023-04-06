import requests as rq
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_3_default_movies(index):
    TMBD_BASE_URL = "https://api.themoviedb.org/3"
    TMBD_MOVIE_PATH = "/movie/"
    MOVIE_IDS = ["808", "1091", "9615"]

    request = rq.get(
        TMBD_BASE_URL + TMBD_MOVIE_PATH + MOVIE_IDS[index],
        params={"api_key": os.getenv("TMBD_API_KEY")},
    )
    return request.json()


def get_movie_by_id(id):
    TMBD_BASE_URL = "https://api.themoviedb.org/3"
    TMBD_MOVIE_PATH = "/movie/"

    request = rq.get(
        TMBD_BASE_URL + TMBD_MOVIE_PATH + str(id),
        params={"api_key": os.getenv("TMBD_API_KEY")},
    )
    return request.json()


def get_movie_img(poster_path):
    TMBD_BASE_IMAGE_URL = "https://image.tmdb.org/t/p/"
    TMBD_IMG_SIZE = "w500/"

    return TMBD_BASE_IMAGE_URL + TMBD_IMG_SIZE + poster_path


def search_for_movie(movie):
    TMBD_BASE_URL = "https://api.themoviedb.org/3"
    TMBD_MOVIE_PATH = "/movie/"
    TMBD_SEARCH_PATH = "/search/movie"
    MOVIE_PARAM = movie

    request = rq.get(
        TMBD_BASE_URL + TMBD_SEARCH_PATH,
        params={"api_key": os.getenv("TMBD_API_KEY"), "query": MOVIE_PARAM},
    )
    if request.json()["results"][0]["id"]:
        ID = request.json()["results"][0]["id"]
        request = rq.get(
            TMBD_BASE_URL + TMBD_MOVIE_PATH + str(ID),
            params={"api_key": os.getenv("TMBD_API_KEY")},
        )
        return request.json()
    return request.json()["results"]


def get_wiki_link(name):
    WIKI_BASE_URL = "https://www.wikipedia.org/w/api.php"

    request = rq.get(
        WIKI_BASE_URL,
        params={
            "action": "query",
            "prop": "categories",
            "list": "search",
            "srsearch": name,
            "format": "json",
        },
    )
    for i in request.json()["query"]["search"]:
        rq1 = rq.get(
            WIKI_BASE_URL,
            params={
                "action": "query",
                "prop": "categories",
                "titles": i["title"],
                "format": "json",
            },
        )

        for category in rq1.json()["query"]["pages"][
            list(rq1.json()["query"]["pages"])[0]
        ]["categories"]:
            if "film" in category["title"]:
                result = rq.get(
                    WIKI_BASE_URL,
                    params={
                        "action": "query",
                        "prop": "info",
                        "inprop": "url",
                        "format": "json",
                        "titles": i["title"],
                    },
                )
                return result.json()["query"]["pages"][
                    list(result.json()["query"]["pages"])[0]
                ]["fullurl"]
    return


# print(search_for_movie("Terminator")["id"])
