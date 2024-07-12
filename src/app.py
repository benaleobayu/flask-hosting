import os
import sys

from src import create_app
from src.modules.user.user_route import user_bp

app = create_app()

app.register_blueprint(user_bp)


sys.path.insert(0, os.path.dirname(__file__))


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    message = 'It works!\n'
    version = 'Python %s\n' % sys.version.split()[0]
    response = '\n'.join([message, version])
    return [response.encode()]
