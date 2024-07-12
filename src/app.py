from flask_migrate import Migrate

from src import create_app
from src.config import Config
from src.models import db
from src.modules.user.user_route import user_bp
from src.modules.auth.auth_route import auth_bp
from utils.check_db import connection_check

app = create_app()
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/api')

connection_check()


if __name__ == '__main__':
    app.run(debug=True)
