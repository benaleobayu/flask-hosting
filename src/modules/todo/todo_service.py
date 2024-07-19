from src.modules.todo.todo_repository import TodoRepository
from utils.exception import NotFoundError, UnauthorizeError
class Validator:
    @staticmethod
    def todo_validator(category_id, name, description, status):
        if not category_id:
            raise ValueError('category is required')
        if not name:
            raise ValueError('name is required')
        if not description:
            raise ValueError('description is required')


        if not isinstance(category_id, int):
            raise ValueError('category_id must be an integer')

class TodoService:
    @staticmethod
    def create_todo(category_id, name, description, status, user_id=None,):
        Validator.todo_validator(category_id, name, description, status)

        todo = TodoRepository.create_todo(
            category_id,
            user_id,
            name,
            description,
            status,
        )
        return todo


    @staticmethod
    def get_all_todo(sort=None, order='asc'):
        todos = TodoRepository.get_all_todos(sort, order)
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
    def update_todo_status(
            id,
            status
    ):
        data = TodoService.get_todo(id)
        if not data:
            raise NotFoundError('todo not found')

        try:
            todo = TodoRepository.update_todo_status(
                id,
                status
            )
            return todo
        except Exception as e:
            raise e

    @staticmethod
    def delete_todo(id):
        find = TodoService.get_todo(id)
        if not find:
            raise NotFoundError('todo not found')

        data = TodoRepository.delete_todo(id)
        return data
