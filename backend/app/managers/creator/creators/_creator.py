import os


class Creator:
    def file_creator(self, path: str, source_file: str, destination_file: str):
        with open(source_file, "r", encoding="utf-8") as source:
            content = source.read()

        with open(
            os.path.join(path, destination_file), "w", encoding="utf-8"
        ) as destination:
            destination.write(content)

    def dirs_creation(self, path: str):
        os.mkdir(path)
        return
