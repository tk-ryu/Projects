from flask import Blueprint, render_template
from my_app import db

bp = Blueprint('test', __name__)

# breakpoint()


# print(db.Model.metadata.tables)


# class Ingredients(db.Model):
#     __table_args__= {'schema':'recipe_project'}
#     __table__ = db.Model.metadata.tables['ingredients']

#     def __repr__(self):
#         return str(self.u)

# breakpoint()

from my_app import Base
Ingredients2 = Base.classes.pp_users_csv


@bp.route('/test')
def user_index():
    # test = Ingredients.query.filter_by(id = 4308).first()
    # return str(test)
    results = db.session.query(Ingredients2).filter_by(u=1).first()
    return str(results)