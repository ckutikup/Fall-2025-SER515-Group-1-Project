from sqlalchemy import Column, Integer, String, Text, DateTime, func
from database import Base

class UserStory(Base):
    __tablename__ = "Stories"
    id = Column(Integer, primary_key=True, index=True)
    Title = Column(String(250), nullable=False)
    Description = Column(Text, nullable=False)
    Assignee = Column(String(250), nullable=False, server_default="Unassigned")
    Status = Column(String(250), nullable=False, server_default="In Progress")
    CreatedOn = Column(DateTime(timezone=True), server_default=func.now())