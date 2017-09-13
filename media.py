class Movie:
    """ Model of a movie object """

    def __init__(self, title, storyline, poster_url, trailer_url):
        """ Initialising the instance variables for the movie object, i.e.
        movie's title, storyline, poster_image_url and trailer_youtube_url """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
