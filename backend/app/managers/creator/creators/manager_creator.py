import os
from typing import Dict
from ._creator import Creator

template_model_file = "template_models.py"
template_core_file = "template_core.py"


class ManagerCreator(Creator):
    def __init__(
        self, manager_name: str = None, manager_class_attributes: Dict[str, str] = None
    ):
        self.manager_name = manager_name
        self.manager_attributes = manager_class_attributes
        self.manager_path = os.path.join(os.path.abspath("../../"), self.manager_name)

    def create_manager(self):
        # Validation needed to check if manager with this name exist
        self.dirs_creation(self.manager_path)
        self.manager_files_creation()

    def delete_manager(self):
        return

    def manager_files_creation(self):
        # Model file creation and copy from template
        self.file_creator(self.manager_path, template_model_file, "model.py")

        # Core file creation and copy from template
        self.file_creator(self.manager_path, template_core_file, "core.py")
        return

    def model_file_changer(self):
        return
