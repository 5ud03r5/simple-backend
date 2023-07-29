from fastapi import APIRouter
import uuid
from app.managers import example
from typing import List

router = APIRouter(prefix="/example", tags=["Example"])


@router.get(
    "",
    description="API call to retrieve example information about all of the functionalities for this router",
    response_model=List[example.ExampleApiModel],
)
def query_examples():
    return example.query_examples()


@router.get("/{example_id}", response_model=example.ExampleApiModel)
def get_example_item(example_id: uuid.UUID):
    return example.get_example_item(example_id)


@router.post(
    "/:createEntry",
    response_model=example.ExampleApiModel,
    description="Example Creation endpoint. It's purpose is to show basic functionalities on predefined db models",
)
def create_entry_example(example_item: example.ExampleCreationApiModel):
    return example.create_entry_example(example_item)


@router.delete(
    "/:deleteEntry",
    status_code=204,
    description="Example Deletion endpoint. It's purpose is to show basic functionalities on predefined db models",
)
def delete_entry_example(example_id: uuid.UUID):
    return example.delete_entry_example(example_id)
