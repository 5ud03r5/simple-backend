import uuid
from datetime import datetime
from pydantic import BaseModel
from app.db.database import Base
from sqlalchemy import Column, String, DateTime


class Template(Base):
    __tablename__ = "template"
    id = Column(
        String(36),
        primary_key=True,
        index=True,
        default=lambda: str(uuid.uuid4()),
    )
    created = Column(DateTime, default=datetime.now)


class TemplateCreationApiModel(BaseModel):
    pass


class TemplateApiModel(BaseModel):
    id: uuid.UUID
    created: datetime
