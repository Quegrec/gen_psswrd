"""
importer sqlite3
connecter au fichier

requêtes
"""
import sqlite3

DATABASE = 'database.db'
SCHEMA = 'db_schema.sql'

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

with open(SCHEMA, 'r') as f:
    schema = f.read()
connection.executescript(schema)

query = "INSERT INTO passwords (password, name) VALUES (?, ?)"
cursor.execute(query, ("sfgdggr", "Discord"))
connection.commit()

rows = cursor.execute("SELECT * FROM passwords")
for row in rows:
    print(row)