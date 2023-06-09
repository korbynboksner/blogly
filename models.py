"""Models for Blogly."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User."""

    __tablename__ = "users"
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.Text,
                     nullable=False)
    last_name = db.Column(db.Text,
                     nullable=False)
    image_url = db.Column(db.Text,
                     nullable=False,
                     )
    
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

