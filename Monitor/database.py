import pymysql
import pymysql.cursors

from config import host, user, password, db_name

connection = pymysql.connect(
    host = host,
    port = 3306,
    user = user,
    password = password,
    database = db_name,
    cursorclass = pymysql.cursors.DictCursor
)

def get_db(message):
    db = (f"id{message.from_user.id}")

    return db

def create_table(message):
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE TABLE id{get_db(message)} (id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age VARCHAR(255), date VARCHAR(255))")

        connection.commit()