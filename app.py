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
# When first landing on the page welcome page is loaded
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


@app.route("/get_reviews")
# display reviews on review page
def get_reviews():
    reviews = list(mongo.db.reviews.find())
    return render_template("reviews.html", reviews=reviews)


@app.route("/search", methods=["GET", "POST"])
# Search for reviews by book name, author, reviewed_by
def search():
    query = request.form.get("query")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))
    return render_template("reviews.html", reviews=reviews)


@app.route("/see_review/<reviews>", methods=["GET", "POST"])
# view the full review of individual book
def see_review(reviews):
    reviews = list(mongo.db.reviews.find({"_id": ObjectId(reviews)}))
    return render_template("book_review.html", reviews=reviews)


@app.route("/book_review", methods=["GET", "POST"])
# gets the information for the see_review function
def book_review():
    if request.method == "POST":
        favourite = "on" if request.form.get('favourite') else "off"
        review = {
            "genre_name": request.form.get("genre_name"),
            "review_image": request.form.get("review_image"),
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "review_title": request.form.get("review_title"),
            "review": request.form.get("review"),
            "rating": request.form.get("rating_no"),
            "favourite": favourite,
            # takes the username of the person logged in
            "reviewed_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Review successfully added")
        return redirect(url_for('book_review'))

    genres = list(mongo.db.genres.find().sort("genre_name", 1))
    ratings = list(mongo.db.ratings.find().sort("rating", 1))
    return render_template("book_review.html", genres=genres, ratings=ratings)


@app.route("/register", methods=["GET", "POST"])
# allows the user to register
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
        session["user"] = request.form.get("username").lower()
        flash("Registration successful, {}".format(
            request.form.get("username")))
        return redirect(url_for(
                "profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
# allows user to log in
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
# profile page for user
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    my_reviews = list(mongo.db.book_review.find(
            {"created_by": session["user"]}))

    if session["user"]:
        return render_template(
            "profile.html", username=username, my_reviews=my_reviews)

    return redirect(url_for("login"))


@app.route("/logout")
# log user out using session cookie
def logout():
    flash("You have been logged out")
    session.pop('user')
    return redirect(url_for('login'))


@app.route("/add_review", methods=["GET", "POST"])
# allows user to add review
def add_review():
    if request.method == "POST":
        favourite = "on" if request.form.get('favourite') else "off"
        review = {
            "genre_name": request.form.get("genre_name"),
            "review_image": request.form.get("review_image"),
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "review_title": request.form.get("review_title"),
            "review": request.form.get("review"),
            "rating": request.form.get("rating_no"),
            "favourite": favourite,
            "reviewed_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Review successfully added")
        return redirect(url_for('get_reviews'))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    ratings = list(mongo.db.ratings.find().sort("rating", 1))
    return render_template("add_review.html", genres=genres, ratings=ratings)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
# allows users to edit their own reviews
def edit_review(review_id):
    if request.method == "POST":
        favourite = "on" if request.form.get('favourite') else "off"
        submit = {
            "genre_name": request.form.get("genre_name"),
            "review_image": request.form.get("review_image"),
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "review_title": request.form.get("review_title"),
            "review": request.form.get("review"),
            "rating": request.form.get("rating_no"),
            "favourite": favourite,
            "reviewed_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review successfully updated")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    genres = mongo.db.genres.find().sort("genre_name", 1)
    ratings = list(mongo.db.ratings.find().sort("rating", 1))
    return render_template(
        "edit_review.html", genres=genres, ratings=ratings, review=review)


@app.route("/delete_review/<review_id>")
# allows user to delete review
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review deleted")
    return redirect(url_for('get_reviews'))


@app.route("/get_genres")
# allows superuser to manage the genres
def get_genres():
    genres = list(mongo.db.genres.find().sort("genre_name", 1))
    return render_template("genres.html", genres=genres)


@app.route("/add_genre", methods=["GET", "POST"])
# allows superuser to add new genre
def add_genre():
    if request.method == "POST":
        genre = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.insert_one(genre)
        flash("New Genre Added")
        return redirect(url_for("get_genres"))

    return render_template("add_genre.html")


@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
# allows superuser to edit the genres
def edit_genre(genre_id):
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.update({"_id": ObjectId(genre_id)}, submit)
        flash("genre Successfully Updated")
        return redirect(url_for("get_genres"))

    genre = list(mongo.db.genres.find_one({"_id": ObjectId(genre_id)}))
    return render_template("edit_genre.html", genre=genre)

# prompt if want to delete using toast/modal - defensive programming


@app.route("/delete_genre/<genre_id>")
# allows superuser to delete the genres
def delete_genre(genre_id):
    mongo.db.genres.remove({"_id": ObjectId(genre_id)})
    flash("Genre Successfully Deleted")
    return redirect(url_for("get_genres"))


@app.route("/review/add_favourite/<review_id>", methods=["GET", "POST"])
# add a favourite book review to profile with help from
# https://github.com/manni8436/MS3-Project/
def add_favourite(review_id):
    if session["user"]:
        data = {
            "book_name": review_id,
            "username": session["user"]
        }

    mongo.db.favourites.insert_one(data)
    return redirect(url_for("reviews"))


@app.route("/favourites")
# add a favourite book review to profile with help from
# https://github.com/manni8436/MS3-Project/
def favourites():
    user = list(mongo.db.favourites.find(
        {"$and": [{"username": {'$eq': session["user"]}}]}))
    favourite_list = []
    for i in user:
        favourite_list.append(
            mongo.db.reviews.find_one({"_id": ObjectId(i["review_name"])}))
    return render_template("profile.html", favourite_list=favourite_list)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
