from flask import Blueprint, render_template, request, session, g, url_for
from werkzeug.utils import redirect
from my_app import db
from my_app.models.model import Ingr, Pp_rp, In_rp, Raw_rp, Review, Users


from my_app.forms import ReviewForm
from my_app.forms import RecipeForm


bp = Blueprint('main', __name__)

@bp.route('/')


def main():
    user_name = session.get('user_name')
    top_reviews = db.session.query(Review.recipe_id, db.func.sum(Review.rating)).group_by(Review.recipe_id).order_by(db.func.sum(Review.rating).desc()).limit(3).all()
    top_ratings = [i[1] for i in top_reviews]
    top_recipe_id = [i[0] for i in top_reviews]
    recipe_list = [db.session.query(Raw_rp.name).filter_by(id=i).first().name for i in top_recipe_id]
    # recipe_list = PP_recipes.query.

    results = db.session.query(Review.recipe_id, db.func.count(Review.rating), db.func.avg(Review.rating), Raw_rp.name, Raw_rp.minutes, Raw_rp.ingredients, Raw_rp.tags).filter(In_rp.ingr_id==Ingr.id).filter(In_rp.rp_id==Review.recipe_id).filter(Raw_rp.id==In_rp.rp_id).group_by(Review.recipe_id, Raw_rp.name, Raw_rp.minutes, Raw_rp.ingredients, Raw_rp.tags).order_by(db.func.count(Review.rating).desc()).limit(3).all()

    results2 = db.session.query(Review.recipe_id, db.func.count(Review.rating), db.func.avg(Review.rating), Raw_rp.name, Raw_rp.minutes, Raw_rp.ingredients, Raw_rp.tags).filter(Raw_rp.id==Review.recipe_id).group_by(Review.recipe_id, Raw_rp.name, Raw_rp.minutes, Raw_rp.ingredients, Raw_rp.tags).order_by(db.func.count(Review.rating).desc()).limit(3).all()

    # breakpoint()

    return render_template('index.html', results=results2, user_name = user_name)


@bp.route('/search')
def search():
    ingredient = request.args.get('kw', type=str, default='')
    if ingredient is None:
        return "Please input keywords", 400
    
    elif Ingr.query.filter_by(replaced = ingredient).first() is None:
        return f"{ingredient} not in database", 404

    else:
        ingr = f'%{ingredient}%'
        
        results = db.session.query(Review.recipe_id, db.func.count(Review.rating), db.func.avg(Review.rating), Raw_rp.name, Raw_rp.minutes, Raw_rp.ingredients, Raw_rp.tags).filter(In_rp.ingr_id==Ingr.id).filter(In_rp.rp_id==Review.recipe_id).filter(Raw_rp.id==In_rp.rp_id).filter(Ingr.replaced.ilike(ingr)).group_by(Review.recipe_id, Raw_rp.name, Raw_rp.minutes, Raw_rp.ingredients, Raw_rp.tags).order_by(db.func.count(Review.rating).desc()).limit(5).all()
        
        # breakpoint()


        recipe_ids = [i[0] for i in results]
        review_counts = [i[1] for i in results]

        return render_template('search.html', ids = recipe_ids, counts = review_counts, results=results, keyword=ingredient), 200

# breakpoint()

@bp.route('/recipe/<rp_id>')
def recipe(rp_id):

    recipe = Raw_rp.query.filter_by(id=rp_id).first()
    description = recipe.description
    minutes = recipe.minutes

    rating_avg = float(db.session.query(Review.recipe_id, db.func.avg(Review.rating)).filter(Review.recipe_id == rp_id).group_by(Review.recipe_id).first()[1])
    review_count = review_count = db.session.query(Review.recipe_id, db.func.count(Review.rating)).filter(Review.recipe_id == rp_id).group_by(Review.recipe_id).first()[1]
    review_list = db.session.query(Review.review, Review.rating).filter(Review.recipe_id == rp_id).all()


    form = ReviewForm()

    return render_template('recipe.html', recipe=recipe, rating_avg=rating_avg, review_count=review_count, review_list=review_list, description = description, minutes=minutes, form=form)
















@bp.route('/write_recipe', methods=('GET', 'POST'))
def write():
    form = RecipeForm()
    if request.method =='POST' and form.validate_on_submit():
        raw_recipe = Raw_rp(name = form.subject.data, 
                            minutes = form.time.data,
                            contributor_id = g.user.user_id,
                            ingredients = [form.ingredients1.data,form.ingredients2.data,form.ingredients3.data,form.ingredients4.data,form.ingredients5.data],
                            tags = form.tags.data)
        db.session.add(raw_recipe)
        db.session.commit()

        rp_id = Raw_rp.query.filter_by(name = form.subject.data).first().id
        ingr_id1 = Ingr.query.filter_by(replaced = form.ingredients1.data).first().id
        ingr_id2 = Ingr.query.filter_by(replaced = form.ingredients2.data).first().id
        ingr_id3 = Ingr.query.filter_by(replaced = form.ingredients3.data).first().id
        ingr_id4 = Ingr.query.filter_by(replaced = form.ingredients4.data).first().id
        ingr_id5 = Ingr.query.filter_by(replaced = form.ingredients5.data).first().id


        pp_recipe = Pp_rp(id = rp_id,
                            ingredient_id1 = ingr_id1,
                            ingredient_id2 = ingr_id2,
                            ingredient_id3 = ingr_id3,
                            ingredient_id4 = ingr_id4,
                            ingredient_id5 = ingr_id5,)
        
        # in_rp = In_rp()
        db.session.add(pp_recipe)
        db.session.commit()
        return redirect(url_for('main.index'))
    
    return render_template('write_recipe_form.html', form=form)







    # join1 = db.session.query(In_rp).join(Ingr).filter(Ingr.replaced.ilike('%vanilla%')).all()

    # join2 = db.session.query(In_rp, Ingr).filter(Ingr.replaced.ilike('%vanilla%')).all()

    # join3 = db.session.query(In_rp, Ingr, Review).filter(In_rp.ingr_id==Ingr.id).filter(In_rp.rp_id==Review.recipe_id).filter(Ingr.replaced.ilike('%vanilla%')).all()

    # join4 = db.session.query(Review.recipe_id).filter(In_rp.ingr_id==Ingr.id).filter(In_rp.rp_id==Review.recipe_id).filter(Ingr.replaced.ilike('%vanilla%')).all()

    # join5 = db.session.query(Review.recipe_id, db.func.count(Review.rating)).filter(In_rp.ingr_id==Ingr.id).filter(In_rp.rp_id==Review.recipe_id).filter(Ingr.replaced.ilike('%vanilla%')).group_by(Review.recipe_id).order_by(db.func.count(Review.rating).desc()).limit(5).all()

    # rating_avg = float(db.session.query(Review.recipe_id, db.func.avg(Review.rating)).filter(Review.recipe_id == rp_id).group_by(Review.recipe_id).first()[1])

    # review_count = db.session.query(Review.recipe_id, db.func.count(Review.rating)).filter(Review.recipe_id == rp_id).group_by(Review.recipe_id).first()

    # review_list = db.session.query(Review.review, Review.rating).filter(Review.recipe_id == 3470).all()