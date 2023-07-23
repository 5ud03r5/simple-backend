import uuid
from .models import Example, ExampleApiModel
from app.db.manager import DatabaseClient, QueryResult
from app.utils.responses import DeleteResponse


def create_entry_example(example_item: ExampleApiModel) -> Example:
    return DatabaseClient.post(Example, example_item)


def query_examples() -> QueryResult:
    return DatabaseClient.get_all(Example)


def get_example_item(example_id: uuid.UUID) -> Example:
    return DatabaseClient.get(Example, "id", example_id)


def delete_entry_example(example_id: uuid.UUID) -> DeleteResponse:
    DatabaseClient.delete(Example, example_id)
    return DeleteResponse()
