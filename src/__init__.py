from datetime import timedelta

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from src.models.user_model import TokenBlacklist

from config import Config
from models import db

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)
    app.config.from_object(Config)

    CORS(
        app,
        support_credentials=True,
        origins=['http://127.0.0.1:3000']
    )

    db.init_app(app)
    migrate = Migrate(app, db)

    jwt = JWTManager(app)

    @app.route('/')
    def index():
        return "Hello, world!"

    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        jti = jwt_payload['jti']
        token = TokenBlacklist.query.filter_by(jti=jti).first()
        return token is not None

    return app
