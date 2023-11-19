from my_lib.config import host, user, password, db_name, port
import psycopg2


class ConnPost:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            dbname=db_name,
            port=port
        )

    def get_query(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchone()
            print(f"data: {data}")
        return data

    def write_db(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
        self.connection.commit()
        print("write")
