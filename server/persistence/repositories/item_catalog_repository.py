"""
Repository for paginated item_prototypes catalog listing.
"""

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime
from typing import cast

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from structlog.stdlib import BoundLogger

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)

_LIST_PAGE_SQL = """
SELECT
    prototype_id,
    name,
    short_description,
    long_description,
    item_type,
    weight,
    base_value,
    durability,
    flags,
    wear_slots,
    stacking_rules,
    usage_restrictions,
    effect_components,
    metadata,
    tags,
    created_at,
    total_count
FROM list_item_prototypes_page(
    :item_type,
    :namespace,
    :search,
    :limit,
    :offset
)
"""


@dataclass(frozen=True, slots=True)
class ItemPrototypeRow:
    """One item_prototypes row from list_item_prototypes_page."""

    prototype_id: str
    name: str
    short_description: str
    long_description: str
    item_type: str
    weight: float
    base_value: int
    durability: int | None
    flags: list[object]
    wear_slots: list[object]
    stacking_rules: dict[str, object]
    usage_restrictions: dict[str, object]
    effect_components: list[object]
    metadata: dict[str, object]
    tags: list[object]
    created_at: datetime | None


@dataclass(frozen=True, slots=True)
class ItemCatalogPage:
    """Paginated prototype list with total matching filter count."""

    rows: list[ItemPrototypeRow]
    total: int


def _as_object_list(value: object) -> list[object]:
    if isinstance(value, list):
        return cast(list[object], value)
    return []


def _as_object_dict(value: object) -> dict[str, object]:
    if isinstance(value, dict):
        return cast(dict[str, object], value)
    return {}


def _coerce_int(value: object) -> int:
    if isinstance(value, bool):
        raise TypeError("boolean is not a valid total_count")
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if isinstance(value, str):
        return int(value)
    raise TypeError(f"unsupported total_count type: {type(value)!r}")


def _row_to_prototype(row: Mapping[str, object]) -> ItemPrototypeRow:
    durability_raw = row.get("durability")
    durability = int(durability_raw) if isinstance(durability_raw, int) else None
    created_raw = row.get("created_at")
    created_at = created_raw if isinstance(created_raw, datetime) else None
    return ItemPrototypeRow(
        prototype_id=str(row["prototype_id"]),
        name=str(row["name"]),
        short_description=str(row["short_description"]),
        long_description=str(row["long_description"]),
        item_type=str(row["item_type"]),
        weight=float(cast(float | int, row["weight"])),
        base_value=int(cast(int, row["base_value"])),
        durability=durability,
        flags=_as_object_list(row.get("flags")),
        wear_slots=_as_object_list(row.get("wear_slots")),
        stacking_rules=_as_object_dict(row.get("stacking_rules")),
        usage_restrictions=_as_object_dict(row.get("usage_restrictions")),
        effect_components=_as_object_list(row.get("effect_components")),
        metadata=_as_object_dict(row.get("metadata")),
        tags=_as_object_list(row.get("tags")),
        created_at=created_at,
    )


def _mappings_to_page(rows: list[Mapping[str, object]]) -> ItemCatalogPage:
    if not rows:
        return ItemCatalogPage(rows=[], total=0)
    total = _coerce_int(rows[0]["total_count"])
    prototypes = [_row_to_prototype(row) for row in rows]
    return ItemCatalogPage(rows=prototypes, total=total)


class ItemCatalogRepository:
    """Persistence for item catalog listing via list_item_prototypes_page()."""

    _logger: BoundLogger

    def __init__(self) -> None:
        """Initialize the item catalog repository."""
        self._logger = get_logger(__name__)

    async def list_page(
        self,
        *,
        item_type: str | None,
        namespace: str | None,
        search: str | None,
        limit: int,
        offset: int,
    ) -> ItemCatalogPage:
        """Return a filtered page of item prototypes."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text(_LIST_PAGE_SQL),
                    {
                        "item_type": item_type,
                        "namespace": namespace,
                        "search": search,
                        "limit": limit,
                        "offset": offset,
                    },
                )
                mapped = [cast(Mapping[str, object], dict(r)) for r in result.mappings().all()]
                page = _mappings_to_page(mapped)
                self._logger.debug(
                    "Loaded item catalog page",
                    row_count=len(page.rows),
                    total=page.total,
                    offset=offset,
                )
                return page
        except (SQLAlchemyError, OSError, TypeError, ValueError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error listing item catalog: {e}",
                operation="list_item_prototypes_page",
                details={"error": str(e)},
                user_friendly="Failed to retrieve item catalog",
            )
