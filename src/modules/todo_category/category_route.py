from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from src.modules.todo_category.category_service import TodoCategoryService
from utils.exception import NotFoundError

todo_category_bp = Blueprint('todo_category_bp', __name__)


class TodoCategoryForm:
    def __init__(self):
        data = request.get_json()
        self.name = data.get('name')
        self.description = data.get('description')


@todo_category_bp.route('/todos/categories', methods=['POST'])
@jwt_required()
def create_todo_category():
    try:
        form = TodoCategoryForm()

        # direct to service
        data = TodoCategoryService.create_todo_category(
            form.name,
            form.description,
        )

        return jsonify({
            'message': 'todo category created successfully',
            'status': 200,
            'data': data.to_dict()
        }), 200

    except ValueError as e:
        return jsonify({
            'error': {
                'message': str(e),
                'status': 400
            }
        }), 400


@todo_category_bp.route('/todos/categories', methods=['GET'])
@jwt_required()
def get_all_todo_categories():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')

    todo = TodoCategoryService.get_all_todo_category(sort, order)

    return jsonify({
        'status': 200,
        'data': todo
    }), 200


@todo_category_bp.route('/todos/categories/<int:id>', methods=['GET'])
@jwt_required()
def get_todo_category(id):
    try:
        todo = TodoCategoryService.get_todo_category(id)
        return jsonify({
            'status': 200,
            'data': todo.to_dict()
        }), 200 if todo else ('', 404)

    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404


@todo_category_bp.route('/todos/categories/<int:id>', methods=['PUT'])
@jwt_required()
def update_todo_category(id):
    try:
        form = TodoCategoryForm()
        update_data = TodoCategoryService.update_todo_category(
            id,
            form.name,
            form.description,
        )
        return jsonify({
            'message': 'todo updated successfully',
            'status': 201,
            'data': update_data.to_dict()
        })
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404


@todo_category_bp.route('/todos/categories/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_todo_category(id):
    try:
        TodoCategoryService.delete_todo_category(id)
        return jsonify({
            'message': "Todo category deleted successfully",
            'status': 200
        })

    except NotFoundError as e:
        return jsonify({'message': str(e)}), 404
