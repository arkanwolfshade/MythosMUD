"""
/catalog command: paginated text table of item prototypes.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Protocol, cast

from ..alias_storage import AliasStorage
from ..game.item_catalog_service import (
    DEFAULT_PAGE_SIZE,
    CatalogQuery,
    ItemCatalogService,
    normalize_catalog_query,
)
from ..schemas.item_catalog import ItemCatalogAdminItem, ItemCatalogPlayerItem, ItemCatalogResponse
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user
from ..utils.int_coercion import coerce_int

logger = get_logger(__name__)

_FILTER_KEYS = frozenset({"page", "type", "namespace", "search", "page_size"})


class _CatalogPlayer(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Player fields used for admin projection checks."""

    is_admin: bool


class _CatalogPersistence(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Async persistence surface for admin lookup."""

    async def get_player_by_name(self, name: str) -> _CatalogPlayer | None:
        """Look up a player by character name."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Protocol stub body for basedpyright


class _CatalogContainer(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Container fields used by /catalog."""

    async_persistence: _CatalogPersistence | None
    item_catalog_service: ItemCatalogService | None


class _CatalogAppState(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    container: _CatalogContainer | None


class _CatalogApp(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    state: _CatalogAppState


class _CatalogRequest(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    @property
    def app(self) -> _CatalogApp:
        """FastAPI app carrying the DI container."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Protocol stub body for basedpyright


def parse_catalog_args(args: list[object]) -> CatalogQuery:
    """
    Parse /catalog args.

    Supports key=value tokens: page, type, namespace, search, page_size.
    Remaining bare tokens are joined into search (if search not set).
    """
    keyed: dict[str, str] = {}
    bare: list[str] = []
    for raw in args:
        token = str(raw).strip()
        if not token:
            continue
        if "=" in token:
            key, _, value = token.partition("=")
            key_l = key.strip().lower()
            if key_l in _FILTER_KEYS:
                keyed[key_l] = value.strip()
                continue
        bare.append(token)

    search = keyed.get("search")
    if bare and not search:
        search = " ".join(bare)

    return normalize_catalog_query(
        item_type=keyed.get("type"),
        namespace=keyed.get("namespace"),
        search=search,
        page=coerce_int(keyed.get("page"), default=1),
        page_size=coerce_int(keyed.get("page_size"), default=DEFAULT_PAGE_SIZE),
    )


def _truncate(text: str, width: int) -> str:
    if len(text) <= width:
        return text
    if width <= 3:
        return text[:width]
    return text[: width - 3] + "..."


def _format_jsonish(value: object) -> str:
    try:
        return json.dumps(value, separators=(",", ":"), default=str)
    except (TypeError, ValueError):
        return str(value)


def _page_range(total: int, page: int, page_size: int) -> tuple[int, int]:
    if not total:
        return 0, 0
    start = (page - 1) * page_size + 1
    end = min(page * page_size, total)
    return start, end


def _append_admin_rows(lines: list[str], items: list[ItemCatalogAdminItem]) -> None:
    lines.append(f"  {'name':<22} {'type':<12} {'prototype_id':<28} details")
    for item in items:
        details = (
            f"wt={item.weight} val={item.base_value} "
            + f"flags={_format_jsonish(item.flags)} "
            + f"meta={_format_jsonish(item.metadata)}"
        )
        name_col = _truncate(item.name, 22)
        type_col = _truncate(item.item_type, 12)
        id_col = _truncate(item.prototype_id, 28)
        detail_col = _truncate(details, 80)
        lines.append(f"  {name_col:<22} {type_col:<12} {id_col:<28} {detail_col}")


def _append_player_rows(lines: list[str], items: list[ItemCatalogPlayerItem]) -> None:
    lines.append(f"  {'name':<28} {'type':<14} short description")
    for item in items:
        name_col = _truncate(item.name, 28)
        type_col = _truncate(item.item_type, 14)
        desc_col = _truncate(item.short_description, 60)
        lines.append(f"  {name_col:<28} {type_col:<14} {desc_col}")


def _append_catalog_footer(lines: list[str], *, total: int, page: int, page_size: int) -> None:
    lines.append("---")
    max_page = max(1, (total + page_size - 1) // page_size) if total else 1
    if page < max_page:
        lines.append(f"Next page: /catalog page={page + 1}")
    lines.append("Filters: type=<t> namespace=<ns> search=<q> page=<n>")
    lines.append("Open ESC Main Menu > Catalog for the full table UI.")


def format_catalog_output(response: ItemCatalogResponse) -> str:
    """Format catalog page as a text table with showing header and footer hints."""
    total = response.total
    page = response.page
    page_size = response.page_size
    start, end = _page_range(total, page, page_size)
    lines = [
        f"Item catalog: showing {start}-{end} of {total}; refine with filters",
        "---",
    ]
    if not response.items:
        lines.append("  (no prototypes match)")
        _append_catalog_footer(lines, total=total, page=page, page_size=page_size)
        return "\n".join(lines)
    if response.is_admin:
        admin_items = [i for i in response.items if isinstance(i, ItemCatalogAdminItem)]
        _append_admin_rows(lines, admin_items)
    else:
        player_items = [i for i in response.items if isinstance(i, ItemCatalogPlayerItem)]
        _append_player_rows(lines, player_items)
    _append_catalog_footer(lines, total=total, page=page, page_size=page_size)
    return "\n".join(lines)


def _as_catalog_request(request: object) -> _CatalogRequest | None:
    if request is None:
        return None
    return cast(_CatalogRequest, request)


def _get_catalog_service(request: object) -> ItemCatalogService:
    catalog_request = _as_catalog_request(request)
    if catalog_request is None:
        return ItemCatalogService()
    container = catalog_request.app.state.container
    if container is None:
        return ItemCatalogService()
    # getattr: older containers / partial test doubles may lack the attribute.
    existing = getattr(container, "item_catalog_service", None)
    if isinstance(existing, ItemCatalogService):
        return existing
    return ItemCatalogService()


def _user_flag_true(current_user: object, key: str) -> bool:
    """Read a boolean flag from a dict-shaped user or attribute-bearing object (Player/User)."""
    if isinstance(current_user, Mapping):
        mapping = cast(Mapping[str, object], current_user)
        return bool(mapping.get(key))
    return bool(getattr(current_user, key, False))


async def _resolve_is_admin(
    current_user: object,
    request: object,
    player_name: str,
) -> bool:
    """True when the active character has admin privileges."""
    catalog_request = _as_catalog_request(request)
    if catalog_request is not None:
        container = catalog_request.app.state.container
        persistence = container.async_persistence if container is not None else None
        if persistence is not None:
            try:
                username = get_username_from_user(current_user)
                player = await persistence.get_player_by_name(username)
                if player is not None and bool(player.is_admin):
                    return True
            except Exception as e:  # pylint: disable=broad-except
                logger.warning("Catalog admin check failed", player=player_name, error=str(e))
    return _user_flag_true(current_user, "is_admin") or _user_flag_true(current_user, "is_superuser")


async def handle_catalog_command(
    command_data: dict[str, object],
    current_user: object,
    request: object,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle /catalog: print a paginated prototype table (text only)."""
    raw_args_obj = command_data.get("args", [])
    raw_args: list[object]
    if isinstance(raw_args_obj, list):
        raw_args = cast(list[object], raw_args_obj)
    else:
        raw_args = []
    query = parse_catalog_args(raw_args)
    logger.debug(
        "Processing catalog command",
        player=player_name,
        page=query.page,
        item_type=query.item_type,
        namespace=query.namespace,
    )

    service = _get_catalog_service(request)

    try:
        is_admin = await _resolve_is_admin(current_user, request, player_name)
        response = await service.list_catalog(query, is_admin=is_admin)
        return {"result": format_catalog_output(response)}
    except Exception as e:  # pylint: disable=broad-except
        logger.exception("Catalog command failed", player=player_name, error=str(e))
        return {"result": "Failed to load item catalog."}
