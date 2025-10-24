from sqlalchemy import Column, Integer, String, Text, DateTime, func
from database import Base

class UserStory(Base):
    __tablename__ = "Stories"

    id = Column(Integer, primary_key=True, index=True)
    Title = Column(String(250))
    Description = Column(Text)
    Assignee = Column(String(250))
    Status = Column(String(250))
    CreatedOn = Column(DateTime(timezone=True), server_default=func.now())