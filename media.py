import webbrowser
'''Media Module contains Movie class, it can be used to create
instances of movies using movie class'''
class Movie:
    ''' Movie class has four attributes : title, story, trailer, poster'''
    def __init__(self, title, story_line, trailer_link, poster_link):
        self.title = title
        self.story_line = story_line
        self.trailer_youtube_url = trailer_link
        self.poster_image_url = poster_link
    
    def show_trailer(self):
        '''opens the youtube trailer of the movie in a webpage using the default browser'''
        webbrowser.open(self.trailer_youtube_url)
    