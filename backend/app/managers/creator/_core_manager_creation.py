import os
from typing import Dict

template_model_file = "template_models.py"
template_core_file = "template_core.py"


class ManagerCreator:
    def __init__(
        self, manager_name: str = None, manager_class_attributes: Dict[str, str] = None
    ):
        self.manager_name = manager_name
        self.manager_attributes = manager_class_attributes
        self.manager_path = os.path.join(os.path.abspath("../"), self.manager_name)
        self.router_path = os.path.abspath("../../routers")

    def create_manager(self):
        # Validation needed to check if manager with this name exist
        self._dirs_creation()
        self._manager_files_creation()
        self._router_file_creation()
        return

    def delete_manager(self):
        return

    def _dirs_creation(self):
        # Manager dir creation
        os.mkdir(self.manager_path)
        return

    def _manager_files_creation(self):
        # Model file creation and copy from template
        self._file_creator(self.manager_path, template_model_file, "model.py")

        # Core file creation and copy from template
        self._file_creator(self.manager_path, template_core_file, "core.py")
        return

    def _file_creator(self, path: str, source_file: str, destination_file: str):
        with open(source_file, "r", encoding="utf-8") as source:
            content = source.read()

        with open(
            os.path.join(path, destination_file), "w", encoding="utf-8"
        ) as destination:
            destination.write(content)

    def _model_file_changer(self):
        return

    def _router_file_creation(self):
        return
