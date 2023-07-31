import os
from app.managers._endpoint_handler.creators._router_creator import (
    _ext_routers,
    _router_path,
)
from app.managers._endpoint_handler.creators._manager_creator import _managers_path
import shutil


class Deleter:
    def __init__(self, name: str):
        self.router_path = os.path.join(_router_path, f"{name}.py")
        self.manager_path = os.path.join(_managers_path, name)

    def begin_deletion_process(self):
        self.delete_endpoint_structure(self.manager_exist(), self.router_exist())

    def router_exist(self) -> str:
        assert os.path.exists(self.manager_path), "Router with this name does not exist"
        return self.manager_path

    def manager_exist(self) -> str:
        assert os.path.exists(self.router_path), "Manager with this name does not exist"
        return self.router_path

    def delete_endpoint_structure(self, *paths: str):
        for path in paths:
            try:
                os.remove(path)
            except IsADirectoryError:
                shutil.rmtree(path, ignore_errors=True)

    @staticmethod
    def exclude_from_ext_routers(*names: str):
        lines = []
        with open(_ext_routers, "r") as file:
            for line in file:
                delete_blank = False
                for name in names:
                    if f"from app.routers import {name}" in line:
                        line = line.replace(f"from app.routers import {name}", "")
                        delete_blank = True
                    elif "routers =" in line:
                        line = line.replace(f", {name}.router", "")
                    elif f", {name}" in line:
                        line = line.replace(f", {name}", "")
                if delete_blank:
                    continue
                lines.append(line)

        with open(_ext_routers, "w") as file:
            file.writelines(lines)
