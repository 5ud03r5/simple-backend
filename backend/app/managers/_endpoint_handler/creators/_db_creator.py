import os


class DatabaseModelCreator:
    type_mapping = {"string": "str", "integer": "int"}

    @classmethod
    def adjust_attributes(cls, model_path: str, **attributes):
        assert os.path.exists(model_path), "Specified path does not exist"
        lines = []
        with open(model_path, "r") as file:
            for line in file:
                if "created =" in line:
                    for key, value in attributes.items():
                        number = f"({value[1]})" if len(value) == 2 else ""
                        line = f"{line}\n    {key} = Column({value[0].capitalize()}{number})"
                lines.append(line)

        with open(model_path, "w") as file:
            file.writelines(lines)

        cls.update_creation_model(model_path, **attributes)
        cls.update_api_model(model_path, **attributes)

    @classmethod
    def update_creation_model(cls, model_path: str, **attributes):
        lines = []
        with open(model_path, "r") as file:
            for line in file:
                if "CreationApiModel" in line:
                    for key, value in attributes.items():
                        line = f"{line}\n    {key}: {cls.type_mapping[value[0]]}"
                if "pass" in line:
                    line = line.replace("pass", "")
                lines.append(line)

        with open(model_path, "w") as file:
            file.writelines(lines)

    @classmethod
    def update_api_model(cls, model_path: str, **attributes):
        lines = []
        with open(model_path, "r") as file:
            for line in file:
                if "DisplayApiModel" in line:
                    for key, value in attributes.items():
                        line = f"{line}\n    {key}: {cls.type_mapping[value[0]]}"
                    line = f"{line}\n"
                if "pass" in line:
                    line = line.replace("pass", "")

                lines.append(line)

        with open(model_path, "w") as file:
            file.writelines(lines)

    @staticmethod
    def update_ext_db():
        # ext_db file to be updated with this structure:
        # from app.managers import new_manager
        # new_manager.models.Base.metadata.create_all(bind=engine)
        pass
