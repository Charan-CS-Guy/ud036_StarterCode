import os
import requests
import simplejson
import sqlite3
import urllib


def get_top_movies():

    '''fetches the movies by popularity from tmdb database.'''
    discover_link = "https://api.themoviedb.org/3/discover/movie?"

    payload = {'api_key' : "a7e17d6da36a880ac3fa023195e93ec7", 'language' : 'en-US',
               'sort_by' : 'popularity.desc', 'page' : '1'}

    r = requests.get(discover_link, params=payload)

    print(r.url)
    data = r.content

    js = simplejson.loads(data)

    for movie in js['results']:

        print(movie['id'])
        print(movie['title'])
        print(movie['overview'].encode('ascii', 'ignore').decode('ascii'))
        print(movie['poster_path'])

get_top_movies()