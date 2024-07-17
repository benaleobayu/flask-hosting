from flask_cors import CORS
from flask_migrate import Migrate

from src import create_app
from src.config import Config
from src.models import db
from src.modules.auth.auth_route import auth_bp
from src.modules.todo.todo_route import todo_bp
from src.modules.todo_category.category_route import todo_category_bp
from src.modules.user.user_route import user_bp
from utils.check_db import connection_check

app = create_app()
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(todo_bp, url_prefix='/api')
app.register_blueprint(todo_category_bp, url_prefix='/api')

connection_check()

devUrl = 'https://simple-todo-4klznynxv-stafakurs-projects.vercel.app/auth/register'
prodUrl = 'https://simple-todo-three-pied.vercel.app'

CORS(
    app,
    supports_credentials=True,
    origins=[
        'http://127.0.0.1:3000',
        devUrl,
        prodUrl
    ],
    allow_headers=['Content-Type', 'Authorization'],
    methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
)

if __name__ == '__main__':
    app.run(debug=True)
