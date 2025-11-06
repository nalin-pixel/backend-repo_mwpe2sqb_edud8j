"""
Database Schemas for Cybersecurity LMS

Each Pydantic model represents a MongoDB collection. The collection name is the
lowercase of the class name (e.g., Course -> "course").
"""
from pydantic import BaseModel, Field
from typing import Optional, List

class Course(BaseModel):
    title: str = Field(..., description="Course title")
    description: str = Field(..., description="What this course covers")
    level: str = Field(..., description="Beginner, Intermediate, Advanced")
    category: str = Field(..., description="Category such as Network, Web, Forensics")
    thumbnail: Optional[str] = Field(None, description="Optional image URL")

class Lesson(BaseModel):
    course_id: str = Field(..., description="ID of the parent course")
    title: str = Field(..., description="Lesson title")
    content: str = Field(..., description="Lesson content in markdown/plain text")
    order: int = Field(..., description="Lesson order index within the course")

class Enrollment(BaseModel):
    course_id: str = Field(..., description="Course being enrolled in")
    email: str = Field(..., description="Learner email")
    name: str = Field(..., description="Learner name")

class Progress(BaseModel):
    email: str = Field(..., description="Learner email")
    course_id: str = Field(..., description="Associated course")
    lesson_id: str = Field(..., description="Lesson being tracked")
    status: str = Field("in_progress", description="in_progress or completed")

class Quiz(BaseModel):
    lesson_id: str = Field(..., description="Linked lesson")
    question: str = Field(..., description="Multiple choice question")
    options: List[str] = Field(..., description="Answer options")
    correct_option: int = Field(..., ge=0, description="Index of the correct option")

class Submission(BaseModel):
    email: str = Field(..., description="Learner email")
    quiz_id: str = Field(..., description="Quiz identifier")
    selected_option: int = Field(..., ge=0, description="Selected option index")
    score: int = Field(..., ge=0, le=1, description="1 if correct else 0")
