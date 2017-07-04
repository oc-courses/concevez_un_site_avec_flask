from flask_sqlalchemy import SQLAlchemy
import logging as lg

from .views import app
# Create database connection object
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Integer(), nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("THIS IS SPARTAAAAAAA!!!", 1))
    db.session.add(Content("What's your favorite scary movie?", 0))
    db.session.commit()
    lg.warning('Database initialized!')
