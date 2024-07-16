from flask import Blueprint, request, jsonify
from src.modules.todo.todo_service import TodoService
from utils.exception import NotFoundError
from flask_jwt_extended import jwt_required

todo_bp = Blueprint('todo_bp', __name__)

class TodoForm:
    def __init__(self):
        data = request.get_json()
        self.name = data.get('name')
        self.description = data.get('description')
        self.status = data.get('status')
        self.category_id = data.get('category_id')


@todo_bp.route('/todos', methods=['POST'])
@jwt_required()
def create_todo():
    try:
        form = TodoForm()

        # direct to service
        todo = TodoService.create_todo(
            form.category_id,
            form.name,
            form.description,
            form.status
        )

        return jsonify({
            'message': 'todo created successfully',
            'status': 200,
            'data': todo.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({
            'error': {
                'message': str(e),
                'status': 400
            }
        }), 400

@todo_bp.route('/todos', methods=['GET'])
@jwt_required()
def get_all_todos():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')
    todo = TodoService.get_all_todo(sort, order)
    return jsonify({
        'status': 200,
        'data': todo
    }), 200

@todo_bp.route('/todos/<int:id>', methods=['GET'])
@jwt_required()
def get_todo(id):
    try:
        todo = TodoService.get_todo(id)
        return jsonify({
            'status': 200,
            'data': todo.to_dict()
        }), 200 if todo else ('', 404)

    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404

@todo_bp.route('/todos/<int:id>', methods=['PUT'])
@jwt_required()
def update_todo(id):
    try:
        form = TodoForm()
        data = TodoService.update_todo(
            id,
            form.category_id,
            form.name,
            form.description,
            form.status
        )
        return jsonify({
            'message': 'todo updated successfully',
            'status' : 201,
            'data': data.to_dict()
        })
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404

@todo_bp.route('/todos/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_todo(id):
    try:
        TodoService.delete_todo(id)
        return jsonify({
            'message': "Todo deleted successfully",
            'status': 200
        })

    except NotFoundError as e:
        return jsonify({'message': str(e)}), 404

