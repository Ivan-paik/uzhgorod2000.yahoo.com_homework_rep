import sqlite3

db = sqlite3.connect("HW_21_task1.db.sqlite")
cursor = db.cursor()

query = ("CREATE TABLE IF NOT EXISTS users ("
         "id INTEGER PRIMARY KEY AUTOINCREMENT,"
         "first_name TEXT,"
         "last_name TEXT,"
         "age INTEGER)")

cursor.execute(query)

data = [
    ("John", "Smith", 18),
    ("Johnny", "Walker", 156),
    ("Jim", "Beam", 228),
    ("Jack", "Daniel's", 157),
    ("Pierre", "Pérignon", 102)
]

query = "INSERT INTO users (first_name, last_name, age) VALUES (?, ?, ?)"

cursor.executemany(query, data)
db.commit()

# Null value in field
query = ("INSERT INTO users (first_name, last_name, age) "
         "values ('John', Null, 18)")

cursor.execute(query)
db.commit()


from pprint import pprint

query = "SELECT * FROM users"
res = cursor.execute(query)
pprint(res.fetchall())