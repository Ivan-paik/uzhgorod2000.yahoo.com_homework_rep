import sqlite3

def try_commit(query):
    try:
        cursor.execute(query)
        db.commit()
    except Exception:
        print(f"Wrong value in {query}")

db = sqlite3.connect("HW_21_task4.db.sqlite")
cursor = db.cursor()

query = ("CREATE TABLE IF NOT EXISTS users ("
         "id INTEGER PRIMARY KEY AUTOINCREMENT,"
         "first_name TEXT,"
         "last_name TEXT,"
         "age INTEGER,"
         "UNIQUE(first_name, last_name))")

cursor.execute(query)


query = ("INSERT INTO users (first_name, last_name, age) "
         "values ('John', 'Smith', 18)")

try_commit(query)


query = ("INSERT INTO users (first_name, last_name, age) "
         "values ('John', 'Lennon', 18)")

try_commit(query)


query = ("INSERT INTO users (first_name, last_name, age) "
         "values ('Adam', 'Smith', 18)")

try_commit(query)


query = ("INSERT INTO users (first_name, last_name, age) "
         "values ('John', 'Smith', 18)")

try_commit(query)


# Null value is ignored for unique
query = ("INSERT INTO users (first_name, last_name, age) "
         "values (Null, 'Smith', 18)")

try_commit(query)


query = ("INSERT INTO users (first_name, last_name, age) "
         "values (Null, 'Smith', 18)")

try_commit(query)


from pprint import pprint

query = "SELECT * FROM users"
res = cursor.execute(query)
pprint(res.fetchall())