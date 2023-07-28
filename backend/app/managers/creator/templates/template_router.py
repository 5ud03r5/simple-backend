from fastapi import APIRouter
import uuid
from app.managers.creator.templates import template_models
from app.managers.creator.templates import template_core
from app.utils.responses import DeleteResponse
from typing import List

router = APIRouter(prefix="/template", tags=["template"])


@router.get(
    "",
    description="query_template",
    response_model=List[template_models.TemplateApiModel],
)
def query_template():
    return template_core.query_template()


@router.get("/{template_id}", response_model=template_models.TemplateApiModel)
def get_template_item(template_id: uuid.UUID):
    return template_core.get_template_item(template_id)


@router.post(
    "/:createTemplate",
    response_model=template_models.TemplateApiModel,
    description="Example Creation endpoint. It's purpose is to show basic functionalities on predefined db models",
)
def create_entry_template(template: template_models.TemplateCreationApiModel):
    return template_core.create_entry_template(template)


@router.delete(
    "/:deleteEntry",
    response_class=DeleteResponse,
    description="Example Deletion endpoint. It's purpose is to show basic functionalities on predefined db models",
)
def delete_entry_template(template_id: uuid.UUID):
    return template_core.delete_entry_template(template_id)
