from flask_sqlalchemy import SQLAlchemy
import logging as lg

from .views import app
# Create database connection object
db = SQLAlchemy(app)

class Content(db.Model):
    GENDER_FEMALE = 'female'
    GENDER_MALE = 'male'
    GENDER_OTHER = 'other'
    GENDERS = {
        GENDER_FEMALE: 0,
        GENDER_MALE: 1,
        GENDER_OTHER: 2
    }
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))
    gender = db.Column('gender', db.Integer, nullable=False, default=GENDERS[GENDER_FEMALE])

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("What's your favorite scary movie?", Content.GENDERS[Content.GENDER_MALE]))
    db.session.commit()
    lg.warning('Database initialized!')
