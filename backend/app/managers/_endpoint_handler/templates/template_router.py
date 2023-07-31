from fastapi import APIRouter
import uuid
from app.managers._endpoint_handler.templates import template_models
from app.managers._endpoint_handler.templates import template_core
from app.utils.responses import EmptyResponse
from typing import List

router = APIRouter(prefix="/template", tags=["template"])


@router.get(
    "",
    description="query_template",
    response_model=List[template_models.TemplateApiModel],
)
def query_template():
    return template_core.query_templates()


@router.get("/{template_id}", response_model=template_models.TemplateApiModel)
def get_template_item(template_id: uuid.UUID):
    return template_core.get_item_template(template_id)


@router.post(
    "",
    response_model=template_models.TemplateApiModel,
)
def create_entry_template(template: template_models.TemplateCreationApiModel):
    return template_core.create_entry_template(template)


@router.delete(
    "/",
    response_class=EmptyResponse,
)
def delete_entry_template(template_id: uuid.UUID):
    return template_core.delete_entry_template(template_id)
