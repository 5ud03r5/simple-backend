import uuid
from datetime import datetime
from pydantic import BaseModel
from app.db.database import Base
from sqlalchemy import Column, String, BINARY, DateTime


class Example(Base):
    __tablename__ = "example"
    id = Column(
        String(36),
        primary_key=True,
        index=True,
        default=lambda: str(uuid.uuid4()),
    )
    description = Column(String(255))
    name = Column(String(100))
    created = Column(DateTime, default=datetime.now)


class ExampleCreationApiModel(BaseModel):
    description: str
    name: str


class ExampleApiModel(BaseModel):
    id: uuid.UUID
    description: str
    name: str
    created: datetime
