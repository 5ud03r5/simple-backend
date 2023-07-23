from fastapi.responses import Response
from typing import Any


class DeleteResponse(Response):
    def __init__(self, status_code: int = 204, content: Any = None):
        super().__init__(status_code=status_code, content=content)
