import os
import fileinput
import sys


class Creator:
    def file_creator(self, path: str, source_file: str, destination_file: str):
        source_file = os.path.join(
            os.path.abspath("app/managers/_endpoint_handler/templates"), source_file
        )
        with open(source_file, "r", encoding="utf-8") as source:
            content = source.read()
        destination_file_path = os.path.join(path, destination_file)

        with open(destination_file_path, "w", encoding="utf-8") as destination:
            destination.write(content)

        return destination_file_path

    def dirs_creation(self, path: str):
        os.mkdir(path)

    def replace_word_in_file(
        self,
        name: str,
        *file_paths: str,
    ):
        for file_path in file_paths:
            with fileinput.FileInput(file_path, inplace=True) as file:
                for line in file:
                    new_line = line.replace("_endpoint_handler.templates", name)
                    new_line = new_line.replace("template_id", name + "_id")
                    new_line = new_line.replace("template_item", name + "_item")
                    new_line = new_line.replace("template_", "")
                    new_line = new_line.replace("Template", name.capitalize())
                    new_line = new_line.replace("template", name)
                    new_line = new_line.replace("_endpoint_handler", name)
                    # Write the modified line to the file
                    sys.stdout.write(new_line)
