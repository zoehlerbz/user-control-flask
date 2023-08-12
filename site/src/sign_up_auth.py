from flask import redirect, url_for
from src.database_management import database_management
import re

class sign_up_auth:
    def __init__(self, user, email, password, repeat_password) -> None:
        self.user = user
        self.email = email
        self.password = password
        self.repeat_password = repeat_password

    def user_registration(self):
        if self.user_requirements() and self.email_requirements() and self.password_requirements():
            db_user = database_management()
            if db_user.new_user_registration(self.user, self.email, self.password):
                return True
            return False
        return False

    def user_requirements(self):
        if not isinstance(self.user, str):
            # Username deve ser alfanumérico
            return False
        elif not bool(self.user):
            # Username não pode ser vazio
            return False
        elif len(self.user) <= 2 or len(self.user) > 50:
            # Username deve ter entre 3 e 50 caracteres
            return False
        else:
            return True
     
    def email_requirements(self):
        '''
        Para o e-mail ser válido, deve ter:

            [a-zA-Z0-9._%+-]+ : Um ou mais caracteres alfanuméricos, pontos, underscores, porcentagens e sinais de mais e menos.
            @ : O caractere "@".
            [a-zA-Z0-9.-]+ : Um ou mais caracteres alfanuméricos, pontos e hífens.
            \. : O caractere ".".
            [a-zA-Z]{2,} : Dois ou mais caracteres alfabéticos para o domínio (por exemplo, ".com", ".org").
        '''
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(pattern, self.email) is None:
            # Email deve combinar com os padrões
            return False
        elif len(self.email) > 150:
            # Email deve ter até 150 caracteres
            return False
        else:
            return True
    
    def password_requirements(self):
        if not bool(self.password):
            # Password não pode ser vazio
            return False
        elif len(self.password) < 8:
            # Password deve ter mais de 8 caracteres
            return False
        elif self.password != self.repeat_password:
            # Password deve ser igual a Repeat Password
            return False
        else:
            return True