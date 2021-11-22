from entities.user import User
import string


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if len(username) < 3:
            raise UserInputError("Username is too short")

        if len(password) < 8:
            raise UserInputError("Password is too short")

        letters = string.ascii_letters + "åäöÅÄÖ"
        only_letters = True
        for character in password:
            if character not in letters:
                only_letters = False
                break
        if only_letters:
            raise UserInputError("Password must contain at least one number or special character")

