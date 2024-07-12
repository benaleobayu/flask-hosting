from src import create_app

from src.modules.user.user_route import user_bp

app = create_app()

app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)