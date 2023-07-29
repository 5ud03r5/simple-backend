from .creators import RouterCreator, ManagerCreator
from typing import Dict
from ._util import ensure_string_is_valid_and_return_lower, ensure_attributes_are_valid


def create_api_endpoint(name: str, attributes: Dict[str, list]):
    ensure_string_is_valid_and_return_lower(name)
    ensure_attributes_are_valid(attributes)
    new_manager = ManagerCreator(name, attributes)
    try:
        new_manager.create_manager()
    except Exception as error:
        print(error)
        raise error

    new_router = RouterCreator(name)
    try:
        new_router.create_router()
    except Exception as error:
        print(error)
        raise error

    return


def delete_api_endpoint():
    return


def update_api_endpoint():
    return
