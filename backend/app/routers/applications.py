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

from typing import Optional

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


@router.put("/{application_id}", response_model=ApplicationResponse)
def update_application(
    application_id: int,
    updated_data: ApplicationUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing application.
    Only fields provided in the request will be changed.
    """

    application = db.query(Application).filter(Application.id == application_id).first()

    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    # Update only provided fields
    if updated_data.company is not None:
        application.company = updated_data.company

    if updated_data.position is not None:
        application.position = updated_data.position

    if updated_data.status is not None:
        application.status = updated_data.status

    if updated_data.location is not None:
        application.location = updated_data.location

    if updated_data.salary is not None:
        application.salary = updated_data.salary

    if updated_data.notes is not None:
        application.notes = updated_data.notes

    db.commit()
    db.refresh(application)

    return application

@router.delete("/{application_id}")
def delete_application(
    application_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete an application permanently.
    """

    application = db.query(Application).filter(Application.id == application_id).first()

    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    db.delete(application)
    db.commit()

    return {"message": "Application deleted successfully"}
@router.get("/", response_model=list[ApplicationResponse])
def get_all_applications(
    status: Optional[str] = None,
    company: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Return all applications with optional filters.
    """

    query = db.query(Application)

    # Filter by status if provided
    if status:
        query = query.filter(Application.status == status)

    # Filter by company if provided
    if company:
        query = query.filter(Application.company.contains(company))

    return query.all()

