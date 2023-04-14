"""Blogly application."""

from flask import Flask, render_template, request, redirect, session
from models import db, connect_db, User
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_ECHO'] = True


connect_db(app)

db.create_all()

@app.route('/')
def go_home():
    return redirect("/users")


@app.route("/users", methods=["GET"])
def list_users():
    """List pets and show add form."""

    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template("homelist.html", users=users)

@app.route("/users/new", methods=["GET"])
def new_form():
    return render_template("newform.html")

@app.route("/users/new", methods=["POST"])
def add():
    first = request.form['fn']
    last = request.form['ln']
    url = request.form['url']

    user = User(first_name=first, last_name=last, image_url=url)
    db.session.add(user)
    db.session.commit()
    return redirect("/users")

@app.route("/users/<int:user_id>")
def show_user(user_id):
    """Show info on a single user."""

    user = User.query.get_or_404(user_id)
    return render_template("detail.html", user=user)

@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")

@app.route("/users/<int:user_id>/edit", methods=["GET"])
def edit_page(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("edit.html", user=user)


@app.route("/users/<int:user_id>/edit", methods=["POST"])
def user_update(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['fn']
    user.last_name = request.form['ln']
    user.image_url = request.form['url']

    db.session.add(user)
    db.session.commit()
    return redirect("/users")