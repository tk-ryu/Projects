from flask import Blueprint, render_template
from my_app import db
from my_app.models.model import Ingr, Pp_rp, In_rp, Raw_rp, Review, Users

bp = Blueprint('main', __name__)

@bp.route('/')
def user_index():
    top_reviews = db.session.query(Review.recipe_id, db.func.sum(Review.rating)).group_by(Review.recipe_id).order_by(db.func.sum(Review.rating).desc()).limit(5).all()
    top_ratings = [i[1] for i in top_reviews]
    top_recipe_id = [i[0] for i in top_reviews]
    recipe_list = [db.session.query(Raw_rp.name).filter_by(id=i).first().name for i in top_recipe_id]
    # recipe_list = PP_recipes.query.
    return render_template('index.html', ratings=top_ratings, recipes=recipe_list)