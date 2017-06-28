import random

from fbapp.models import Content

def find_content(gender):
    contents = Content.query.filter(Content.gender == Content.GENDERS[gender]).all()
    ids = [content.id for content in contents]
    the_one = Content.query.get(random.choice(ids))
    return the_one
