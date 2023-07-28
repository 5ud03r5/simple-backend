import os
from ._creator import Creator

template_router_file = "template_router.py"


class RouterCreator(Creator):
    def __init__(self, router_name: str = None):
        self.router_name = router_name
        self.router_path = os.path.abspath("../../../routers")

    def create_router_file(self):
        self.file_creator(
            self.router_path,
            template_router_file,
            os.path.join(self.router_path, self.router_name),
        )
