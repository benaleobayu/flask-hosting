from src.models.user_model import User, db


class UserRepository:

    @staticmethod
    def check_email_exist(email, user_id=None):
        existing = User.query.filter_by(email=email)
        if user_id:
            existing = existing.filter(User.id != user_id)

        existing = existing.first()
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
    def get_mydata_user(id):
        return User.query.get(id)

    @staticmethod
    def get_user(id):
        return User.query.get(id)

    @staticmethod
    def update_user(id, name, username, email=None, password=None):
        try:
            data = User.query.get(id)
            if not data:
                return None

            data.name = name
            data.username = username
            data.updated_at = db.func.now()

            if email and email != data.email:
                if UserRepository.check_email_exist(email, id):
                    raise ValueError('email already exist')

                data.email = email

            if password:
                data.set_password(password)

            db.session.commit()

            return data
        except Exception as e:
            db.session.rollback()
            return e

    @staticmethod
    def update_user_status(id, status):
        try:
            user = User.query.get(id)
            if not user:
                return None

            user.status = status
            user.updated_at = db.func.now()

            db.session.commit()

            return user
        except Exception as e:
            db.session.rollback()
            return e

    @staticmethod
    def update_user_password(id, password):
        try:
            user = User.query.get(id)
            if not user:
                return None

            user.set_password(password)
            user.updated_at = db.func.now()

            db.session.commit()

            return user
        except Exception as e:
            db.session.rollback()
            return e

    @staticmethod
    def delete_user(id):
        try:
            find_data = User.query.get(id)
            if not find_data:
                return None

            if find_data:
                db.session.delete(find_data)
                db.session.commit()
            return find_data
        except Exception as e:
            db.session.rollback()
            return e
