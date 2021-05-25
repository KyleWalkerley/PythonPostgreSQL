import os
import datetime
import psycopg2

from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(os.environ["TEST_URL"])

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

INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp) VALUES (%s, %s);"
INSERT_USER = "INSERT INTO users (username) VALUES (%s)"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > %s;"
SELECT_WATCHED_MOVIES = """SELECT movies.* FROM movies 
JOIN watched ON movie.id = watched.movie_id
JOIN users ON users.username = watched.user_username
WHERE users.username = %s;"""
INSERT_WATCHED_MOVIE = "INSERT INTO watched (user_username, movie_id) VALUES (%s, %s)"
SEARCH_MOVIES = "SELECT * FROM movies WHERE title LIKE %s;"


def create_tables():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_MOVIES_TABLE)
            cursor.execute(CREATE_USERS_TABLE)
            cursor.execute(CREATE_WATCHED_TABLE)

def add_user(username):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_USER, (username,))


def add_movie(title, release_timestamp):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_MOVIES, (title, release_timestamp))

def get_movies(upcoming=False):
    with connection:
        with connection.cursor() as cursor:
            Cursor = connection.cursor()
            if upcoming:
                today_timestamp = datetime.datetime.today().timestamp()
                Cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
            else:
                Cursor.execute(SELECT_ALL_MOVIES)
            return Cursor.fetchall


def search_movies(search_term):
    with connection:
        with connection.cursor() as cursor:
            Cursor = connection.cursor()
            Cursor.execute(SEARCH_MOVIES, (f"%{search_term}%", ))
            return Cursor.fetchall()

def watch_movie(username, movie_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_WATCHED_MOVIE, (username, movie_id))

def get_watched_movies(username):
    with connection:
        with connection.cursor() as cursor:
            Cursor = connection.cursor()
            Cursor.execute(SELECT_WATCHED_MOVIES, (username, ))
            return Cursor.fetchall()