from DataAccess.database import get, add


class UserManager:
    def get_user(self, username, password):
        user = get(
            f"SELECT * FROM users WHERE username='{username}' AND \
                password='{password}'")
        return user

    def add_user(self, username, password, name=None, surname=None):
        if name is None or surname is None:
            add(
                f"INSERT INTO users(username, password) \
                    VALUES('{username}','{password}')")
        else:
            add(
                f"INSERT INTO users(username, password, name, surname) \
                    VALUES('{username}','{password}','{name}','{surname}')")
