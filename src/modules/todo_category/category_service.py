from src.modules.todo_category.category_repository import TodoCategoryRepository
from utils.exception import NotFoundError, UnauthorizeError
class Validator:
    @staticmethod
    def todo_category_validator(name, description):
        if not name or not isinstance(name, str):
            raise ValueError('name is required')
        if not description or not isinstance(description, str):
            raise ValueError('description is required')

class TodoCategoryService:
    @staticmethod
    def create_todo_category(name: object, description: object) -> object:
        Validator.todo_category_validator(name, description)

        todo_category = TodoCategoryRepository.create_todo_category(
            name,
            description,
        )
        return todo_category


    @staticmethod
    def get_all_todo_category(sort=None, order='asc'):
        todo_categories = TodoCategoryRepository.get_all_todo_categories(sort, order)
        return [todo_category.to_dict() for todo_category in todo_categories]

    @staticmethod
    def get_todo_category(id):
        todo_category = TodoCategoryRepository.get_todo_category(id)
        if not todo_category:
            raise NotFoundError('todo_category not found')
        return todo_category

    @staticmethod
    def update_todo_category(id: object, name: object, description: object) -> object:
        Validator.todo_category_validator(name, description)

        data = TodoCategoryRepository.get_todo_category(id)
        if not data:
            raise NotFoundError('todo_category not found')

        try:
            todo_category = TodoCategoryRepository.update_todo_category(
                id,
                name,
                description,
            )
            return todo_category
        except Exception as e:
            raise e

    @staticmethod
    def delete_todo_category(id):
        data = TodoCategoryService.get_todo_category(id)
        if not data:
            raise NotFoundError('todo_category not found')
        category = TodoCategoryRepository.delete_todo_category(id)

        return category
