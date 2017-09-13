# Import modules
import media
import json
import fresh_tomatoes

# Create empty list to store "media.Movie" objects
movies_list = []

# Extract data from "movies.json"
with open('movies.json') as movies_data:
    movies = json.load(movies_data)

# For each movie,
for movie in movies:
    # Create media.Movie object
    movie_obj = media.Movie(movie['title'],
                            movie['storyline'],
                            movie['poster_image_url'],
                            movie['trailer_youtube_url'])

    # Add object to "movies_list"
    movies_list.append(movie_obj)

# Create page(if not already),
# Display page
fresh_tomatoes.open_movies_page(movies_list)
