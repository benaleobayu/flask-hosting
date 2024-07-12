from src.modules.todo.todo_repository import TodoRepository
from utils.exception import NotFoundError, UnauthorizeError
class Validator:
    @staticmethod
    def todo_validator(category_id, name, description, status):
        if not category_id or not isinstance(category_id, int):
            raise ValueError('category is required')
        if not name or not isinstance(name, str):
            raise ValueError('name is required')
        if not description or not isinstance(description, str):
            raise ValueError('description is required')
        if not status or not isinstance(status, bool):
            raise ValueError('status is required')

class TodoService:
    @staticmethod
    def create_todo(category_id: object, name: object, description: object, status: object) -> object:
        Validator.todo_validator(category_id, name, description, status)

        todo = TodoRepository.create_todo(
            category_id,
            name,
            description,
            status
        )
        return todo


    @staticmethod
    def get_all_todo():
        todos = TodoRepository.get_all_todos()
        return [todo.to_dict() for todo in todos]

    @staticmethod
    def get_todo(id):
        todo = TodoRepository.get_todo(id)
        if not todo:
            raise NotFoundError('todo not found')
        return todo

    @staticmethod
    def update_todo(id: object, category_id: object, name: object, description: object, status: object) -> object:
        Validator.todo_validator(category_id, name, description, status)

        data = TodoService.get_todo(id)
        if not data:
            raise NotFoundError('todo not found')

        try:
            todo = TodoRepository.update_todo(
                id,
                name,
                description,
                status,
                category_id
            )
            return todo
        except Exception as e:
            raise e

    @staticmethod
    def delete_todo(id):
        data = TodoService.get_todo(id)
        if not data:
            raise NotFoundError('todo not found')

        return data
