"""
    Code adapted from Code Institute Course Material
    Task Manager Flask App mini Project
"""

import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_reviews")
def get_reviews():
    reviews = list(mongo.db.reviews.find())
    return render_template("reviews.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # change the flash to toast?
            flash("Username already exists, please select another")
            return redirect(url_for("register"))

# in Mini Project | Putting It All Together  User Authentication
# Adding Registration Functionality video
# Tim says if you want a confirm password you should do it
# before this dictionary

        register = {
            "fname": request.form.get("fname").capitalize(),
            "lname": request.form.get("lname").capitalize(),
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            # as a challenge can change the hash and salt method for project
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put new user in to session using session cookie
        # add user's name to flash method
        session["user"] = request.form.get("fname").lower()
        flash("Registration successful, {}".format(
            request.form.get("fname")))
        return redirect(url_for(
                "profile", fname=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session['user'] = request.form.get('username')
                return redirect(url_for(
                    "profile", fname=session['user']))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<fname>", methods=["GET", "POST"])
def profile(fname):
    # grab the session user's username from db
    fname = mongo.db.users.find_one(
        {"username": session["user"]})["fname"]

    if session['user']:
        return render_template("profile.html", fname=fname)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session
    flash("You have been logged out")
    session.pop('user')
    return redirect(url_for('login'))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        favourite = "on" if request.form.get('favourite') else "off"
        review = {
            "genre_name": request.form.get("genre_name"),
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "favourite": favourite,
            "reviewed_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Review successfully added")
        return redirect(url_for('get_reviews'))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    ratings = mongo.db.ratings.find().sort("rating", 1)
    return render_template("add_review.html", genres=genres, ratings=ratings)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
