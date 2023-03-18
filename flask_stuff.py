import flask
import random
from movie_discovery import get_3_default_movies, get_movie_img, get_wiki_link

app = flask.Flask("Movie Discovery")


@app.route("/")
def index():
    index = random.randrange(0,2)
    movies = get_3_default_movies()
    movie_title = movies[index]["title"]
    movie_overview = movies[index]["overview"]
    movie_genres = ", ".join([movie["name"] for movie in movies[index]["genres"]])
    movie_img = get_movie_img(movies[index]["poster_path"])
    link = get_wiki_link(movies[index]['title'])
    return flask.render_template(
        "index.html",
        Title=movie_title,
        Overview=movie_overview,
        Genres=movie_genres,
        IMG=movie_img,
        WikiLink=link
    )


app.run(debug=True)
