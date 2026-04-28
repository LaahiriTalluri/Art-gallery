import sqlite3

conn = sqlite3.connect("database.db")

with open("sql/schema.sql") as f:
    conn.executescript(f.read())

conn.commit()
conn.close()

print("Database Created Successfully")