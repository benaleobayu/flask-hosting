from flask import Blueprint, request, jsonify

todo_category_bp = Blueprint('todo_category_bp', __name__)

@todo_category_bp.route('/todos/categories', methods=['POST'])
def create_todo_category():
    pass

@todo_category_bp.route('/todos/categories', methods=['GET'])
def get_all_todo_categories():
    pass

@todo_category_bp.route('/todos/categories/<int:id>', methods=['GET'])
def get_todo_category(id):
    pass

@todo_category_bp.route('/todos/categories/<int:id>', methods=['PUT'])
def update_todo_category(id):
    pass

@todo_category_bp.route('/todos/categories/<int:id>', methods=['DELETE'])
def delete_todo_category(id):
    pass