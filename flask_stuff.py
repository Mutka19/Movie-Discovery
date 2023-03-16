import flask
from movie_discovery import get_3_default_movies, get_movie_img

app = flask.Flask("Movie Discovery")


@app.route("/")
def index():
    movies = get_3_default_movies()
    movie_title = movies[0]['title']
    movie_overview = movies[0]['overview']
    movie_genres = ", ".join([movie['name'] for movie in movies[0]['genres']])
    movie_img = get_movie_img(movies[0]['poster_path'])
    return flask.render_template("index.html", Title=movie_title, Overview=movie_overview, Genres=movie_genres, IMG=movie_img)

app.run(debug=True)