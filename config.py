import os

if not os.getenv("GAMESDB_URL"):
    raise RuntimeError("DATABASE_URL is not set")


DEBUG = True
SQLALCHEMY_DATABASE_URI = os.getenv("GAMESDB_URL")
SECRET_KEY = "(wqkkkss1212@#!@!{si)Wqw+"
SQLALCHEMY_TRACK_MODIFICATIONS = False
