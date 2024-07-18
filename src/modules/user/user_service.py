import re

from src.modules.user.user_repository import UserRepository
from utils.exception import NotFoundError, UnauthorizeError
from flask_jwt_extended import get_jwt_identity

class Validator:
    @staticmethod
    def user_validator(name, username, email, password):
        if UserRepository.check_email_exist(email):
            raise ValueError('email already exist')
        if UserRepository.check_username_exist(username):
            raise ValueError('username already exist')


        if not name or not isinstance(name, str):
            raise ValueError('name is required')
        if not username or not isinstance(username, str):
            raise ValueError('username is required')
        if not email or not isinstance(email, str):
            raise ValueError('email is required')
        if not password or not isinstance(password, str) or len(password) <= 6:
            raise ValueError('password is required and min must be 6 character')

        regex_username = '^[a-zA-Z0-9]*$'
        if not re.match(regex_username, username):
            raise ValueError('only alpabeth and number is allowed in username')
        regex_email = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
        if not re.match(regex_email, email):
            raise ValueError('please input the valid email')

class UserService:
    @staticmethod
    def create_user(name, username, email, password):
        Validator.user_validator(name, username, email, password)

        return UserRepository.create_user(
            name,
            username,
            email,
            password
        )


    @staticmethod
    def get_all_users():
        users = UserRepository.get_all_users()
        return [user.to_dict() for user in users]

    @staticmethod
    def get_user(id):
        user = UserRepository.get_user(id)
        if not user:
            raise NotFoundError('user not found')
        return user

    @staticmethod
    def update_user(id,name,username,email, password=None):
        Validator.user_validator(name,username,email,password)

        data = UserService.get_user(id)
        if not data:
            raise NotFoundError('user not found')

        try:
            user = UserRepository.update_user(
                id,
                name,
                username,
                email,
                password
            )
            return user
        except Exception as e:
            raise e

    @staticmethod
    def update_user_status(id, status):
        data = UserService.get_user(id)
        if not data:
            raise NotFoundError('user not found')

        user = UserRepository.update_user_status(id, status)
        return user

    @staticmethod
    def update_user_password(id, password):
        Validator.user_validator(password)

        data = UserService.get_user(id)
        if not data:
            raise NotFoundError('user not found')

        user = UserRepository.update_user_password(id, password)
        return user

    @staticmethod
    def delete_user(id):
        data = UserService.get_user(id)
        if not data:
            raise NotFoundError('user not found')
        user = UserRepository.delete_user(id)
        return user
