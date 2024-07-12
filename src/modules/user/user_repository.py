from src.models.user_model import User, db


class UserRepository:

    @staticmethod
    def check_email_exist(email):
        existing = User.query.filter_by(email=email).first()
        return True if existing else False

    @staticmethod
    def check_username_exist(username):
        existing = User.query.filter_by(username=username).first()
        return True if existing else False

    @staticmethod
    def create_user(name, username, email, password):
        new_user = User(
            name=name,
            username=username,
            email=email
        )
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user(id):
        return User.query.get(id)

    @staticmethod
    def update_user(id, name, username, email, password=None):
        try:
            user = User.query.get(id)
            if not user:
                return None

            user.name = name
            user.username = username
            user.email = email
            user.updated_at = db.func.now()

            if password:
                user.set_password(password)

            db.session.commit()

            return user
        except Exception as e:
            db.session.rollback()
            return e

    @staticmethod
    def delete_user(id):
        find_id = User.query.get(id)
        try:
            if not find_id:
                return None

            user = User.query.filter_by(id=id)
            if user:
                db.session.delete(user)
                db.session.commit()
            return user
        except Exception as e:
            db.session.rollback()
            return e
