import uuid

from datetime import datetime
from unittest.mock import Mock

from app.managers import example
from app.managers.example import Example
from app.utils.responses import DeleteResponse

example_item = Example(
    id=uuid.uuid4(),
    description="Test Description",
    name="Test Name",
    created=datetime.now(),
)


def test_create_entry_example(client, monkeypatch):
    _example_response = {
        "id": str(example_item.id),
        "description": example_item.description,
        "name": example_item.name,
        "created": example_item.created.isoformat(),
    }
    create_entry_example = Mock(return_value=_example_response)
    monkeypatch.setattr(example, "create_entry_example", create_entry_example)

    response = client.post(
        "/example/:createEntry",
        json={"name": "Test Example", "description": "Test Description"},
    )

    assert response.status_code == 200
    assert response.json() == _example_response


def test_get_example_item(client, monkeypatch):
    _example_response = {
        "id": str(example_item.id),
        "description": example_item.description,
        "name": example_item.name,
        "created": example_item.created.isoformat(),
    }
    get_example_item = Mock(return_value=_example_response)
    monkeypatch.setattr(example, "get_example_item", get_example_item)

    response = client.get(
        f"/example/{str(example_item.id)}",
    )

    assert response.status_code == 200
    assert response.json() == _example_response


def test_query_examples(client, monkeypatch):
    _example_response = {
        "id": str(example_item.id),
        "description": example_item.description,
        "name": example_item.name,
        "created": example_item.created.isoformat(),
    }
    query_examples = Mock(return_value=[_example_response])
    monkeypatch.setattr(example, "query_examples", query_examples)

    response = client.get(
        "/example",
    )

    assert response.status_code == 200
    assert response.json() == [_example_response]


def test_delete_entry_example(client, monkeypatch):
    delete_entry_example = Mock(return_value=DeleteResponse())
    monkeypatch.setattr(example, "delete_entry_example", delete_entry_example)

    response = client.delete(
        f"/example/:deleteEntry?example_id={str(example_item.id)}",
    )
    assert response.status_code == 204
