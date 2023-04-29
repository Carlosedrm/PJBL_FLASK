from flask import Flask, render_template, session, g
from models.auth.user import User
from controllers.admin_controller import admin
from controllers.ajuda_controller import ajuda
from controllers.auth_controller import auth
from controllers.iot_controller import iot
from flask_login import LoginManager
from models.db import db, instance 

def create_app() -> Flask:
    app = Flask(__name__, template_folder="./views/", 
                        static_folder="./static/", 
                        root_path="./")
    
    app.config["TESTING"] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config["SQLALCHEMY_DATABASE_URI"] = instance
    db.init_app(app)
    
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(ajuda, url_prefix='/ajuda')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(iot, url_prefix='/iot')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/')
    def index():
        return render_template("NHome.html")
    
    return app