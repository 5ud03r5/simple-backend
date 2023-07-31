import os


class DatabaseModelCreator:
    @staticmethod
    def adjust_attributes(model_path: str, **attributes):
        assert os.path.exists(model_path), "Specified path does not exist"
        # adjust attributes for db model in such way:
        # key = Column(value[0](value[1]))

    @staticmethod
    def update_ext_db():
        # ext_db file to be updated with this structure:
        # from app.managers import new_manager
        # new_manager.models.Base.metadata.create_all(bind=engine)
        pass
