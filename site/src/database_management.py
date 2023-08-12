import os
import mysql.connector
import uuid

class database_management:
    def __init__(self) -> None:
        self.host = os.getenv('DB_HOSTNAME')
        self.user = os.getenv('MYSQL_USER')
        self.password = os.getenv('MYSQL_PASSWORD')
        self.database = os.getenv('MYSQL_DATABASE')

    def database_connetion(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return conn
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def check_user(self, user, email):
        conn = self.database_connetion()
        if not conn:
            return False
        
        try:
            query = "SELECT `ID`, `username`, `email` FROM `user_registration` WHERE `username` = %s OR `email` = %s"

            cursor = conn.cursor()
            cursor.execute(query, (user, email))

            if not cursor.fetchone():
                return True     # Usuário ainda não registrado
            else:
                return False     # Usuário já registrado
        
        except mysql.connector.Error as e:
            print(f"Erro ao conferir usuário no banco de dados: {e}")
            return None
        
        finally:
            conn.close() 

    def new_user_registration(self, user, email, password):
        conn = self.database_connetion()
        if not conn:
            return False
        
        try:
            # Token para verificação do e-mail
            token_auth = str(uuid.uuid1())
            query = "INSERT INTO `user_registration`(`username`, `email`, `password`, `token_auth`) VALUES (%s, %s, %s, %s)"

            cursor = conn.cursor()
            cursor.execute(query, (user, email, password, token_auth))
            conn.commit()
            return True
        
        except mysql.connector.Error as e:
            print(f"Erro ao registrar usuário no banco de dados: {e}")
            return False
        
        finally:
            if cursor:
                cursor.close()
            conn.close()