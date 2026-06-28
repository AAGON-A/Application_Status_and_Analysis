"""
==========================================================
applications.py

Purpose:
---------
Handles all application-related endpoints.

Endpoints:
-----------
POST   /applications
GET    /applications
GET    /applications/{id}
==========================================================
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import Application
from app.database.schemas import (
    ApplicationCreate,
    ApplicationResponse
)

router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)


@router.post(
    "/",
    response_model=ApplicationResponse
)
def create_application(
    application: ApplicationCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new job application.
    """

    new_application = Application(
        company=application.company,
        position=application.position,
        status=application.status,
        location=application.location,
        salary=application.salary,
        notes=application.notes
    )

    db.add(new_application)

    db.commit()

    db.refresh(new_application)

    return new_application


@router.get(
    "/",
    response_model=list[ApplicationResponse]
)
def get_all_applications(
    db: Session = Depends(get_db)
):
    """
    Return every application.
    """

    applications = db.query(Application).all()

    return applications


@router.get(
    "/{application_id}",
    response_model=ApplicationResponse
)
def get_application(
    application_id: int,
    db: Session = Depends(get_db)
):
    """
    Return one application by ID.
    """

    application = (
        db.query(Application)
        .filter(Application.id == application_id)
        .first()
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return application
