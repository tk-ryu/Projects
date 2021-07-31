from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.ext.automap import automap_base
# import config

# db = SQLAlchemy()


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/postgres'

# with app.app_context():
db.init_app(app)
db.Model.metadata.reflect(db.engine)

# Base = automap_base()
# Base.prepare(db.engine, reflect=True)



from my_app.routes import (main_route,user_routes)
from my_app.models import model
app.register_blueprint(main_route.bp)
app.register_blueprint(user_routes.bp)
app.register_blueprint(model.bp)



'''
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/postgres'

    with app.app_context():
        db.init_app(app)
        db.Model.metadata.reflect(db.engine)


    from my_app.routes import (main_route,user_routes,test)
    app.register_blueprint(main_route.bp)
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(test.bp)

    
    return app
'''


if __name__ == '__main__':
    # app = create_app()
    app.run(debug=True)