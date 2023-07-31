import uuid
from app.managers._endpoint_handler.templates import template_models
from app.db.manager import DatabaseClient, QueryResult
from app.utils.responses import EmptyResponse


def create_entry_template(
    template_item: template_models.TemplateApiModel,
) -> template_models.Template:
    return DatabaseClient.post(template_models.Template, template_item)


def get_item_template(template_id: uuid.UUID) -> template_models.Template:
    return DatabaseClient.get(template_models.Template, "id", template_id)


def query_templates() -> QueryResult:
    return DatabaseClient.get_all(template_models.Template)


def delete_entry_template(template_id: uuid.UUID) -> EmptyResponse:
    DatabaseClient.delete(template_models.Template, template_id)
    return EmptyResponse()
