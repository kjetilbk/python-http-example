import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',  # default, can be omitted
    'port': '3306',  # default, can be omitted
    'database': 'flaskapp'
}
connection = mysql.connector.connect(**config)


def list_people(max_age):
    cursor = connection.cursor(dictionary=True)
    list_query = "SELECT * FROM people WHERE age < %s";
    cursor.execute(list_query, (max_age,))
    people = list(cursor)
    cursor.close()
    return people