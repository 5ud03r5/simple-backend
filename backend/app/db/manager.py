import uuid
from app.db.database import Base
from app.db.database import get_db
from sqlalchemy.orm import Query
from app.utils.errors import NotFoundError


class DatabaseClient:
    """
    Utility database interaction class
    """

    @staticmethod
    def get_all(model: Base):
        with get_db() as db:
            return db.query(model).all()

    @staticmethod
    def get(model_class: Base, query_by: str, value: str | uuid.UUID):
        if not hasattr(model_class, query_by):
            raise ValueError(f"{query_by} is not a valid class {model_class} attribute")

        attr = getattr(model_class, query_by)
        with get_db() as db:
            return db.query(model_class).filter(attr == str(value)).first()

    @staticmethod
    def post(model_class: Base, creation_item):
        creation_item = dict(creation_item)
        prepared_model = model_class(**creation_item)
        with get_db() as db:
            db.add(prepared_model)
            db.commit()
            db.refresh(prepared_model)
            return prepared_model

    @staticmethod
    def delete(model_class: Base, item_id: uuid.UUID):
        if not hasattr(model_class, "id"):
            raise ValueError(f"id is not a valid class {model_class} attribute")

        attr = getattr(model_class, "id")
        with get_db() as db:
            item = db.query(model_class).filter(attr == str(item_id)).first()
            if item is None:
                raise NotFoundError("Object not found")
            db.delete(item)
            db.commit()


class QueryResult(Query):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
