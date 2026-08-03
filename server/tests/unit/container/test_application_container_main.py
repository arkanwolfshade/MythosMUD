"""Gap coverage for ApplicationContainer main module accessors."""

from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.container.main import ApplicationContainer, _flatten_bundle, get_container, reset_container


def test_flatten_bundle_copies_existing_attrs() -> None:
    container = SimpleNamespace()
    bundle = SimpleNamespace(a=1, b=2)
    _flatten_bundle(container, bundle, ("a", "missing", "b"))  # type: ignore[arg-type]
    assert container.a == 1
    assert container.b == 2
    assert not hasattr(container, "missing")


def test_get_service_not_initialized() -> None:
    c = ApplicationContainer()
    with pytest.raises(RuntimeError, match="not initialized"):
        c.get_service("player_service")


def test_get_service_unknown_and_none() -> None:
    c = ApplicationContainer()
    c._initialized = True
    with pytest.raises(ValueError, match="Unknown service"):
        c.get_service("not_a_real_service_xyz")
    c.player_service = None
    with pytest.raises(ValueError, match="not initialized"):
        c.get_service("player_service")
    c.player_service = object()
    assert c.get_service("player_service") is c.player_service


def test_is_initialized_property() -> None:
    c = ApplicationContainer()
    assert c.is_initialized is False
    c._initialized = True
    assert c.is_initialized is True


def test_get_project_root_caches() -> None:
    c = ApplicationContainer()
    root = Path("C:/projects/MythosMUD")
    with patch("server.container.main.get_project_root", return_value=root) as mock_root:
        assert c._get_project_root() == root
        assert c._get_project_root() == root
        mock_root.assert_called_once()


def test_decode_and_normalize_delegates() -> None:
    c = ApplicationContainer()
    with patch("server.container.main.decode_json_column", return_value={"ok": True}) as dec:
        assert c._decode_json_column('{"ok":true}', dict) == {"ok": True}
        dec.assert_called_once()
    with patch("server.container.main.normalize_path_from_url_or_path", return_value=Path("x")) as norm:
        assert c._normalize_path_from_url_or_path("/tmp", Path(".")) == Path("x")
        norm.assert_called_once()


def test_get_and_reset_container_helpers() -> None:
    ApplicationContainer.reset_instance()
    first = get_container()
    assert isinstance(first, ApplicationContainer)
    reset_container()
    assert ApplicationContainer._instance is None


@pytest.mark.asyncio
async def test_initialize_skips_when_already_initialized() -> None:
    c = ApplicationContainer()
    c._initialized = True
    await c.initialize()


@pytest.mark.asyncio
async def test_shutdown_calls_bundles() -> None:
    c = ApplicationContainer()
    c.log_aggregator = MagicMock()
    c.nats_message_handler = MagicMock()
    c.nats_service = MagicMock()
    c.event_bus = MagicMock()
    c.database_manager = MagicMock()
    c.async_persistence = MagicMock()

    with (
        patch("server.container.bundles.MonitoringBundle") as mon_cls,
        patch("server.container.bundles.RealtimeBundle") as rt_cls,
        patch("server.container.bundles.CoreBundle") as core_cls,
    ):
        mon = MagicMock()
        mon.shutdown = AsyncMock()
        mon_cls.return_value = mon
        rt = MagicMock()
        rt.shutdown = AsyncMock()
        rt_cls.return_value = rt
        core = MagicMock()
        core.shutdown = AsyncMock()
        core_cls.return_value = core
        await c.shutdown()
        mon.shutdown.assert_awaited_once()
        rt.shutdown.assert_awaited_once()
        core.shutdown.assert_awaited_once()


@pytest.mark.asyncio
async def test_shutdown_logs_runtime_error() -> None:
    c = ApplicationContainer()
    with patch("server.container.bundles.MonitoringBundle") as mon_cls:
        mon = MagicMock()
        mon.shutdown = AsyncMock(side_effect=RuntimeError("shutdown fail"))
        mon_cls.return_value = mon
        await c.shutdown()


@pytest.mark.asyncio
async def test_initialize_success_with_mocked_bundles() -> None:
    c = ApplicationContainer()

    def _mk_bundle() -> MagicMock:
        b = MagicMock()
        b.initialize = AsyncMock()
        b.initialize_nats_combat = AsyncMock()
        return b

    combat = _mk_bundle()

    async def _after_core(container: ApplicationContainer) -> None:
        container.combat_service = MagicMock()
        container.magic_service = MagicMock()
        container.quest_service = MagicMock()
        container.spell_learning_service = MagicMock()

    core = _mk_bundle()
    core.initialize = AsyncMock(side_effect=_after_core)

    with (
        patch("server.container.bundles.CoreBundle", return_value=core),
        patch("server.container.bundles.RealtimeBundle", return_value=_mk_bundle()),
        patch("server.container.bundles.GameBundle", return_value=_mk_bundle()),
        patch("server.container.bundles.MonitoringBundle", return_value=_mk_bundle()),
        patch("server.container.bundles.CombatBundle", return_value=combat),
        patch("server.container.bundles.NPCBundle", return_value=_mk_bundle()),
        patch("server.container.bundles.MagicBundle", return_value=_mk_bundle()),
        patch("server.container.bundles.ChatBundle", return_value=_mk_bundle()),
        patch("server.container.bundles.TimeBundle", return_value=_mk_bundle()),
        patch("server.container.bundles.core.CORE_ATTRS", ()),
        patch("server.container.bundles.realtime.REALTIME_ATTRS", ()),
        patch("server.container.bundles.game.GAME_ATTRS", ()),
        patch("server.container.bundles.monitoring.MONITORING_ATTRS", ()),
        patch("server.container.bundles.combat.COMBAT_ATTRS", ()),
        patch("server.container.bundles.npc.NPC_ATTRS", ()),
        patch("server.container.bundles.magic.MAGIC_ATTRS", ()),
        patch("server.container.bundles.chat.CHAT_ATTRS", ()),
        patch("server.container.bundles.time.TIME_ATTRS", ()),
    ):
        await c.initialize()

    assert c.is_initialized is True
    assert c.combat_service.magic_service is c.magic_service
    c.quest_service.set_spell_learning_service.assert_called_once_with(c.spell_learning_service)
