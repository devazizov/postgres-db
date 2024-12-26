import psycopg2
from psycopg2.extras import RealDictCursor


class Database:
    def __init__(
        self, db_name: str, db_user: str, db_password: str, db_port: int, db_host: str
    ) -> None:
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port

    @property
    def connect(self):
        return psycopg2.connect(
            dbname=self.db_name,
            user=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            cursor_factory=RealDictCursor,
        )

    def execute(
        self,
        sql: str,
        params: tuple = None,
        fetchall: bool = False,
        fetchone: bool = False,
        commit: bool = False,
    ) -> dict | tuple | None:
        connection = self.connect

        if not params:
            params = ()

        cursor = connection.cursor()

        cursor.execute(sql, params)

        data = None
        if fetchall:
            data = cursor.fetchall()

        elif fetchone:
            data = cursor.fetchone()

        else:
            data = None

        if commit:
            connection.commit()

        cursor.close()
        connection.close()
        return data

    def create_users_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            user_id VARCHAR(255) UNIQUE,
            full_name VARCHAR(255)
        )
        """

        self.execute(sql=sql, commit=True)

    def create(self, user_id: str, full_name: str):
        sql = """
            INSERT INTO users (user_id, full_name) VALUES (%s, %s)
        """
        params = (
            user_id,
            full_name,
        )
        self.execute(sql=sql, params=params, commit=True)

    def read(self, user_id: str):
        sql = """
            SELECT * FROM users WHERE user_id = %s
        """
        params = (user_id,)
        return self.execute(sql=sql, params=params, fetchone=True)

    def update(self, user_id: str, full_name: str):
        sql = """
            UPDATE users SET full_name = %s WHERE user_id = %s
        """
        params = (full_name, user_id)
        self.execute(sql=sql, params=params, commit=True)

    def delete(self, user_id: str):
        sql = """
            DELETE FROM users WHERE user_id = %s
        """
        params = (user_id,)
        self.execute(sql=sql, params=params, commit=True)

    def list(self):
        sql = """
            SELECT * FROM users
        """
        return self.execute(sql=sql, fetchall=True)

    def count(self):
        sql = """
            SELECT COUNT(*) FROM users
        """
        return self.execute(sql=sql, fetchone=True)


db = Database(
    db_name="users",
    db_user="postgres",
    db_password="0000",
    db_host="localhost",
    db_port=5432,
)

db.create_users_table()
