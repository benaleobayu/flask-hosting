from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt, jwt_required, get_jwt_identity

from src.models import db
from src.models.user_model import User, TokenBlacklist

from src.modules.user.user_route import api_create_users
from src.modules.user.user_service import UserService

auth_bp = Blueprint('auth_bp', __name__)

class UserForm:
    def __init__(self):
        data = request.get_json()
        self.name = data.get('name')
        self.username = data.get('username')
        self.password = data.get('password')
        self.email = data.get('email')

@auth_bp.route('/register', methods=['POST'])
def api_register():
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



@auth_bp.route('/login', methods=['POST'])
def api_login():
    data = UserForm()

    username = data.username
    password = data.password

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password) and user.isDeleted == '0':
        additional_claims = {
            'id': user.id,
            'name': user.name,
            'username': user.username,
            'email': user.email
        }

        access_token = create_access_token(identity=additional_claims)
        refresh_token = create_refresh_token(identity=additional_claims)
        return jsonify(access_token=access_token, refresh_token=refresh_token), 200
    elif user and user.check_password(password) and user.isDeleted == '1':
        return jsonify({'error': {
            'message': 'user is not active'
        }}), 401
    else:
        return jsonify({'error': {
            'message': 'invalid username or password'
        }}), 404

@auth_bp.route('/refresh', methods=['OPTIONS'])
def refresh_options():
    response = make_response()
    response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:3000'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'error': 'invalid refresh token'}), 422

    print(f'refresh token for user: {current_user}')
    new_access_token = create_access_token(identity=current_user)
    response = jsonify(access_token=new_access_token)
    response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:3000'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def api_logout():
    jti = get_jwt()['jti']
    token = TokenBlacklist(jti=jti)
    db.session.add(token)
    db.session.commit()
    return jsonify(msg="Successfully logged out")
