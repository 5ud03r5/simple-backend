from fastapi import APIRouter
from app.managers import _endpoint_handler

router = APIRouter(prefix="/endpoint_handler", tags=["Endpoint handler"])


@router.post("/", description="Creates an api endpoint")
def create_api_endpoint(request: _endpoint_handler.EndpointCreationRequest):
    return _endpoint_handler.create_api_endpoint(request.name, request.attributes)


@router.put("/", description="Updates an api endpoint")
def update_api_endpoint():
    return _endpoint_handler.update_api_endpoint()


@router.delete("/", description="Deletes an api endpoint")
def delete_api_endpoint(endpoint_name: str):
    return _endpoint_handler.delete_api_endpoint(endpoint_name)
