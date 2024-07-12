from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt, jwt_required, get_jwt_identity

from src.models import db
from src.models.user_model import User, TokenBlacklist

from src.modules.user.user_route import api_create_users
from src.modules.user.user_service import UserService

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/api/register', methods=['POST'])
def api_register():
    api_create_users()

@auth_bp.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        additional_claims = {
            'name': user.name,
            'username': user.username,
            'email': user.email,
        }

        access_token = create_access_token(identity=additional_claims)
        refresh_token = create_refresh_token(identity=additional_claims)
        return jsonify(access_token=access_token, refresh_token=refresh_token), 200
    else:
        return jsonify({'error': {
            'message': 'invalid username or password'
        }}), 401

@auth_bp.route('/api/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'error': 'invalid refresh token'}), 422

    print(f'refresh token for user: {current_user}')
    new_access_token = create_access_token(identity=current_user)
    return jsonify(access_token=new_access_token), 200

@auth_bp.route('/api/logout', methods=['POST'])
@jwt_required()
def api_logout():
    jti = get_jwt()['jti']
    token = TokenBlacklist(jti=jti)
    db.session.add(token)
    db.session.commit()
    return jsonify(msg="Successfully logged out")
