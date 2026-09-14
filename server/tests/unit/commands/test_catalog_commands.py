"""Unit tests for /catalog command helpers and handler."""

from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands import catalog_commands as cmd
from server.game.item_catalog_service import ItemCatalogService
from server.schemas.item_catalog import ItemCatalogAdminItem, ItemCatalogPlayerItem, ItemCatalogResponse


def _player_response(**overrides: object) -> ItemCatalogResponse:
    base = ItemCatalogResponse(
        items=[ItemCatalogPlayerItem(name="Knife", item_type="weapon", short_description="A blade")],
        page=1,
        page_size=25,
        total=1,
        is_admin=False,
    )
    return base.model_copy(update=overrides) if overrides else base


def test_parse_catalog_args_defaults() -> None:
    query = cmd.parse_catalog_args([])
    assert query.page == 1
    assert query.page_size == 25
    assert query.item_type is None
    assert query.namespace is None
    assert query.search is None


def test_parse_catalog_args_filters_and_bare_search() -> None:
    query = cmd.parse_catalog_args(["type=weapon", "namespace=core", "page=2", "silver", "knife"])
    assert query.item_type == "weapon"
    assert query.namespace == "core"
    assert query.page == 2
    assert query.search == "silver knife"


def test_parse_catalog_args_explicit_search_wins_over_bare() -> None:
    query = cmd.parse_catalog_args(["search=lantern", "ignored", "tokens"])
    assert query.search == "lantern"


def test_parse_catalog_args_invalid_page_and_page_size() -> None:
    query = cmd.parse_catalog_args(["page=nope", "page_size=xyz"])
    assert query.page == 1
    assert query.page_size == 25


def test_parse_catalog_args_skips_blank_unknown_keys_become_bare_search() -> None:
    query = cmd.parse_catalog_args(["", "  ", "foo=bar", "type=tome"])
    assert query.item_type == "tome"
    # Unknown key=value tokens are treated as bare search tokens.
    assert query.search == "foo=bar"


def test_format_catalog_output_player() -> None:
    text = cmd.format_catalog_output(
        _player_response(
            items=[
                ItemCatalogPlayerItem(
                    name="A" * 40,
                    item_type="weapon",
                    short_description="B" * 80,
                )
            ]
        )
    )
    assert "showing 1-1 of 1" in text
    assert "..." in text
    assert "Filters: type=" in text


def test_format_catalog_output_empty() -> None:
    text = cmd.format_catalog_output(ItemCatalogResponse(items=[], page=1, page_size=25, total=0, is_admin=False))
    assert "showing 0-0 of 0" in text
    assert "(no prototypes match)" in text


def test_format_catalog_output_next_page_hint() -> None:
    text = cmd.format_catalog_output(
        ItemCatalogResponse(
            items=[ItemCatalogPlayerItem(name="A", item_type="tool", short_description="x")],
            page=1,
            page_size=25,
            total=40,
            is_admin=False,
        )
    )
    assert "Next page: /catalog page=2" in text


def test_format_catalog_output_admin_includes_prototype_id() -> None:
    response = ItemCatalogResponse(
        items=[
            ItemCatalogAdminItem(
                prototype_id="core.weapon.knife",
                name="Knife",
                short_description="A blade",
                long_description="Long",
                item_type="weapon",
                weight=0.5,
                base_value=10,
                durability=None,
                flags=["sharp"],
                wear_slots=[],
                stacking_rules={},
                usage_restrictions={},
                effect_components=[],
                metadata={"namespace": "core"},
                tags=[],
                created_at=datetime.now(UTC),
            )
        ],
        page=1,
        page_size=25,
        total=1,
        is_admin=True,
    )
    text = cmd.format_catalog_output(response)
    assert "core.weapon.knife" in text
    assert "wt=0.5" in text
    assert '"sharp"' in text
    assert '"namespace":"core"' in text


class _CatalogContainerStub:
    def __init__(
        self,
        *,
        persistence: object | None = None,
        catalog_service: ItemCatalogService | None = None,
    ) -> None:
        self.async_persistence: object | None = persistence
        self.item_catalog_service: ItemCatalogService | None = catalog_service


class _CatalogAppStateStub:
    def __init__(self, container: _CatalogContainerStub) -> None:
        self.container: _CatalogContainerStub = container


class _CatalogAppStub:
    def __init__(self, state: _CatalogAppStateStub) -> None:
        self.state: _CatalogAppStateStub = state


class _CatalogRequestStub:
    def __init__(self, app: _CatalogAppStub) -> None:
        self.app: _CatalogAppStub = app


def _request_with(
    *,
    persistence: object | None = None,
    catalog_service: ItemCatalogService | None = None,
) -> _CatalogRequestStub:
    container = _CatalogContainerStub(persistence=persistence, catalog_service=catalog_service)
    return _CatalogRequestStub(_CatalogAppStub(_CatalogAppStateStub(container)))


@pytest.mark.asyncio
async def test_handle_catalog_command_admin_from_player() -> None:
    persistence = MagicMock()
    persistence.get_player_by_name = AsyncMock(return_value=MagicMock(is_admin=True))
    service = ItemCatalogService(repository=MagicMock())
    list_catalog: AsyncMock = AsyncMock(return_value=_player_response())
    request = _request_with(persistence=persistence, catalog_service=service)

    with patch.object(service, "list_catalog", list_catalog):
        with patch("server.commands.catalog_commands.get_username_from_user", return_value="Alice"):
            result = await cmd.handle_catalog_command(
                {"args": []},
                {"id": "u1"},
                request,
                None,
                "Alice",
            )

    assert "Knife" in result["result"]
    assert list_catalog.await_args is not None
    assert list_catalog.await_args.kwargs["is_admin"] is True


@pytest.mark.asyncio
async def test_handle_catalog_command_admin_from_user_flags() -> None:
    list_catalog: AsyncMock = AsyncMock(return_value=_player_response())

    with patch.object(ItemCatalogService, "list_catalog", list_catalog):
        result = await cmd.handle_catalog_command(
            {},
            {"is_superuser": True},
            None,
            None,
            "Alice",
        )

    assert "Knife" in result["result"]
    assert list_catalog.await_args is not None
    assert list_catalog.await_args.kwargs["is_admin"] is True


@pytest.mark.asyncio
async def test_handle_catalog_command_success() -> None:
    service = ItemCatalogService(repository=MagicMock())
    list_catalog: AsyncMock = AsyncMock(
        return_value=_player_response(
            items=[ItemCatalogPlayerItem(name="Lantern", item_type="tool", short_description="Light")]
        )
    )
    request = _request_with(catalog_service=service)

    with patch.object(service, "list_catalog", list_catalog):
        result = await cmd.handle_catalog_command(
            {"args": ["type=tool"]},
            {"id": "user-1"},
            request,
            None,
            "Alice",
        )
    assert "Lantern" in result["result"]
    assert "showing 1-1 of 1" in result["result"]
    assert list_catalog.await_args is not None
    assert list_catalog.await_args.kwargs["is_admin"] is False


@pytest.mark.asyncio
async def test_handle_catalog_command_failure() -> None:
    list_catalog: AsyncMock = AsyncMock(side_effect=RuntimeError("boom"))
    with patch.object(ItemCatalogService, "list_catalog", list_catalog):
        result = await cmd.handle_catalog_command({}, {"id": "user-1"}, None, None, "Alice")
    assert result["result"] == "Failed to load item catalog."
