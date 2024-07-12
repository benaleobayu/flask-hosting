from flask import Blueprint, request, jsonify

todo_bp = Blueprint('todo_bp', __name__)

@todo_bp.route('/todos', methods=['POST'])
def create_todo():
    pass

@todo_bp.route('/todos', methods=['GET'])
def get_all_todos():
    pass

@todo_bp.route('/todos/<int:id>', methods=['GET'])
def get_todo():
    pass

@todo_bp.route('/todos/<int:id>', methods=['PUT'])
def update_todo():
    pass

@todo_bp.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo():
    pass

