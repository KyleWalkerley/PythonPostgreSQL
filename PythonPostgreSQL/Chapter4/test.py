import datetime
import sqlite3
from sqlite3.dbapi2 import Cursor

connection = sqlite3.connect("data.db")

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies(
    title TEXT,
    released_timestamp REAL 
);"""

CREATE_WATCHLIST_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    watcher_name TEXT,
    title TEXT,
);"""

INSERT_MOVIES = "INSERT INTO movies (title, released_timestamp) VALUES (?, ?);"
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE released_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM watched WHERE watcher_name = ?;"
INSERT_WATCHED_MOVIE = "INSERT INTO watched (watcher_name, title) VALUES (?, ?)"
SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title =?;"



def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_WATCHLIST_TABLE)

def add_movie(title, released_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES, (title, released_timestamp))

def get_movies(upcoming=False):
    with connection:
        Cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            Cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            Cursor.execute(SELECT_ALL_MOVIES)
        return Cursor.fetchall

def watch_movie(username, title):
    with connection:
        connection.execute(DELETE_MOVIE, (title,))
        connection.execute(INSERT_WATCHED_MOVIE, (username, title))

def get_watched_movies(username):
    with connection:
        Cursor = connection.cursor()
        Cursor.execute(SELECT_WATCHED_MOVIES, (username, ))
        return Cursor.fetchall()