import os
from app.managers._endpoint_handler.creators._router_creator import (
    _ext_routers,
    _router_path,
)
import importlib
import shutil


class Deleter:
    def __init__(self, name: str):
        self.router_path = os.path.join(_router_path, f"{name}.py")
        self.manager_path = os.path.join(_managers_path, name)

    def begin_deletion_process(self):
        self.delete_files(self.router_exist(), self.manager_exist)

    def router_exist(self) -> str:
        assert os.path.exists(self.manager_path), "Router with this name does not exist"
        return self.manager_path

    def manager_exist(self) -> str:
        assert os.path.exists(self.router_path), "Manager with this name does not exist"
        return self.router_path

    def delete_files(self, *paths: str):
        for path in paths:
            try:
                os.remove(path)
            except IsADirectoryError:
                shutil.rmtree(path, ignore_errors=True)

    @staticmethod
    def exclude_from_ext_routers(*names: str):
        # This is to be done
        pass
