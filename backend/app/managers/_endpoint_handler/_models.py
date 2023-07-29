from pydantic import BaseModel
from typing import Dict


class EndpointCreationRequest(BaseModel):
    name: str
    attributes: Dict[str, list]
