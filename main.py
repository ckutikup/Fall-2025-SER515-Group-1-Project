from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas

# Create database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Requirements Engineering Tool Prototype")

# Dependency to get a new DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/stories")
def get_stories(db: Session = Depends(get_db)):
    stories = db.query(models.UserStory).all()
    return stories

@app.post("/stories")
def add_story(request: schemas.StoryCreate, db: Session = Depends(get_db)):
    new_story = models.UserStory(
        Title=request.Title,
        Description=request.Description,
        Assignee=request.Assignee,
        Status=request.Status
    )
    db.add(new_story)
    db.commit()
    db.refresh(new_story)
    return {"message": "Story added successfully", "story": new_story}