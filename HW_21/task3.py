import sqlite3

def try_commit(query):
    try:
        cursor.execute(query)
        db.commit()
    except Exception:
        print(f"Wrong value in {query}")

db = sqlite3.connect("HW_21_task3.db.sqlite")
cursor = db.cursor()

query = ("CREATE TABLE IF NOT EXISTS users ("
         "id INTEGER PRIMARY KEY AUTOINCREMENT,"
         "first_name TEXT NOT NULL,"
         "last_name TEXT NOT NULL,"
         "age INTEGER)")

cursor.execute(query)


query = ("INSERT INTO users (first_name, last_name, age) "
         "values ('John', 'Smith', 18)")

try_commit(query)


query = ("INSERT INTO users (first_name, last_name, age) "
         "values (Null, 'Smith', 18)")

try_commit(query)


query = ("INSERT INTO users (first_name, last_name, age) "
         "values ('John', Null, 18)")

try_commit(query)


query = ("INSERT INTO users (first_name, last_name, age) "
         "values (Null, Null, 18)")

try_commit(query)


from pprint import pprint

query = "SELECT * FROM users"
res = cursor.execute(query)
pprint(res.fetchall())