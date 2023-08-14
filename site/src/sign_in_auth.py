from flask import redirect, url_for
from src.database_management import database_management

class sign_in_auth:
    def __init__(self, user, password) -> None:
        self.user = user
        self.password = password

    def check_login(self):
        check_user = database_management()
        user = check_user.check_login(self.user)
        
        if (user is not None and (self.user == user[1] or self.user == user[2]) and self.password == user[3]):
            return True
        else:
            return False