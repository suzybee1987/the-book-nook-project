"""
    Code adapted from Code Institute Course Material
    Task Manager Flask App mini Project
"""

import os
import datetime
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
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
@app.route("/welcome")
def welcome():
    """
    When first landing on the page welcome page is loaded
    """
    quotes = list(mongo.db.quotes.find())
    return render_template("welcome.html", quotes=quotes)


@app.route("/get_reviews")
def get_reviews():
    """
    get the list of reviews to show on reviews.html
    """
    reviews = list(mongo.db.reviews.find())
    return render_template("reviews.html", reviews=reviews)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search for reviews by book name, author, reviewed_by
    """
    query = request.form.get("query")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))
    return render_template("reviews.html", reviews=reviews)


@app.route("/see_review/<reviews>", methods=["GET", "POST"])
def see_review(reviews):
    """
    view the full review of individual book
    """
    reviews = list(mongo.db.reviews.find({"_id": ObjectId(reviews)}))
    return render_template("book_review.html", reviews=reviews)


@app.route("/book_review", methods=["GET", "POST"])
def book_review():
    """
    gets the information for the see_review function
    """
    if request.method == "POST":
        review = {
            "genre_name": request.form.get("genre_name"),
            "image": request.form.get("image"),
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "review_title": request.form.get("review_title"),
            "review": request.form.get("review"),
            "rating_no": request.form.get("rating"),
            "favourites": request.form.get("favourites"),
            "reviewed_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Review successfully added")
        return redirect(url_for('book_review'))

    genres = list(mongo.db.genres.find().sort("genre_name", 1))
    ratings = list(mongo.db.ratings.find().sort("rating_no", 1))
    return render_template("book_review.html", genres=genres, ratings=ratings)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    allows the user to register
    """
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

        user_details = {
            "fname": request.form.get("fname").capitalize(),
            "lname": request.form.get("lname").capitalize(),
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            # as a challenge can change the hash and salt method for project
            "password": generate_password_hash(request.form.get("password")),
            "admin": "off",
        }
        mongo.db.users.insert_one(user_details)

        # put new user in to session using session cookie
        session["user"] = request.form.get("username").lower()

        return redirect(url_for("get_reviews"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    allows user to log in
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()

                username = mongo.db.users.find_one(
                    {"username": session["user"]})["username"]
                # get the users name to load in profile page
                fname = mongo.db.users.find_one(
                    {"username": username})["fname"]
                flash("You are logged in, {}".format(fname))
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    profile page for user
    """
    if session["user"]:
        # grab the session user's username from db
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        # get the users name to load in profile page
        fname = mongo.db.users.find_one(
            {"username": username})["fname"]
        # get the reviws written by session user
        my_reviews = list(mongo.db.reviews.find(
            {"reviewed_by": session["user"]}))
        reviews = list(mongo.db.reviews.find())
        # favourites functionality
        user = list(mongo.db.favourites.find(
            {"$and": [{"username": {'$eq': session["user"]}}]}))
        favourites_list = []
        for i in user:
            favourites_list.append(mongo.db.reviews.find_one(
                {"_id": ObjectId(i["book_name"])}))

        return render_template(
            "profile.html", username=username,
            my_reviews=my_reviews, fname=fname, reviews=reviews,
            favourites_list=favourites_list)

    flash("Please log in")
    return redirect(url_for('login'))


@app.route("/logout")
def logout():
    """
    log user out using session cookie
    """
    flash("You have been logged out")
    session.pop('user')
    return redirect(url_for('login'))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    """
    allows user to add review
    """
    if request.method == "POST":
        review = {
            "genre_name": request.form.get("genre_name"),
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "review_title": request.form.get("review_title"),
            "review": request.form.get("review"),
            "description": request.form.get("description"),
            "rating_no": request.form.get("rating"),
            "image": request.form.get("image"),
            "favourites": request.form.get("favourites"),
            "reviewed_by": session["user"],
            "review_date": datetime.datetime.utcnow()
        }
        mongo.db.reviews.insert_one(review)
        flash("Review successfully added")
        return redirect(url_for('get_reviews'))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    ratings = list(mongo.db.ratings.find().sort("rating_no", 1))
    return render_template("add_review.html", genres=genres, ratings=ratings)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    """
    allows users to edit their own reviews
    """
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name"),
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "review_title": request.form.get("review_title"),
            "review": request.form.get("review"),
            "description": request.form.get("description"),
            "image": request.form.get("image"),
            "rating_no": request.form.get("rating"),
            "favourites": request.form.get("favourites"),
            "reviewed_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review successfully updated")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    genres = mongo.db.genres.find().sort("genre_name", 1)
    ratings = list(mongo.db.ratings.find().sort("rating_no", 1))
    return render_template(
        "edit_review.html", genres=genres, ratings=ratings, review=review)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    """
    allows user to delete review
    """
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review deleted")
    return redirect(url_for('get_reviews'))


@app.route("/add_thoughts/<thoughts_id>", methods=["GET", "POST"])
def add_thoughts(thoughts_id):
    """
    allows user to add their thoughts to an existing review
    """
    if request.method == "POST":
        new_thoughts = {
            "thoughts": request.form.get("thoughts"),
            "review_by": session["user"],
            "reviewed_date": datetime.datetime.utcnow()
        }
        mongo.db.reviews.update_one(
            {"_id": ObjectId(thoughts_id)},
            {"$push": {"thoughts": new_thoughts}})

        flash("Your thoughts successfully added")
        return redirect(url_for('see_review', reviews=thoughts_id))

    thoughts = mongo.db.reviews.find_one({"_id": ObjectId(thoughts_id)})
    return render_template("add_thoughts", thoughts=thoughts)


@app.route("/favourites")
def favourites():
    """
        favourites functionality
        following guidance from
        https://github.com/manni8436/MS3-Project
    """
    user = list(mongo.db.favourites.find(
        {"$and": [{"username": {'$eq': session["user"]}}]}))
    favourites_list = []
    for i in user:
        favourites_list.append(mongo.db.reviews.find_one(
            {"_id": ObjectId(i["book_id"])}))

    return render_template("profile.html", favourites_list=favourites_list)


@app.route("/add_favourite/<favourite_id>", methods=["GET", "POST"])
def add_favourite(favourite_id):
    """
    add book into favourites collection in DB.
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    data = {
        "book_name": ObjectId(favourite_id),
        "username": username
    }
    mongo.db.favourites.insert_one(data)
    flash("Book saved to favourites")

    if username:
        return redirect(url_for("profile", username=username))

    flash("Please log in to save a favourite")
    return render_template("login.html")


@app.route("/remove_favourite/<favourite_id>")
def remove_favourite(favourite_id):
    """
    deletes book from favourites collection in DB and from profile
    """
    if session["user"]:
        mongo.db.favourites.remove({"book_name": ObjectId(favourite_id)})
        return redirect(url_for("profile", username=session["user"]))
    else:
        flash("Please log in to save a favourite")
        return render_template("login")


@app.route("/get_genres")
def get_genres():
    """
    allows superuser to manage the genres
    """
    genres = list(mongo.db.genres.find().sort("genre_name", 1))
    return render_template("genres.html", genres=genres)


@app.route("/see_genre/<genre_id>", methods=["GET", "POST"])
def see_genre(genre_id):
    """
    view the full page of individual genre
    """
    genres = list(mongo.db.genres.find({"_id": ObjectId(genre_id)}))
    return render_template("delete_genre.html", genres=genres)


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    """
    allows superuser to add new genre
    """
    if request.method == "POST":
        genre = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.insert_one(genre)
        flash("New Genre Added")
        return redirect(url_for("get_genres"))

    return render_template("add_genre.html")


@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    """
    allows admin to edit the genres
    """
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name")
        }
        try:
            if session["user"]:
                username = mongo.db.users.find_one(
                    {"username": session["user"]}
                )

                if username["admin"] == "on":
                    mongo.db.genres.update({"_id": ObjectId(genre_id)}, submit)
                    flash("Genre Successfully Updated")
                    return redirect(url_for("get_genres"))
        except Exception:
            flash("You are not allowed to do that")
            return redirect(url_for("get_reviews"))

    genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
    return render_template("edit_genre.html", genre=genre)


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    """
    allows superuser to delete the genres
    """
    try:
        if session["user"]:
            username = mongo.db.users.find_one(
                {"username": session["user"]}
            )
            if username["admin"] == "on":
                mongo.db.genres.remove({"_id": ObjectId(genre_id)})
                flash("Genre Successfully Deleted")
                return redirect(url_for("get_genres"))
    except Exception:
        flash("You are not allowed to do that")
        return redirect(url_for("get_reviews"))


@app.route("/get_users")
def get_users():
    """
    allows admin to manage the users
    """
    users = list(mongo.db.users.find().sort("username", 1))
    return render_template("users.html", users=users)


@app.route("/see_user/<user_id>", methods=["GET", "POST"])
def see_user(user_id):
    """
    view the full page of individual user
    """
    users = list(mongo.db.users.find({"_id": ObjectId(user_id)}))
    return render_template("delete_user.html", users=users)


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    """
    allows superuser to add new user
    """
    if request.method == "POST":
        user = {
            "username": request.form.get("username")
        }
        mongo.db.users.insert_one(user)
        flash("New User Added")
        return redirect(url_for("get_users"))

    return render_template("add_user.html")


@app.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    """
    allows admin to edit the users
    """
    if request.method == "POST":
        submit = {
            "username": request.form.get("username")
        }
        try:
            if session["user"]:
                username = mongo.db.users.find_one(
                    {"username": session["user"]}
                )

                if username["admin"] == "on":
                    mongo.db.users.update({"_id": ObjectId(user_id)}, submit)
                    flash("User Successfully Updated")
                    return redirect(url_for("get_users"))
        except Exception:
            flash("You are not allowed to do that")
            return redirect(url_for("get_reviews"))

    user = list(mongo.db.users.find_one({"_id": ObjectId(user_id)}))
    return render_template("edit_user.html", user=user)


@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    """
    allows superuser to delete the users
    """
    try:
        if session["user"]:
            username = mongo.db.users.find_one(
                {"username": session["user"]}
            )
            if username["admin"] == "on":
                mongo.db.users.remove({"_id": ObjectId(user_id)})
                flash("User Successfully Deleted")
                return redirect(url_for("get_users"))
    except Exception:
        flash("You are not allowed to do that")
        return redirect(url_for("get_reviews"))


@app.errorhandler(404)
def page_not_found(e):
    """
    404 page, code from
    https://flask.palletsprojects.com/en/2.0.x/errorhandling/?highlight=custom%20error%20pages
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """
    404 page, code from
    https://flask.palletsprojects.com/en/2.0.x/errorhandling/?highlight=custom%20error%20pages
    """
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
