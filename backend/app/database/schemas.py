
"""
==========================================================
schemas.py

Purpose:
---------
Defines the data structure used by the API.

Why?
----
Database Models:
    How data is stored.

Schemas:
    How data is sent and received.
==========================================================
"""

from pydantic import BaseModel
from typing import Optional


class ApplicationCreate(BaseModel):
    """
    Data required when creating a new application.
    """

    company: str
    position: str
    status: Optional[str] = "Applied"
    location: Optional[str] = None
    salary: Optional[str] = None
    notes: Optional[str] = None


class ApplicationResponse(BaseModel):
    """
    Data returned to the client.
    """

    id: int
    company: str
    position: str
    status: str
    location: Optional[str]
    salary: Optional[str]
    notes: Optional[str]

    class Config:
        from_attributes = True
