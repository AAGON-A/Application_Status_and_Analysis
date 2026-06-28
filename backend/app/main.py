"""
========================================================
Job Application Assistant
Author: Your Name

This is the entry point of the backend.

Responsibilities:
- Start the FastAPI server
- Register API routes
- Check server health

This file should stay as small as possible.
========================================================
"""

# Import the FastAPI framework.
# FastAPI allows us to build REST APIs quickly.
from fastapi import FastAPI

from app.database.database import engine
from app.database.database import Base

import app.database.models
# ---------------------------------------------------------
# Create Database Tables
# ---------------------------------------------------------
#
# If the tables do not exist,
# SQLAlchemy creates them automatically.
#
Base.metadata.create_all(bind=engine)

# Create the FastAPI application.
# Every API endpoint belongs to this object.
app = FastAPI(
    title="Job Application Assistant",
    description="Backend API for managing job applications.",
    version="1.0.0"
)


@app.get("/")
def root():
    """
    Root endpoint.

    This function is called when someone visits:

        http://localhost:8000/

    It simply tells us that the backend is running.
    """

    return {
        "message": "Job Application Assistant API is running."
    }


@app.get("/health")
def health_check():
    """
    Health check endpoint.

    Useful for:
    - Docker
    - Deployment
    - Monitoring
    """

    return {
        "status": "healthy"
    }
