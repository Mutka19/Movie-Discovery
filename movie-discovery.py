import flask
import random
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
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
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username

    def validate(self, password):
        return self.password == password

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review_text = db.Column(db.String(280), nullable=False)
    film_id = db.Column(db.Integer, nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer)

def check_login():
    return "username" in flask.session


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
    review = Review.query.filter_by(film_id=m_id).order_by(func.random()).first()
    return flask.render_template(
        "index.html",
        Title=movie_title,
        Overview=movie_overview,
        Genres=movie_genres,
        IMG=movie_img,
        WikiLink=link,
        username=username,
        movie_id=m_id,
        review=review
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
        m_id = movie["id"]
        username = flask.session.get("username")
        review = Review.query.filter_by(film_id=m_id).order_by(func.random()).first()
        return flask.render_template(
            "index.html",
            Title=movie_title,
            Overview=movie_overview,
            Genres=movie_genres,
            IMG=movie_img,
            WikiLink=link,
            username=username,
            movie_id=m_id,
            review=review
        )


@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        username = flask.request.form["username"]
        password = flask.request.form["password"]
        print(username, password)

        user = Person.query.filter_by(username=username).first()
        if user is not None and user.validate(password):
            flask.session["user_id"] = user.id
            flask.session["username"] = username
            return flask.redirect(flask.url_for("index"))
        else:
            error_message = "Invalid username or password"
            return flask.render_template("login.html", error_message=error_message)

    # Render login page
    return flask.render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if flask.request.method == "POST":
        username = flask.request.form["username"]
        password = flask.request.form["password"]

        if Person.query.filter_by(username=username).first():
            error_message = "This username already exists, please choose a different username!"
            return flask.render_template("signup.html", error_message=error_message)

        new_user = Person(username=username, password=password)

        db.session.add(new_user)
        db.session.commit()
        return flask.redirect("/login")
    else:
        return flask.render_template("signup.html")


@app.route("/review/<int:movie_id>", methods=["GET", "POST"])
def review(movie_id):
    if not check_login():
        return flask.render_template("login.html", error_message="Must be logged in to write a review!")
    
    if flask.request.method == "POST":

        review_text = flask.request.form["review_text"]
        rating = flask.request.form.get('rating')
        review = Review(review_text=review_text, film_id=movie_id, rating=rating, user_name=flask.session.get("username"))
        db.session.add(review)
        db.session.commit()

        return flask.redirect(flask.url_for("index"))

    else:
        return flask.render_template("review.html", movie_id=movie_id, movie_title=get_movie_by_id(movie_id)["title"])
    
@app.route("/signout")
def signout():
    flask.session.pop("user_id", None)
    flask.session.pop("username", None)

    return flask.redirect(flask.url_for("index"))


app.run(debug=True)
