from .creators import RouterCreator, ManagerCreator, DatabaseModelCreator
import os
from typing import Dict
from .deleters import Deleter
from ._util import (
    ensure_string_is_valid_and_return_lower,
    ensure_attributes_are_valid,
)


def create_api_endpoint(name: str, attributes: Dict[str, list]):
    ensure_string_is_valid_and_return_lower(name)
    ensure_attributes_are_valid(attributes)
    new_manager = ManagerCreator(name, attributes)
    new_manager.create_manager()
    new_router = RouterCreator(name)
    new_router.create_router()
    DatabaseModelCreator.adjust_attributes(new_manager.models_file_path, **attributes)


def delete_api_endpoint(name: str):
    Deleter.exclude_from_ext_routers(name)
    endpoint_deletor = Deleter(name)
    endpoint_deletor.begin_deletion_process()


def update_api_endpoint():
    return
