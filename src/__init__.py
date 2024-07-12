from dotenv import load_dotenv
from flask import Flask
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Hello, world!"
    return app
