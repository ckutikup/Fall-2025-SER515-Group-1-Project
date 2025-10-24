from pydantic import BaseModel

class StoryCreate(BaseModel):
    Title: str
    Description: str
    Assignee: str
    Status: str