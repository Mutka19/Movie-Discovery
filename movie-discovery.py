import flask
import random
from api_handler import (
    get_3_default_movies,
    get_movie_img,
    get_wiki_link,
    search_for_movie,
)

app = flask.Flask(__name__)


@app.route("/")
def index():
    index = random.randrange(0, 3)
    movie = get_3_default_movies(index)
    movie_title = movie["title"]
    movie_overview = movie["overview"]
    movie_genres = ", ".join([movie["name"] for movie in movie["genres"]])
    movie_img = get_movie_img(movie["poster_path"])
    link = get_wiki_link(movie["title"])
    return flask.render_template(
        "index.html",
        Title=movie_title,
        Overview=movie_overview,
        Genres=movie_genres,
        IMG=movie_img,
        WikiLink=link,
    )


@app.route("/", methods=["POST"])
def handle_user_info():
    form_data = flask.request.form
    movie_title = form_data["Movie"]
    if len(movie_title) == 0:
        flask.flash("Please enter a movie title before submitting")
        return flask.redirect(flask.url_for("index"))
    else:
        movie = search_for_movie(movie_title)
        movie_title = movie["title"]
        movie_overview = movie["overview"]
        movie_genres = ", ".join([genres["name"] for genres in movie["genres"]])
        movie_img = get_movie_img(movie["poster_path"])
        link = get_wiki_link(movie["title"])
        return flask.render_template(
            "index.html",
            Title=movie_title,
            Overview=movie_overview,
            Genres=movie_genres,
            IMG=movie_img,
            WikiLink=link,
        )

app.run(debug=True)