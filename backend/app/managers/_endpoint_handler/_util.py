import re
from typing import Dict, List

# TODO: This needs to be completed
reserved_names: Dict[str, bool] = {
    "string": True,
    "number": True,
    "integer": True,
    "date": True,
    "dict": True,
}

# TODO: This needs to be completed
valid_values: Dict[str, bool] = {
    "string": True,
    "integer": True,
    "uuid": True,
    "datetime": True,
}


def ensure_string_is_valid_and_return_lower(name: str) -> str:
    if not re.match(r"^[A-Za-z]*$", name):
        raise ValueError("Must contain only letters")
    try:
        reserved_names[name.lower()]
        raise ValueError(f"Value {name.lower()} is forbiden")
    except KeyError:
        return name.lower()


def ensure_attributes_are_valid(attributes: Dict[str, list]) -> Dict[str, list]:
    for key, value in attributes.items():
        ensure_string_is_valid_and_return_lower(key)
        assert isinstance(value, list), "Value needs to be a list"
        assert len(value) > 0, "Value cannot be an empty list"
        assert len(value) <= 2, "Value cannot have more than 2 items"
        assert isinstance(
            value[0], str
        ), "First item in passed value needs to be a string type"
        if len(value) == 2:
            assert isinstance(
                value[1], int
            ), "Second item in passed value needs to be a integer type"
        try:
            valid_values[value[0].lower()]
        except KeyError as exc:
            raise ValueError(f"{value[0].lower()} is not a valid type ") from exc

    verified_attributes = {
        key.lower(): [val.lower() if isinstance(val, str) else val for val in value]
        for key, value in attributes.items()
    }

    return verified_attributes
