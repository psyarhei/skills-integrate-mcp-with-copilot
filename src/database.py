"""
Database models for the High School Management System
"""

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
from pathlib import Path

# Create database directory if it doesn't exist
db_dir = Path(__file__).parent.parent / "data"
db_dir.mkdir(exist_ok=True)

# SQLite database URL
DATABASE_URL = f"sqlite:///{db_dir}/school.db"

# Create engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


class Activity(Base):
    """Activity model"""
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    schedule = Column(String)
    max_participants = Column(Integer)

    # Relationship
    enrollments = relationship("Enrollment", back_populates="activity")


class Enrollment(Base):
    """Enrollment model (student signup for activity)"""
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)
    activity_id = Column(Integer, ForeignKey("activities.id"))
    student_email = Column(String, index=True)

    # Relationship
    activity = relationship("Activity", back_populates="enrollments")


# Create tables
Base.metadata.create_all(bind=engine)


def get_db():
    """Dependency for getting database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
