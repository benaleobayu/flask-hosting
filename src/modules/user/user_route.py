from flask import Blueprint, request, jsonify
from utils.exception import NotFoundError, UnauthorizeError

from src.modules.user.user_service import UserService

user_bp = Blueprint('user_bp', __name__)


class UserForm:
    def __init__(self):
        data = request.get_json()
        self.name = data.get('name')
        self.username = data.get('username')
        self.password = data.get('password')
        self.email = data.get('email')

@user_bp.route('/users', methods=['POST'])
def api_create_users():
    try:
        user_form = UserForm()

        #direct to service
        user = UserService.create_user(
            user_form.name,
            user_form.username,
            user_form.email,
            user_form.password
        )

        return jsonify({
            'message': 'user successfully registered',
            'status': 200,
            'data': user.to_dict()
        }), 200
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 400
        }}), 400
