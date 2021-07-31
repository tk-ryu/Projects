from flask import Blueprint, render_template
from my_app import db

bp = Blueprint('test', __name__)

# breakpoint()


# print(db.Model.metadata.tables)


class Ingr(db.Model):
    __table__ = db.Model.metadata.tables['ingredients_csv']

    def __repr__(self):
        return str(self.id)

class Pp_rp(db.Model):
    __table__ = db.Model.metadata.tables['pp_recipes']

    def __repr__(self):
        return str(self.id)

class In_rp(db.Model):
    __table__ = db.Model.metadata.tables['in_rp']

class Raw_rp(db.Model):
    __table__ = db.Model.metadata.tables['raw_recipes_csv']

    def __repr__(self):
        return self.id

class Review(db.Model):
    __table__ = db.Model.metadata.tables['raw_interactions2_csv']

    def __repr__(self):
        return f"Rating : {self.rating} \nReview : {self.review}"

class Users(db.Model):
    __table__ = db.Model.metadata.tables['pp_users_csv']

    def __repr__(self):
        return self.u

# breakpoint()

# from my_app import Base
# Ingredients2 = Base.classes.pp_users_csv


@bp.route('/test')
def user_index():
    test = Ingr.query.filter_by(id = 4308).first()
    return str(test.id)
    # results = db.session.query(Ingredients2).filter_by(u=1).first()
    # return str(results)