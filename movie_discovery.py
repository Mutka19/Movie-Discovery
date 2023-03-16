import requests as rq
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_3_default_movies():
    TMBD_BASE_URL = "https://api.themoviedb.org/3"
    TMBD_MOVIE_PATH = "/movie/"
    MOVIE_IDS = ["808", "1091", "9615"]
    MOVIE_LIST = []

    for ID in MOVIE_IDS:
        request = rq.get(
            TMBD_BASE_URL + TMBD_MOVIE_PATH + ID,
            params={"api_key": os.getenv("TMBD_API_KEY")},
        )
        MOVIE_LIST.append(request.json())
    return MOVIE_LIST


def get_movie_img(poster_path):
    TMBD_BASE_IMAGE_URL = "https://image.tmdb.org/t/p/"
    TMBD_IMG_SIZE = "w500/"

    return TMBD_BASE_IMAGE_URL + TMBD_IMG_SIZE + poster_path


def search_for_movie(movie):
    TMBD_BASE_URL = "https://api.themoviedb.org/3"
    TMBD_MOVIE_PATH = "/search/movie"
    MOVIE_PARAM = movie

    request = rq.get(
        TMBD_BASE_URL + TMBD_MOVIE_PATH,
        params={"api_key": os.getenv("TMBD_API_KEY"), "query": MOVIE_PARAM},
    )
    return request.json()


# print(search_for_movie("Shrek"))
# names = ", ".join([sublist["name"] for sublist in get_3_default_movies()[0]["genres"]])
# movies = get_3_default_movies()
# print(movies[0])
# print(get_movie_img(movies[0]['poster_path']))
# print(names)
# print(get_3_default_movie_images())
