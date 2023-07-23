from fastapi import APIRouter
from app.managers import creator

router = APIRouter(prefix="/creator", tags=["creator"])


@router.post("/:createRouter", description="Creates a router")
def create_router():
    """
    Router creation endpoint. It utilizes method to create router
    file along with all specified endpoints
    """
    pass


@router.delete("/:deleteRouter", description="Deletes the router")
def delete_router():
    """
    Router Deletion endpoint. It utilizes method to delete router file.
    """
    pass
