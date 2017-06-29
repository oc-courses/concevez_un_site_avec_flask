import random

from fbapp.models import Content

def find_content(gender):
    contents = Content.query.filter(Content.gender == Content.GENDERS[gender]).all()
    return random.choice(contents)
