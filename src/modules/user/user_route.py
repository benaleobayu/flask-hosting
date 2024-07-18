from flask import Blueprint, request, jsonify
from utils.exception import NotFoundError, UnauthorizeError
from flask_jwt_extended import jwt_required

from src.modules.user.user_service import UserService

user_bp = Blueprint('user_bp', __name__)


class UserForm:
    def __init__(self):
        data = request.get_json()
        self.name = data.get('name')
        self.username = data.get('username')
        self.password = data.get('password')
        self.email = data.get('email')
        self.status = data.get('status')

@user_bp.route('/api/users', methods=['POST'])
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

@user_bp.route('/users', methods=['GET'])
@jwt_required()
def api_get_users():
    users = UserService.get_all_users()
    return jsonify({
        'status': 200,
        'data': users
    }) if users else ('', 404)

@user_bp.route('/users/<int:id>', methods=['GET'])
@jwt_required()
def api_get_user(id):
    try:
        user = UserService.get_user(id)
        return jsonify({
            'status': 200,
            'data': user.to_dict()
        })
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404

@user_bp.route('/users/<int:id>', methods=['PUT'])
@jwt_required()
def api_update_user(id):
    try:
        form = UserForm()
        user = UserService.update_user(
            id,
            form.name,
            form.username,
            form.email
        )
        return jsonify({
            'message': 'user updated successfully',
            'status': 201,
            'data': user.to_dict()
        })
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404

@user_bp.route('/users/<int:id>/status', methods=['PATCH'])
@jwt_required()
def api_update_user_status(id):
    try:
        form = UserForm()
        user = UserService.update_user_status(
            id,
            form.status
        )
        return jsonify({
            'message': 'user status updated successfully',
            'status': 201,
        }), 201
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404

@user_bp.route('/users/<int:id>/password', methods=['PATCH'])
def api_update_user_password(id):
    try:
        form = UserForm()
        UserService.update_user_password(
            id,
            form.password
        )
        return jsonify({
            'message': 'user password updated successfully',
            'status': 201
        }), 201
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400


@user_bp.route('/users/<int:id>', methods=['DELETE'])
@jwt_required()
def api_delete_user(id):
    try:
        UserService.delete_user(id)
        return jsonify({
            'message': 'user deleted successfully',
            'status': 200
        })
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404