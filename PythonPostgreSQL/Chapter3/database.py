import sqlite3

connection = sqlite3.connect("database.db")

def create_table():
    with connection:
        connection.execute("CREATE TABLE entries (content TEXT, date TEXT);")

def add_entry(entry_content, entry_date):
    with connection:
        connection.execute("INSERT INTO entries VALUES ('This is some test content.', '01-01-2020');")

def get_entries():
    return entries