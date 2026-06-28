"""
==========================================================
database.py

Purpose
-------
This file is responsible for connecting our application
to the SQLite database.

Responsibilities
----------------
1. Create the database engine.
2. Create database sessions.
3. Define the base class that all database models inherit.

Keeping this logic in one file makes the project much
easier to maintain.
==========================================================
"""

# SQLAlchemy is the library that allows Python to communicate
# with SQL databases without writing raw SQL everywhere.
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# ---------------------------------------------------------
# Database Location
# ---------------------------------------------------------
#
# SQLite stores everything inside a single file.
#
# The file does NOT need to exist.
# SQLAlchemy will create it automatically.
#

DATABASE_URL = "sqlite:///job_assistant.db"


# ---------------------------------------------------------
# Create Engine
# ---------------------------------------------------------
#
# The engine is responsible for communicating with
# the database.
#

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# ---------------------------------------------------------
# Session Factory
# ---------------------------------------------------------
#
# Every request to our API will receive its own
# database session.
#

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ---------------------------------------------------------
# Base Class
# ---------------------------------------------------------
#
# Every table in our database will inherit from Base.
#

Base = declarative_base()


# ---------------------------------------------------------
# Dependency
# ---------------------------------------------------------
#
# FastAPI uses this function to obtain
# a database connection.
#

def get_db():
    """
    Creates a database session.

    The session is automatically closed
    after the request finishes.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
