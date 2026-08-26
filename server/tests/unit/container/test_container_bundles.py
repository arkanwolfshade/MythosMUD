"""Unit tests for container bundle modules."""

import uuid
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.container.bundles.chat import CHAT_ATTRS, ChatBundle
from server.container.bundles.combat import COMBAT_ATTRS, CombatBundle
from server.container.bundles.core import CORE_ATTRS, CoreBundle
from server.container.bundles.game import GAME_ATTRS, GameBundle
from server.container.bundles.magic import (
    MAGIC_ATTRS,
    MagicBundle,
    _create_registry_and_targeting,
    _validate_magic_prerequisites,
)
from server.container.bundles.monitoring import MONITORING_ATTRS, MonitoringBundle
from server.container.bundles.npc import NPC_ATTRS, NPCBundle
from server.container.bundles.realtime import REALTIME_ATTRS, RealtimeBundle
from server.container.bundles.time import TIME_ATTRS, TimeBundle
from server.container.main import _flatten_bundle


def test_bundle_attr_constants() -> None:
    assert "chat_service" in CHAT_ATTRS
    assert "passive_lucidity_flux_service" in COMBAT_ATTRS
    assert "persistence" in CORE_ATTRS
    assert "player_service" in GAME_ATTRS
    assert "magic_service" in MAGIC_ATTRS
    assert "performance_monitor" in MONITORING_ATTRS
    assert "npc_lifecycle_manager" in NPC_ATTRS
    assert "connection_manager" in REALTIME_ATTRS
    assert "mythos_time_consumer" in TIME_ATTRS
    assert "holiday_service" in TIME_ATTRS
    assert "schedule_service" in TIME_ATTRS
    assert "mythos_tick_scheduler" in TIME_ATTRS
    # #635: temporal services moved out of GameBundle into TimeBundle -- the Temporal bounded
    # context (docs/BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md) should live in exactly one bundle.
    assert "holiday_service" not in GAME_ATTRS
    assert "schedule_service" not in GAME_ATTRS
    assert "mythos_tick_scheduler" not in GAME_ATTRS


def test_game_bundle_require_core_services_raises() -> None:
    container = MagicMock(config=None, persistence=MagicMock(), async_persistence=MagicMock(), database_manager=None)
    with pytest.raises(RuntimeError, match="Core services"):
        GameBundle._require_core_services(container)


def test_time_bundle_resolve_hourly_holidays() -> None:
    bundle = TimeBundle()
    assert bundle._resolve_hourly_holidays(datetime.now()) == []
    bundle.holiday_service = MagicMock()
    entry = MagicMock()
    entry.name = "Feast"
    bundle.holiday_service.refresh_active.return_value = [entry]
    names = bundle._resolve_hourly_holidays(datetime.now())
    assert names == ["Feast"]
    bundle.holiday_service.refresh_active.side_effect = RuntimeError("calendar offline")
    assert bundle._resolve_hourly_holidays(datetime.now()) == []


def test_game_bundle_wire_helpers() -> None:
    bundle = GameBundle()
    follow = MagicMock()
    nats_handler = MagicMock()
    user_manager = MagicMock()
    bundle.party_service = MagicMock()
    bundle._wire_user_manager_after_init(follow, nats_handler, user_manager)
    assert follow._user_manager is user_manager
    assert nats_handler.user_manager is user_manager
    bundle.player_service = MagicMock()
    bundle.item_prototype_registry = MagicMock()
    bundle._wire_item_registry_to_player_service()
    bundle.player_service.set_item_prototype_registry.assert_called_once()


def test_game_bundle_build_prototype_payload() -> None:
    bundle = GameBundle()
    db_row = MagicMock(
        prototype_id="p1",
        name="Lantern",
        short_description="short",
        long_description="long",
        item_type="item",
        weight=1.5,
        base_value=10,
        durability=5,
        flags='["lit"]',
        wear_slots="[]",
        stacking_rules="{}",
        usage_restrictions="{}",
        effect_components="[]",
        metadata_payload='{"color":"brass"}',
        tags='["light"]',
    )
    payload = bundle._build_prototype_payload(db_row)
    assert payload["prototype_id"] == "p1"
    assert payload["flags"] == ["lit"]


def test_game_bundle_handle_item_prototypes_db_error() -> None:
    bundle = GameBundle()
    bundle.item_prototype_registry = MagicMock()
    bundle.item_factory = MagicMock()
    bundle._handle_item_prototypes_db_error(Exception("UndefinedTableError: missing"))
    assert bundle.item_prototype_registry is None
    assert bundle.item_factory is None


def test_game_bundle_initialize_caching_services_success() -> None:
    bundle = GameBundle()
    with patch("server.caching.cache_service.RoomCacheService", return_value=MagicMock()):
        with patch("server.caching.cache_service.ProfessionCacheService", return_value=MagicMock()):
            bundle._initialize_caching_services(MagicMock())
    assert bundle.room_cache_service is not None
    assert bundle.profession_cache_service is not None


def test_game_bundle_initialize_caching_services_failure() -> None:
    bundle = GameBundle()
    with patch("server.caching.cache_service.RoomCacheService", side_effect=RuntimeError("cache down")):
        bundle._initialize_caching_services(MagicMock())
    assert bundle.room_cache_service is None


@pytest.mark.asyncio
async def test_game_bundle_init_emote_service_loads_once() -> None:
    """#624: GameBundle constructs EmoteRepository/EmoteService and loads once at init time,
    matching SpellRegistry's pattern -- not reconstructed/reloaded per command."""
    bundle = GameBundle()
    mock_repo_instance = MagicMock()
    mock_repo_instance.get_emotes = AsyncMock(return_value=[])
    mock_repo_instance.get_emote_aliases = AsyncMock(return_value=[])
    with (
        patch("server.persistence.repositories.emote_repository.EmoteRepository", return_value=mock_repo_instance),
    ):
        await bundle._init_emote_service()

    assert bundle.emote_repository is mock_repo_instance
    assert bundle.emote_service is not None
    mock_repo_instance.get_emotes.assert_awaited_once()
    mock_repo_instance.get_emote_aliases.assert_awaited_once()


def test_game_attrs_includes_emote_service() -> None:
    """#624: emote_repository/emote_service must be in GAME_ATTRS or _flatten_bundle never copies
    them onto ApplicationContainer, and every app.state/container.emote_service read breaks."""
    assert "emote_repository" in GAME_ATTRS
    assert "emote_service" in GAME_ATTRS


@pytest.mark.asyncio
async def test_core_bundle_shutdown() -> None:
    bundle = CoreBundle()
    bundle.event_bus = AsyncMock()
    bundle.database_manager = AsyncMock()
    bundle.async_persistence = AsyncMock()
    with patch("server.npc_database.close_npc_db", AsyncMock()):
        await bundle.shutdown(MagicMock())
    bundle.event_bus.shutdown.assert_awaited_once()


@pytest.mark.asyncio
async def test_monitoring_bundle_initialize_and_shutdown() -> None:
    bundle = MonitoringBundle()
    await bundle.initialize(MagicMock())
    assert bundle.performance_monitor is not None
    assert bundle.monitoring_dashboard is not None
    bundle.log_aggregator.shutdown = MagicMock()
    await bundle.shutdown(MagicMock())
    bundle.log_aggregator.shutdown.assert_called_once()


def test_realtime_bundle_require_core_services() -> None:
    container = MagicMock(config=None, event_bus=MagicMock(), task_registry=MagicMock(), async_persistence=MagicMock())
    with pytest.raises(RuntimeError, match="Core services"):
        RealtimeBundle._require_core_services(container)


@pytest.mark.asyncio
async def test_realtime_bundle_connect_nats_skips_unit_test() -> None:
    bundle = RealtimeBundle()
    config = MagicMock()
    config.logging.environment = "unit_test"
    assert await bundle._connect_nats(config, MagicMock()) is None


def test_realtime_bundle_setup_nats_dependent_services_without_nats() -> None:
    bundle = RealtimeBundle()
    bundle.nats_service = None
    bundle.connection_manager = MagicMock()
    bundle._setup_nats_dependent_services(MagicMock())
    assert bundle.event_publisher is None
    assert bundle.nats_message_handler is None


@pytest.mark.asyncio
async def test_realtime_bundle_initialize_unit_test() -> None:
    bundle = RealtimeBundle()
    container = MagicMock()
    container.config = MagicMock()
    container.config.logging.environment = "unit_test"
    container.config.nats.enabled = False
    container.event_bus = MagicMock()
    container.task_registry = MagicMock()
    container.async_persistence = MagicMock()
    with patch("server.realtime.connection_manager.ConnectionManager") as cm_cls:
        cm_cls.return_value = MagicMock(room_manager=MagicMock())
        with patch("server.realtime.event_handler.RealTimeEventHandler"):
            await bundle.initialize(container)
    assert bundle.connection_manager is not None
    assert bundle.nats_service is None


@pytest.mark.asyncio
async def test_chat_bundle_initialize_test_mode() -> None:
    bundle = ChatBundle()
    container = MagicMock()
    container.config = MagicMock()
    container.config.logging.environment = "unit_test"
    container.persistence = MagicMock()
    container.player_service = MagicMock()
    container.user_manager = MagicMock()
    container.nats_service = None
    container.event_bus = MagicMock()
    with patch("server.game.chat_service.ChatService", return_value=MagicMock(nats_service=None)):
        with patch("server.game.chat_npc_system.set_chat_service_for_npc_system"):
            with patch("server.game.chat_npc_system.subscribe_npc_spoke_to_chat"):
                await bundle.initialize(container)
    assert bundle.chat_service is not None


@pytest.mark.asyncio
async def test_chat_bundle_initialize_missing_player_service() -> None:
    bundle = ChatBundle()
    container = MagicMock()
    container.config = MagicMock()
    container.persistence = MagicMock()
    container.player_service = None
    with pytest.raises(RuntimeError, match="PlayerService"):
        await bundle.initialize(container)


def _time_bundle_container(**overrides: object) -> MagicMock:
    """Container stand-in with the deps TimeBundle.initialize() needs, before overrides."""
    container = MagicMock()
    container.config.logging.environment = "unit_test"
    container.async_persistence = MagicMock()
    container.event_bus = MagicMock()
    container.task_registry = MagicMock()
    container.room_service = MagicMock()
    container.npc_lifecycle_manager = MagicMock()
    for key, value in overrides.items():
        setattr(container, key, value)
    return container


def _patch_temporal_construction():
    """Patch the classes TimeBundle._init_temporal_services() constructs."""
    holiday_cls = patch("server.services.holiday_service.HolidayService")
    sched_cls = patch("server.services.schedule_service.ScheduleService")
    tick_cls = patch("server.time.tick_scheduler.MythosTickScheduler")
    chronicle = patch("server.time.time_service.get_mythos_chronicle", return_value=MagicMock())
    return holiday_cls, sched_cls, tick_cls, chronicle


@pytest.mark.asyncio
async def test_time_bundle_initialize_with_deps() -> None:
    bundle = TimeBundle()
    container = _time_bundle_container()
    holiday_cls, sched_cls, tick_cls, chronicle = _patch_temporal_construction()
    with holiday_cls as holiday_mock, sched_cls, tick_cls, chronicle:
        holiday_mock.return_value.collection.holidays = []
        with patch("server.time.time_event_consumer.MythosTimeEventConsumer"):
            await bundle.initialize(container)
    assert bundle.holiday_service is not None
    assert bundle.schedule_service is not None
    assert bundle.mythos_tick_scheduler is not None
    assert bundle.mythos_time_consumer is not None


@pytest.mark.asyncio
async def test_time_bundle_initialize_missing_deps() -> None:
    """#635: holiday_service/schedule_service construct unconditionally now, so the consumer's
    'missing dependencies' case is driven by room_service/npc_lifecycle_manager, not by them."""
    bundle = TimeBundle()
    container = _time_bundle_container(room_service=None, npc_lifecycle_manager=None)
    holiday_cls, sched_cls, tick_cls, chronicle = _patch_temporal_construction()
    with holiday_cls as holiday_mock, sched_cls, tick_cls, chronicle:
        holiday_mock.return_value.collection.holidays = []
        await bundle.initialize(container)
    assert bundle.holiday_service is not None
    assert bundle.mythos_time_consumer is None


@pytest.mark.asyncio
async def test_time_bundle_attrs_flatten_onto_container() -> None:
    """#635 regression: container.holiday_service/schedule_service/mythos_tick_scheduler must
    resolve via _flatten_bundle(TimeBundle) after the move -- root-container attribute access
    unchanged, per the issue's own acceptance criterion, not merely GameBundle no longer setting
    them."""
    bundle = TimeBundle()
    container = _time_bundle_container()
    holiday_cls, sched_cls, tick_cls, chronicle = _patch_temporal_construction()
    with holiday_cls as holiday_mock, sched_cls, tick_cls, chronicle:
        holiday_mock.return_value.collection.holidays = []
        with patch("server.time.time_event_consumer.MythosTimeEventConsumer"):
            await bundle.initialize(container)

    _flatten_bundle(container, bundle, TIME_ATTRS)

    assert container.holiday_service is bundle.holiday_service
    assert container.schedule_service is bundle.schedule_service
    assert container.mythos_tick_scheduler is bundle.mythos_tick_scheduler
    assert container.holiday_service is not None


@pytest.mark.asyncio
async def test_npc_bundle_raises_without_event_bus() -> None:
    bundle = NPCBundle()
    container = MagicMock(event_bus=None, persistence=MagicMock(), async_persistence=MagicMock())
    with pytest.raises(RuntimeError, match="EventBus"):
        await bundle.initialize(container)


def test_magic_validate_prerequisites() -> None:
    container = MagicMock(async_persistence=None, player_service=MagicMock(), combat_service=MagicMock())
    container.config.logging.environment = "production"
    with pytest.raises(RuntimeError, match="async_persistence"):
        _validate_magic_prerequisites(container)


def test_combat_bundle_validate_nats_prerequisites() -> None:
    bundle = CombatBundle()
    container = MagicMock(config=None)
    with pytest.raises(RuntimeError, match="Config"):
        bundle._validate_nats_combat_prerequisites(container)


def test_combat_bundle_handle_nats_unavailable_test_mode() -> None:
    bundle = CombatBundle()
    bundle._handle_nats_unavailable(is_testing=True)
    assert bundle.combat_service is None


def test_combat_bundle_handle_nats_unavailable_prod_raises() -> None:
    bundle = CombatBundle()
    with pytest.raises(RuntimeError, match="NATS"):
        bundle._handle_nats_unavailable(is_testing=False)


@pytest.mark.asyncio
async def test_combat_bundle_initialize_nats_unavailable_in_test() -> None:
    bundle = CombatBundle()
    bundle.player_combat_service = MagicMock()
    bundle.player_death_service = MagicMock()
    bundle.player_respawn_service = MagicMock()
    container = MagicMock()
    container.config = MagicMock()
    container.config.logging.environment = "unit_test"
    container.nats_service = None
    container.event_bus = MagicMock()
    await bundle.initialize_nats_combat(container)
    assert bundle.combat_service is None


@pytest.mark.asyncio
async def test_npc_bundle_raises_without_persistence() -> None:
    bundle = NPCBundle()
    container = MagicMock(event_bus=MagicMock(), persistence=None, async_persistence=MagicMock())
    with pytest.raises(RuntimeError, match="Persistence"):
        await bundle.initialize(container)


@pytest.mark.asyncio
async def test_npc_bundle_initialize_success() -> None:
    bundle = NPCBundle()
    container = MagicMock()
    container.event_bus = MagicMock()
    container.persistence = MagicMock()
    container.async_persistence = MagicMock()

    lifecycle = MagicMock()
    lifecycle.thread_manager = None

    async def npc_session_gen():
        session = AsyncMock()
        yield session

    with patch("server.npc.combat_integration.NPCCombatIntegration", return_value=MagicMock()):
        with patch("server.npc.spawning_service.NPCSpawningService") as spawn_cls:
            spawn_instance = MagicMock()
            spawn_cls.return_value = spawn_instance
            with patch("server.npc.lifecycle_manager.NPCLifecycleManager", return_value=lifecycle):
                with patch("server.npc.population_control.NPCPopulationController") as pop_cls:
                    pop_instance = MagicMock()
                    pop_cls.return_value = pop_instance
                    with patch("server.services.npc_instance_service.initialize_npc_instance_service"):
                        with patch("server.services.npc_service.NPCService") as npc_svc_cls:
                            npc_svc = AsyncMock()
                            npc_svc.get_npc_definitions = AsyncMock(return_value=[])
                            npc_svc.get_spawn_rules = AsyncMock(return_value=[])
                            npc_svc_cls.return_value = npc_svc
                            with patch("server.npc_database.get_npc_session", return_value=npc_session_gen()):
                                await bundle.initialize(container)

    assert bundle.npc_lifecycle_manager is lifecycle
    assert bundle.npc_spawning_service is spawn_instance
    assert bundle.npc_population_controller is pop_instance


@pytest.mark.asyncio
async def test_core_bundle_initialize() -> None:
    bundle = CoreBundle()
    config = MagicMock()
    config.logging.environment = "unit_test"
    async_persistence = AsyncMock()
    async_persistence.warmup_room_cache = AsyncMock()

    with patch("server.config.get_config", return_value=config):
        with patch("server.database.init_db", AsyncMock()):
            with patch("server.npc_database.init_npc_db", AsyncMock()):
                with patch("server.database.DatabaseManager.get_instance", return_value=MagicMock()):
                    with patch("server.events.distributed_event_bus.DistributedEventBus", return_value=MagicMock()):
                        with patch(
                            "server.async_persistence.AsyncPersistenceLayer",
                            return_value=async_persistence,
                        ):
                            await bundle.initialize(MagicMock())

    assert bundle.config is config
    assert bundle.async_persistence is async_persistence


@pytest.mark.asyncio
async def test_core_bundle_initialize_warmup_failure() -> None:
    bundle = CoreBundle()
    config = MagicMock()
    config.logging.environment = "unit_test"
    async_persistence = AsyncMock()
    async_persistence.warmup_room_cache = AsyncMock(side_effect=RuntimeError("cache cold"))

    with patch("server.config.get_config", return_value=config):
        with patch("server.database.init_db", AsyncMock()):
            with patch("server.npc_database.init_npc_db", AsyncMock()):
                with patch("server.database.DatabaseManager.get_instance", return_value=MagicMock()):
                    with patch("server.events.distributed_event_bus.DistributedEventBus", return_value=MagicMock()):
                        with patch(
                            "server.async_persistence.AsyncPersistenceLayer",
                            return_value=async_persistence,
                        ):
                            await bundle.initialize(MagicMock())

    assert bundle.event_bus is not None


@pytest.mark.asyncio
async def test_combat_bundle_initialize() -> None:
    bundle = CombatBundle()
    container = MagicMock()
    container.persistence = MagicMock()
    container.event_bus = MagicMock()
    container.performance_monitor = MagicMock()
    container.connection_manager = MagicMock()
    container.movement_service = MagicMock()
    container.async_persistence = MagicMock()

    with patch("server.services.player_combat_service.PlayerCombatService", return_value=MagicMock()):
        with patch("server.services.player_death_service.PlayerDeathService", return_value=MagicMock()):
            with patch("server.services.player_respawn_service.PlayerRespawnService", return_value=MagicMock()):
                with patch("server.services.catatonia_registry.CatatoniaRegistry", return_value=MagicMock()):
                    with patch(
                        "server.services.passive_lucidity_flux_service.PassiveLucidityFluxService",
                        return_value=MagicMock(),
                    ):
                        await bundle.initialize(container)

    assert bundle.player_combat_service is not None
    assert bundle.passive_lucidity_flux_service is not None


@pytest.mark.asyncio
async def test_combat_bundle_sanitarium_failover_no_db_manager() -> None:
    bundle = CombatBundle()
    container = MagicMock(database_manager=None)
    await bundle._sanitarium_failover_callback(container, str(uuid.uuid4()), 0)


@pytest.mark.asyncio
async def test_realtime_bundle_connect_nats_disabled() -> None:
    bundle = RealtimeBundle()
    config = MagicMock()
    config.logging.environment = "production"
    config.nats.enabled = False
    assert await bundle._connect_nats(config, MagicMock()) is None


@pytest.mark.asyncio
async def test_realtime_bundle_shutdown() -> None:
    bundle = RealtimeBundle()
    bundle.nats_message_handler = AsyncMock()
    bundle.nats_service = AsyncMock()
    await bundle.shutdown(MagicMock())
    bundle.nats_message_handler.stop.assert_awaited_once()
    bundle.nats_service.disconnect.assert_awaited_once()


def test_realtime_bundle_setup_nats_dependent_services_with_nats() -> None:
    bundle = RealtimeBundle()
    bundle.nats_service = MagicMock(subject_manager=MagicMock())
    bundle.connection_manager = MagicMock()
    with patch("server.realtime.event_publisher.EventPublisher", return_value=MagicMock()):
        with patch("server.realtime.nats_message_handler.NATSMessageHandler", return_value=MagicMock()):
            bundle._setup_nats_dependent_services(MagicMock())
    assert bundle.event_publisher is not None
    assert bundle.nats_message_handler is not None


async def test_game_bundle_initialize_item_services_no_db() -> None:
    bundle = GameBundle()
    container = MagicMock(database_manager=None)
    await bundle._initialize_item_services(container)
    assert bundle.item_prototype_registry is None


@pytest.mark.asyncio
async def test_magic_bundle_initialize_unit_test() -> None:
    bundle = MagicBundle()
    container = MagicMock()
    container.async_persistence = MagicMock()
    container.player_service = MagicMock()
    container.combat_service = None
    container.config = MagicMock()
    container.config.logging.environment = "unit_test"
    with patch(
        "server.container.bundles.magic._create_registry_and_targeting",
        AsyncMock(return_value=(MagicMock(), MagicMock())),
    ):
        with patch("server.container.bundles.magic._create_learning_mp_regen_and_magic"):
            await bundle.initialize(container)


@pytest.mark.asyncio
async def test_npc_bundle_initialize() -> None:
    bundle = NPCBundle()
    container = MagicMock()
    container.event_bus = MagicMock()
    container.persistence = MagicMock()
    container.async_persistence = MagicMock()

    async def npc_session_gen():
        session = AsyncMock()
        yield session

    with patch("server.npc.combat_integration.NPCCombatIntegration"):
        with patch("server.npc.spawning_service.NPCSpawningService"):
            with patch("server.npc.lifecycle_manager.NPCLifecycleManager") as lm_cls:
                lm_cls.return_value.thread_manager = AsyncMock()
                lm_cls.return_value.thread_manager.start = AsyncMock()
                with patch("server.npc.population_control.NPCPopulationController"):
                    with patch("server.services.npc_instance_service.initialize_npc_instance_service"):
                        with patch("server.services.npc_service.NPCService") as svc_cls:
                            svc = svc_cls.return_value
                            svc.get_npc_definitions = AsyncMock(return_value=[])
                            svc.get_spawn_rules = AsyncMock(return_value=[])
                            with patch("server.npc_database.get_npc_session", return_value=npc_session_gen()):
                                await bundle.initialize(container)
    assert bundle.npc_lifecycle_manager is not None


async def test_realtime_bundle_connect_nats_success() -> None:
    bundle = RealtimeBundle()
    config = MagicMock()
    config.logging.environment = "development"
    config.nats.enabled = True
    config.nats.connect_timeout = 5
    config.nats.url = "nats://localhost:4222"
    event_bus = MagicMock()
    nats_service = MagicMock()
    nats_service.connect = AsyncMock(return_value=True)
    with patch("server.services.nats_service.NATSService", return_value=nats_service):
        result = await bundle._connect_nats(config, event_bus)
    assert result is nats_service
    event_bus.set_nats_service.assert_called_once_with(nats_service)


async def test_combat_bundle_sanitarium_failover_callback() -> None:
    bundle = CombatBundle()
    bundle.player_respawn_service = AsyncMock()
    container = MagicMock()
    session = AsyncMock()
    session_maker = MagicMock()
    session_maker.__aenter__ = AsyncMock(return_value=session)
    session_maker.__aexit__ = AsyncMock(return_value=None)
    container.database_manager.get_session_maker.return_value = MagicMock(return_value=session_maker)
    with patch("server.services.lucidity_service.LucidityService") as lucidity_cls:
        lucidity_cls.return_value.clear_hallucination_timers = AsyncMock(return_value=0)
        with patch("server.container.bundles.combat.sleep", AsyncMock()):
            await bundle._sanitarium_failover_callback(container, str(uuid.uuid4()), -100)
    bundle.player_respawn_service.move_player_to_limbo.assert_awaited_once()


@pytest.mark.asyncio
async def test_combat_bundle_initialize_nats_connected() -> None:
    bundle = CombatBundle()
    bundle.player_combat_service = MagicMock()
    bundle.player_death_service = MagicMock()
    bundle.player_respawn_service = MagicMock()
    container = MagicMock()
    container.config = MagicMock()
    container.config.logging.environment = "production"
    container.nats_service = MagicMock()
    container.nats_service.is_connected.return_value = True
    container.event_bus = MagicMock()
    container.player_service = MagicMock()
    container.nats_message_handler = AsyncMock()
    with patch("server.services.combat_service.CombatService"):
        with patch("server.services.combat_service.set_combat_service"):
            await bundle.initialize_nats_combat(container)
    assert bundle.combat_service is not None


@pytest.mark.asyncio
async def test_magic_bundle_create_registry_and_targeting() -> None:
    bundle = MagicBundle()
    container = MagicMock()
    container.async_persistence = MagicMock()
    container.player_service = MagicMock()
    container.combat_service = MagicMock()
    container.player_combat_service = MagicMock()
    with patch("server.persistence.repositories.spell_repository.SpellRepository"):
        with patch("server.game.magic.spell_registry.SpellRegistry") as reg_cls:
            reg_cls.return_value.load_spells = AsyncMock()
            reg_cls.return_value.get_all_spell_ids.return_value = ["spell_a"]
            with patch("server.services.target_resolution_service.TargetResolutionService"):
                with patch("server.game.magic.spell_targeting.SpellTargetingService"):
                    with patch("server.game.magic.spell_effects.SpellEffects"):
                        registry, player_repo = await _create_registry_and_targeting(bundle, container)
    assert registry is not None
    assert player_repo is not None


def test_magic_create_learning_mp_regen_and_magic() -> None:
    from server.container.bundles.magic import _create_learning_mp_regen_and_magic

    bundle = MagicBundle()
    bundle.spell_registry = MagicMock()
    bundle.spell_targeting_service = MagicMock()
    bundle.spell_effects = MagicMock()
    container = MagicMock()
    container.player_service = MagicMock()
    container.combat_service = MagicMock()
    with patch("server.game.magic.spell_learning_service.SpellLearningService"):
        with patch("server.game.magic.mp_regeneration_service.MPRegenerationService"):
            with patch("server.game.magic.magic_service.MagicService"):
                _create_learning_mp_regen_and_magic(bundle, container, MagicMock())
    assert bundle.magic_service is not None


@pytest.mark.asyncio
async def test_game_bundle_initialize_wiring() -> None:
    bundle = GameBundle()
    container = MagicMock()
    container.config = MagicMock()
    container.config.logging.environment = "unit_test"
    container.persistence = MagicMock()
    container.async_persistence = MagicMock()
    container.async_persistence._room_cache = MagicMock()
    container.database_manager = MagicMock()
    container.event_bus = MagicMock()
    container.task_registry = MagicMock()
    container.nats_message_handler = MagicMock()
    container.connection_manager = None
    container.alias_storage = None

    with patch("server.services.exploration_service.ExplorationService"):
        with patch("server.game.instance_manager.InstanceManager"):
            with patch("server.game.movement_service.MovementService"):
                with patch("server.game.follow_service.FollowService"):
                    with patch("server.services.player_position_service.PlayerPositionService"):
                        with patch("server.game.party_service.PartyService"):
                            with patch("server.game.player_service.PlayerService"):
                                with patch("server.game.room_service.RoomService"):
                                    with patch("server.services.user_manager.UserManager"):
                                        with patch("server.services.container_service.ContainerService"):
                                            with patch("server.game.skill_service.SkillService"):
                                                with patch("server.game.level_service.LevelService"):
                                                    with patch("server.game.quest.QuestService"):
                                                        with patch(
                                                            "server.persistence.repositories.quest_definition_repository.QuestDefinitionRepository"
                                                        ):
                                                            with patch(
                                                                "server.persistence.repositories.quest_instance_repository.QuestInstanceRepository"
                                                            ):
                                                                with patch.object(
                                                                    bundle,
                                                                    "_initialize_item_services",
                                                                    AsyncMock(),
                                                                ):
                                                                    with patch.object(
                                                                        bundle,
                                                                        "_initialize_caching_services",
                                                                    ):
                                                                        await bundle.initialize(container)
    assert bundle.player_service is not None
    # #635: temporal services no longer exist on GameBundle at all
    assert not hasattr(bundle, "holiday_service")
    assert not hasattr(bundle, "schedule_service")
    assert not hasattr(bundle, "mythos_tick_scheduler")
