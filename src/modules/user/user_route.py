from flask import Blueprint, request, jsonify

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def users():
    return "hello this is user pages"