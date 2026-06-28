"""
==========================================================
models.py

This file contains every database table used by the
application.

Each class below becomes one table inside SQLite.
==========================================================
"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date

from .database import Base


class Application(Base):
    """
    Represents one job application.
    """

    __tablename__ = "applications"

    # Unique identifier
    id = Column(Integer, primary_key=True, index=True)

    # Company name
    company = Column(String, nullable=False)

    # Position applied for
    position = Column(String, nullable=False)

    # Current status
    status = Column(String, default="Applied")

    # Date of application
    applied_date = Column(Date)

    # Job location
    location = Column(String)

    # Salary if known
    salary = Column(String)

    # Notes
    notes = Column(String)
