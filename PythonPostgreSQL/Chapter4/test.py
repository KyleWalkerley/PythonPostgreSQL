import datetime
import sqlite3
from sqlite3.dbapi2 import Cursor

connection = sqlite3.connect("data.db")

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_timestamp REAL 
);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users(
    username TEXT PRIMARY KEY
);"""

CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);"""

INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?);"
INSERT_USER = "INSERT INTO users (username) VALUES (?)"
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = """SELECT movies.* FROM movies 
JOIN watched ON movie.id = watched.movie_id
JOIN users ON users.username = watched.user_username
WHERE users.username = ?;"""
INSERT_WATCHED_MOVIE = "INSERT INTO watched (user_username, movie_id) VALUES (?, ?)"
SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title =?;"
SEARCH_MOVIES = "SELECT * FROM movies WHERE title LIKE ?;"
CREATE_RELEASE_INDEX = "CREATE INDEX IF NOT EXISTS idx_movies_release ON movies(release_timestamp);"


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_RELEASE_INDEX)

def add_user(username):
    with connection:
        connection.execute(INSERT_USER, (username,))


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


def search_movies(search_term):
    with connection:
        Cursor = connection.cursor()
        Cursor.execute(SEARCH_MOVIES, (f"%{search_term}%", ))
        return Cursor.fetchall()

def watch_movie(username, movie_id):
    with connection:
        connection.execute(INSERT_WATCHED_MOVIE, (username, movie_id))

def get_watched_movies(username):
    with connection:
        Cursor = connection.cursor()
        Cursor.execute(SELECT_WATCHED_MOVIES, (username, ))
        return Cursor.fetchall()