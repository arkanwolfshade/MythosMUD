"""
Item catalog service: filtered listing with player/admin column projection.
"""

from __future__ import annotations

from dataclasses import dataclass

from server.persistence.repositories.item_catalog_repository import (
    ItemCatalogPage,
    ItemCatalogRepository,
    ItemPrototypeRow,
)
from server.schemas.item_catalog import ItemCatalogAdminItem, ItemCatalogPlayerItem, ItemCatalogResponse

DEFAULT_PAGE_SIZE = 25
MAX_PAGE_SIZE = 100


@dataclass(frozen=True, slots=True)
class CatalogQuery:
    """Normalized catalog list query."""

    item_type: str | None
    namespace: str | None
    search: str | None
    page: int
    page_size: int


def normalize_catalog_query(
    *,
    item_type: str | None = None,
    namespace: str | None = None,
    search: str | None = None,
    page: int = 1,
    page_size: int = DEFAULT_PAGE_SIZE,
) -> CatalogQuery:
    """Clamp pagination and blank filters to None."""
    safe_page = max(1, page)
    safe_size = min(MAX_PAGE_SIZE, max(1, page_size))
    type_f = item_type.strip() if item_type and item_type.strip() else None
    ns_f = namespace.strip() if namespace and namespace.strip() else None
    search_f = search.strip() if search and search.strip() else None
    return CatalogQuery(
        item_type=type_f,
        namespace=ns_f,
        search=search_f,
        page=safe_page,
        page_size=safe_size,
    )


def project_player_item(row: ItemPrototypeRow) -> ItemCatalogPlayerItem:
    """P1 columns for non-admin viewers."""
    return ItemCatalogPlayerItem(
        name=row.name,
        item_type=row.item_type,
        short_description=row.short_description,
    )


def project_admin_item(row: ItemPrototypeRow) -> ItemCatalogAdminItem:
    """A3 full stored prototype columns for admins."""
    return ItemCatalogAdminItem(
        prototype_id=row.prototype_id,
        name=row.name,
        short_description=row.short_description,
        long_description=row.long_description,
        item_type=row.item_type,
        weight=row.weight,
        base_value=row.base_value,
        durability=row.durability,
        flags=row.flags,
        wear_slots=row.wear_slots,
        stacking_rules=row.stacking_rules,
        usage_restrictions=row.usage_restrictions,
        effect_components=row.effect_components,
        metadata=row.metadata,
        tags=row.tags,
        created_at=row.created_at,
    )


class ItemCatalogService:
    """List item prototypes with role-based projection."""

    _repository: ItemCatalogRepository

    def __init__(self, repository: ItemCatalogRepository | None = None) -> None:
        """Create service with optional repository override for tests."""
        self._repository = repository or ItemCatalogRepository()

    async def list_catalog(self, query: CatalogQuery, *, is_admin: bool) -> ItemCatalogResponse:
        """Fetch one page and project columns for the viewer role."""
        offset = (query.page - 1) * query.page_size
        page_data: ItemCatalogPage = await self._repository.list_page(
            item_type=query.item_type,
            namespace=query.namespace,
            search=query.search,
            limit=query.page_size,
            offset=offset,
        )
        if is_admin:
            items: list[ItemCatalogAdminItem] = [project_admin_item(r) for r in page_data.rows]
            return ItemCatalogResponse(
                items=items,
                page=query.page,
                page_size=query.page_size,
                total=page_data.total,
                is_admin=True,
            )
        player_items: list[ItemCatalogPlayerItem] = [project_player_item(r) for r in page_data.rows]
        return ItemCatalogResponse(
            items=player_items,
            page=query.page,
            page_size=query.page_size,
            total=page_data.total,
            is_admin=False,
        )
