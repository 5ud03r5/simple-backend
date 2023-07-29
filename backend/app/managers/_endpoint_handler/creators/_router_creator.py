import os
from ._creator import Creator
import importlib

_template_router_file = "template_router.py"
_router_path = os.path.abspath("app/routers")
_ext_routers = os.path.abspath("app/ext_routers.py")


class RouterCreator(Creator):
    def __init__(self, router_name: str = None):
        self.router_name = router_name
        self.router_path = _router_path

    def create_router(self):
        router_file = self.file_creator(
            self.router_path,
            _template_router_file,
            os.path.join(self.router_path, self.router_name + ".py"),
        )
        self.replace_word_in_file(self.router_name, router_file)
        self.add_router_to_app()

    def add_router_to_app(self):
        router_to_add = [
            self.router_name + ".router"
        ]  # Convert the single string to a list

        try:
            with open(_ext_routers, "r") as file:
                existing_content = file.read()
        except FileNotFoundError:
            existing_content = ""

        # Check if the router list is already defined in the file
        router_defined = "routers =" in existing_content

        # Append new routers to the router list
        if router_defined:
            # Find the position of the closing square bracket ']' in the existing content
            end_of_router_list = existing_content.find(
                "]", existing_content.find("routers = [")
            )
            # Generate the new content with added routers
            imported_module = importlib.import_module("app.ext_routers")
            routers = imported_module.routers
            if len(routers) == 0:
                new_content = (
                    existing_content[:end_of_router_list]
                    + ", ".join(router_to_add)
                    + existing_content[end_of_router_list:]
                )

            else:
                new_content = (
                    existing_content[:end_of_router_list]
                    + ", "
                    + ", ".join(router_to_add)
                    + existing_content[end_of_router_list:]
                )
        else:
            # If the router list is not defined, add it along with the new routers
            new_content = existing_content + f"\nrouters = {router_to_add}"

        # Write the modified content back to the file
        with open(_ext_routers, "w") as file:
            file.write("from app.routers import " + self.router_name + "\n")
            file.write(new_content)
