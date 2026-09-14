"""
Item catalog API: GET /v1/api/item-catalog
"""

from typing import Annotated

from fastapi import APIRouter, Depends, Query, Request

from ..auth.users import get_current_user
from ..dependencies import get_item_catalog_service
from ..error_types import ErrorMessages
from ..exceptions import LoggedHTTPException
from ..game.item_catalog_service import ItemCatalogService, normalize_catalog_query
from ..models.user import User
from ..schemas.item_catalog import ItemCatalogResponse
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

item_catalog_router = APIRouter(prefix="/api/item-catalog", tags=["item-catalog"])


def _user_is_admin(user: User) -> bool:
    return bool(getattr(user, "is_admin", False) or getattr(user, "is_superuser", False))


@item_catalog_router.get("/", response_model=ItemCatalogResponse)
async def get_item_catalog(
    _request: Request,
    current_user: Annotated[User, Depends(get_current_user)],
    catalog_service: Annotated[ItemCatalogService, Depends(get_item_catalog_service)],
    item_type: Annotated[str | None, Query(alias="type")] = None,
    namespace: Annotated[str | None, Query()] = None,
    search: Annotated[str | None, Query()] = None,
    page: Annotated[int, Query(ge=1)] = 1,
    page_size: Annotated[int, Query(ge=1, le=100)] = 25,
) -> ItemCatalogResponse:
    """Return a paginated item prototype catalog with role-based columns."""
    is_admin = _user_is_admin(current_user)
    query = normalize_catalog_query(
        item_type=item_type,
        namespace=namespace,
        search=search,
        page=page,
        page_size=page_size,
    )
    try:
        return await catalog_service.list_catalog(query, is_admin=is_admin)
    except Exception as e:  # pylint: disable=broad-exception-caught
        logger.error("Error retrieving item catalog", error=str(e))
        raise LoggedHTTPException(
            status_code=500,
            detail=ErrorMessages.INTERNAL_ERROR,
            user_id=str(current_user.id),
            operation="get_item_catalog",
        ) from e
