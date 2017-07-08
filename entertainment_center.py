''' This module creates data for different movies using media module's Movie class'''
import media
import fresh_tomatoes
import requests
import simplejson

from configobj import ConfigObj

def get_trailer_key(movie_id, base_link, interface_key):
    '''used to fetch the key for youtube trailer link of the movie id given'''
    url = base_link + str(movie_id) + "/videos?api_key=" + interface_key

    res = requests.get(url)

    data_res = res.content

    js_res = simplejson.loads(data_res)

    return js_res["results"][0]["key"]

def get_top_movies(api_key):
    '''fetches the top movies from TMDB database and returns
    them as a list of objects or type Movie() from media module'''

    discover_link = "https://api.themoviedb.org/3/discover/movie?"
    poster_base_url = "http://image.tmdb.org/t/p/w185//"
    youtube_base_url = "https://www.youtube.com/watch?v="
    base_link = "https://api.themoviedb.org/3/movie/"
    payload = {'api_key' : api_key, 'language' : 'en-US',
               'sort_by' : 'popularity.desc', 'page' : '1'}

    r = requests.get(discover_link, params=payload)

    data = r.content

    js = simplejson.loads(data)

    #list to hold all the movie objects
    movies_list = []
    
    #create a list of all the movies/objects to provide as an input to open_movies function
    for movie in js['results']:

        id = movie['id']
        title = movie['title']
        story_line = movie['overview'].encode('ascii', 'ignore').decode('ascii')
        poster_path = movie['poster_path']

        poster_link = poster_base_url + poster_path

        trailer_key = get_trailer_key(id, base_link, api_key)
        trailer_link = youtube_base_url + trailer_key

        #creating objects to store each movie details using Movie class from media module.
        obj = media.Movie(title, story_line, trailer_link, poster_link)
        movies_list.append(obj)
    
    return movies_list

#fetching the api key from config file using ConfigObj class from configobj module
config = ConfigObj("config.ini")
key = config['api_key']

if len(key) <= 0:

    print("Please, place your api key in the config.ini file")
    exit
#collecting the data for top movies
list_of_top_movies = get_top_movies(key)

#call open movies function from fresh_tomatoes module to create website
fresh_tomatoes.open_movies_page(list_of_top_movies)
