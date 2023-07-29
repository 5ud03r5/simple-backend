import os
from ._creator import Creator

_template_router_file = "template_router.py"
_router_path = os.path.abspath("app/routers")


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
