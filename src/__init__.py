import os
from datetime import timedelta

from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager

from src.models.user_model import TokenBlacklist


load_dotenv()

# environment
# os.environ['FLASK_APP'] = 'src.app'
def create_app():
    app = Flask(__name__)

    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=120)

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
