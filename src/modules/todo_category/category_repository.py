from src.models.todo_category_model import TodoCategory, db

class TodoCategoryRepository:
    @staticmethod
    def create_todo_category(
            name,
            description,
    ):
        new_data = TodoCategory(
            name=name,
            description=description,
        )
        db.session.add(new_data)
        db.session.commit()
        return new_data

    @staticmethod
    def get_all_todo_categories():
        return TodoCategory.query.all()

    @staticmethod
    def get_todo_category(id):
        return TodoCategory.query.get(id)

    @staticmethod
    def update_todo_category(
            id,
            name,
            description,
    ):
        try:
            todo_category = TodoCategory.query.get(id)
            if not todo_category:
                return None

            todo_category.name = name,
            todo_category.description = description,
            todo_category.updated_at = db.func.now()

            db.session.commit()
            return todo_category

        except Exception as e:
            db.session.rollback()
            raise e



    @staticmethod
    def delete_todo_category(id):
        todo_category = TodoCategory.query.get(id)
        if todo_category:
            db.session.delete(todo_category)
            db.session.commit()
        return todo_category



