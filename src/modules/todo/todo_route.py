from flask import Blueprint, request, jsonify
from src.modules.todo.todo_service import TodoService
from utils.exception import NotFoundError

todo_bp = Blueprint('todo_bp', __name__)

class TodoForm:
    def __init__(self):
        data = request.get_json()
        self.name = data.get('name')
        self.description = data.get('description')
        self.status = data.get('status')
        self.category_id = data.get('category_id')


@todo_bp.route('/todos', methods=['POST'])
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
def get_all_todos():
    todo = TodoService.get_all_todo()
    return jsonify({
        'status': 200,
        'data': todo
    }), 200

@todo_bp.route('/todos/<int:id>', methods=['GET'])
def get_todo():
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
def update_todo():
    try:
        form = TodoForm()
        update_todo = TodoService.update_todo(
            form.category_id,
            form.name,
            form.description,
            form.status
        )
        return jsonify({
            'message': 'todo updated successfully',
            'status' : 201,
            'data': update_todo.to_dict()
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
def delete_todo():
    try:
        TodoService.delete_todo(id)
        return jsonify({
            'message': "Todo deleted successfully",
            'status': 200
        })

    except NotFoundError as e:
        return jsonify({'message': str(e)}), 404

