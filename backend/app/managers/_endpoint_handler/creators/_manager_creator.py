import os
from typing import Dict
from ._creator import Creator

# Static locations and names, shall not be modified
_template_model_file = "template_models.py"
_template_core_file = "template_core.py"
_init_file = "__init__.py"
_managers_path = os.path.abspath("app/managers")


class ManagerCreator(Creator):
    def __init__(
        self, manager_name: str = None, manager_class_attributes: Dict[str, str] = None
    ):
        self.manager_name = manager_name
        self.manager_attributes = manager_class_attributes
        self.manager_path = os.path.join(_managers_path, self.manager_name)

    def create_manager(self):
        # Validation needed to check if manager with this name exist
        self.dirs_creation(self.manager_path)
        self.replace_word_in_file(self.manager_name, self.manager_files_creation())

    def manager_files_creation(self):
        # Model file creation and copy from template
        model_path = self.file_creator(
            self.manager_path, _template_model_file, "models.py"
        )

        # Core file creation and copy from template
        core_path = self.file_creator(self.manager_path, _template_core_file, "core.py")
        init_path = self.file_creator(self.manager_path, _init_file, _init_file)
        return model_path, core_path, init_path

    def manager_ini_file_create(self, path: str):
        pass
