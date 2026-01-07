"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.

Uses a persistent SQLite database to store activities and enrollments.
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import os
from pathlib import Path

from database import get_db, Activity, Enrollment, SessionLocal
from init_db import init_db

# Initialize database on startup
init_db()

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities(db: Session = Depends(get_db)):
    """Get all activities with their current enrollment counts"""
    activities = db.query(Activity).all()
    result = {}
    
    for activity in activities:
        enrollment_count = db.query(Enrollment).filter(
            Enrollment.activity_id == activity.id
        ).count()
        participants = [e.student_email for e in activity.enrollments]
        
        result[activity.name] = {
            "description": activity.description,
            "schedule": activity.schedule,
            "max_participants": activity.max_participants,
            "participants": participants
        }
    
    return result


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str, db: Session = Depends(get_db)):
    """Sign up a student for an activity"""
    # Find the activity
    activity = db.query(Activity).filter(Activity.name == activity_name).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Check if student is already signed up
    existing_enrollment = db.query(Enrollment).filter(
        Enrollment.activity_id == activity.id,
        Enrollment.student_email == email
    ).first()
    
    if existing_enrollment:
        raise HTTPException(
            status_code=400,
            detail="Student is already signed up"
        )
    
    # Check if activity is full
    current_count = db.query(Enrollment).filter(
        Enrollment.activity_id == activity.id
    ).count()
    
    if current_count >= activity.max_participants:
        raise HTTPException(
            status_code=400,
            detail="Activity is full"
        )

    # Add enrollment
    enrollment = Enrollment(activity_id=activity.id, student_email=email)
    db.add(enrollment)
    db.commit()
    
    return {"message": f"Signed up {email} for {activity_name}"}


@app.delete("/activities/{activity_name}/unregister")
def unregister_from_activity(activity_name: str, email: str, db: Session = Depends(get_db)):
    """Unregister a student from an activity"""
    # Find the activity
    activity = db.query(Activity).filter(Activity.name == activity_name).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Find the enrollment
    enrollment = db.query(Enrollment).filter(
        Enrollment.activity_id == activity.id,
        Enrollment.student_email == email
    ).first()
    
    if not enrollment:
        raise HTTPException(
            status_code=400,
            detail="Student is not signed up for this activity"
        )

    # Remove enrollment
    db.delete(enrollment)
    db.commit()
    
    return {"message": f"Unregistered {email} from {activity_name}"}
