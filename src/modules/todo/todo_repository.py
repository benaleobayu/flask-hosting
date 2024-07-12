from src.models.todo_model import Todo, db
from flask_jwt_extended import get_jwt_identity, jwt_required

class TodoRepository:
    @staticmethod
    def create_todo(
            name,
            description,
            status,
            category_id
    ):
        new_data = Todo(
            name=name,
            description=description,
            status=status,
            category_id=category_id
        )
        db.session.add(new_data)
        db.session.commit()
        return new_data

    @staticmethod
    def get_all_todos():
        current_userId = get_jwt_identity()
        return Todo.query.filter_by(user_id=current_userId).order_by(Todo.created_at.desc()).all()

    @staticmethod
    def get_todo(id):
        return Todo.query.get(id)

    @staticmethod
    def update_todo(
            id,
            name,
            description,
            status,
            category_id
    ):
        try:
            todo = Todo.query.get(id)
            if not todo:
                return None

            todo.name = name,
            todo.description = description,
            todo.status = status,
            todo.category_id = category_id,
            todo.updated_at = db.func.now()

            db.session.commit()
            return todo

        except Exception as e:
            db.session.rollback()
            raise e



    @staticmethod
    def delete_todo(id):
        todo = Todo.query.get(id)
        if todo:
            db.session.delete(todo)
            db.session.commit()
        return todo



