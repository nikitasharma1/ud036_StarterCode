# Import modules
import media
import fresh_tomatoes
import movies

# Create empty list to store "media.Movie" objects
movies_list = []

# For each movie,
for movie in movies.movies:
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
