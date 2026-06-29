from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

from config import Config

mail = Mail()
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'login'
socketIO = SocketIO()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    socketIO.init_app(app, cors_allowed_origins='*')

    from .routes import init_routes
    init_routes(app)

    with app.app_context():
        db.create_all()

    return app