from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas


models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Requirements Engineering Tool Prototype")


origins = [
    "http://localhost:5173",  # adjust this if your frontend runs elsewhere
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # allows GET, POST, etc.
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/stories")
def get_stories(db: Session = Depends(get_db)):
    stories = db.query(models.UserStory).all()
    formatted_stories = [
        {
            "id": story.id,
            "title": story.Title,
            "description": story.Description,
            "assignee": story.Assignee,
            "status": story.Status,
            "createdOn": story.CreatedOn.isoformat() # .isoformat() is good practice for datetimes
        }
        for story in stories
    ]

    # 3. Return the newly formatted list
    return formatted_stories


@app.post("/stories")
def add_story(request: schemas.StoryCreate, db: Session = Depends(get_db)):
    new_story = models.UserStory(
        Title=request.title,
        Description=request.description,
        Assignee=request.assignee,
        Status=request.status
    )
    db.add(new_story)
    db.commit()
    db.refresh(new_story)
    return {
        "message": "Story added successfully",
    }