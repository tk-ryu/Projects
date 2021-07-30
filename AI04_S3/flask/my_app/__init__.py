from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    from my_app.routes import user_routes    
    app.register_blueprint(user_routes.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app


#######################

# from my_app.routes import user_routes

# app = Flask(__name__)
# app.register_blueprint(user_routes.bp)

# @app.route('/')
# def index():
#     return 'Hello World!'

########################

# @app.route('/user/<user_id>')
# def user_page(user_id):
#     return f'Welcome {user_id}!'

# @app.route('/index/', defaults={ 'num' : 0 })
# @app.route('/index/<int:num>')
# def index_number(num):
#     return 'Welcome to Index %i' % int(num)

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)