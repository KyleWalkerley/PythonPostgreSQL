import datetime
import sqlite3
from sqlite3.dbapi2 import Cursor

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies(
    title TEXT,
    release_timestamp REAL,
    watched INTEGER
);"""

INSERT_MOVIES = "INSERT INTO movies (title, released_timestamp, watched) VALUES (?, ?, 0);"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM movies WHERE watched = 1;"

connection = sqlite3.connect("data.db")

def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)

def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_timestamp))

def get_movies(upcoming=False):
    with connection:
        Cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            Cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            Cursor.execute(SELECT_ALL_MOVIES)
        return Cursor.fetchall

def watch_movie(title):
    pass

def get_watched_movies():
    with connection:
        Cursor = connection.cursor()
        Cursor.execute(SELECT_WATCHED_MOVIES)
        return cursor.fetchall()