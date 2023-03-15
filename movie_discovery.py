import requests as rq
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def get_3_default_movies():
    TMBD_BASE_URL = 'https://api.themoviedb.org/3'
    TMBD_MOVIE_PATH = '/movie/'
    MOVIE_IDS = ['573531', '335984', '9615']

    r1 = rq.get(
        TMBD_BASE_URL + TMBD_MOVIE_PATH + MOVIE_IDS[0], 
        
        params={
            'api_key': os.getenv("TMBD_API_KEY"),
        }
    )
    movie_list = r1.json()
    print(movie_list)

def search_for_movie(movie):
    TMBD_BASE_URL = 'https://api.themoviedb.org/3'
    TMBD_MOVIE_PATH = '/search/movie'
    MOVIE_PARAM = movie

    r1 = rq.get(
        TMBD_BASE_URL + TMBD_MOVIE_PATH, 
        
        params={
            'api_key': os.getenv("TMBD_API_KEY"),
            'query': MOVIE_PARAM
        }
    )
    movie_list = r1.json()
    print(movie_list)

#search_for_movie('The Fast and the Furious: Tokyo Drift')
get_3_default_movies()
