from pydantic import BaseModel, Field   # ✅ this import is required
from typing import Optional

class StoryCreate(BaseModel):
    title: str = Field(..., description="Title of the story")
    description: str = Field(..., description="Description of the story")
    assignee: Optional[str] = Field(default="Unassigned", description="Person assigned to the story")
    status: Optional[str] = Field(default="In Progress", description="Current status of the story")