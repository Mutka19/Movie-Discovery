import flask
import random
import os
from flask_sqlalchemy import SQLAlchemy
from api_handler import (
    get_3_default_movies,
    get_movie_img,
    get_wiki_link,
    search_for_movie,
    get_movie_by_id,
)
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = flask.Flask(__name__)
app.secret_key = "secret_key_i_need_for_some_reason"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username

    def check_password(self, password):
        return self.password == password


@app.route("/")
def index():
    index = random.randrange(0, 3)
    movie = get_3_default_movies(index)
    movie_title = movie["title"]
    movie_overview = movie["overview"]
    movie_genres = ", ".join([movie["name"] for movie in movie["genres"]])
    movie_img = get_movie_img(movie["poster_path"])
    link = get_wiki_link(movie["title"])
    m_id=movie["id"]
    username = flask.session.get("username")
    return flask.render_template(
        "index.html",
        Title=movie_title,
        Overview=movie_overview,
        Genres=movie_genres,
        IMG=movie_img,
        WikiLink=link,
        username=username,
        movie_id=m_id
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
        id = movie["id"]
        username = flask.session.get("username")
        return flask.render_template(
            "index.html",
            Title=movie_title,
            Overview=movie_overview,
            Genres=movie_genres,
            IMG=movie_img,
            WikiLink=link,
            username=username,
            movie_id=id,
        )


@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        # Handle form submission
        username = flask.request.form["username"]
        password = flask.request.form["password"]
        print(username, password)

        # Authenticate user
        user = Person.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            # Login successful, redirect to dashboard
            flask.session["user_id"] = user.id
            flask.session["username"] = username
            return flask.redirect(flask.url_for("index"))
        else:
            # Login failed, show error message
            error_message = "Invalid username or password"
            return flask.render_template("login.html", error_message=error_message)

    # Render login page
    return flask.render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if flask.request.method == "POST":
        # Handle form submission
        username = flask.request.form["username"]
        password = flask.request.form["password"]

        # Add the new person to the database
        new_user = Person(username=username, password=password)

        db.session.add(new_user)
        db.session.commit()
        # Redirect to the login page or some other page
        return flask.redirect("/login")
    else:
        # Render the sign up page
        return flask.render_template("signup.html")


@app.route("/review/<int:movie_id>", methods=["GET", "POST"])
def review(movie_id):
    if flask.request.method == "POST":
        # Get the review text from the form submission
        review_text = flask.request.form["review-text"]

        # Store the review in the database for the specified movie ID
        # (You would need to write code to do this based on your database schema)

        # Redirect to the movie details page for the specified movie ID
        return flask.redirect(flask.url_for("index"))

    else:
        # Render the review page template
        return flask.render_template("review.html", movie_id=movie_id, movie_title=get_movie_by_id(movie_id)["title"])


app.run(debug=True)
