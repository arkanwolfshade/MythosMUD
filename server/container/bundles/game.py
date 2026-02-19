"""
Game bundle: player, room, movement, exploration, user_manager, container_service,
caches, temporal services, item services.

Depends on CoreBundle and RealtimeBundle (for nats_message_handler.user_manager).
"""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

from pydantic import ValidationError

from server.container.utils import decode_json_column
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.project_paths import (
    get_calendar_paths_for_environment,
    get_environment_data_dir,
    normalize_environment,
)

if TYPE_CHECKING:
    from server.container.main import ApplicationContainer

logger = get_logger(__name__)

GAME_ATTRS = (
    "instance_manager",
    "movement_service",
    "follow_service",
    "party_service",
    "exploration_service",
    "player_service",
    "room_service",
    "user_manager",
    "container_service",
    "level_service",
    "skill_service",
    "room_cache_service",
    "profession_cache_service",
    "holiday_service",
    "schedule_service",
    "mythos_tick_scheduler",
    "item_prototype_registry",
    "item_factory",
)


class GameBundle:  # pylint: disable=too-many-instance-attributes,too-few-public-methods
    """Game services: movement, player, room, user, container, caches, temporal, items."""

    instance_manager: Any = None
    movement_service: Any = None
    follow_service: Any = None
    party_service: Any = None
    exploration_service: Any = None
    player_service: Any = None
    room_service: Any = None
    user_manager: Any = None
    container_service: Any = None
    level_service: Any = None
    skill_service: Any = None
    room_cache_service: Any = None
    profession_cache_service: Any = None
    holiday_service: Any = None
    schedule_service: Any = None
    mythos_tick_scheduler: Any = None
    item_prototype_registry: Any = None
    item_factory: Any = None

    async def initialize(self, container: ApplicationContainer) -> None:  # pylint: disable=too-many-locals,too-many-statements
        """Initialize game services. Requires Core and Realtime."""
        config = container.config
        persistence = container.persistence
        async_persistence = container.async_persistence
        database_manager = container.database_manager
        event_bus = container.event_bus
        task_registry = container.task_registry
        nats_message_handler = container.nats_message_handler

        if config is None or persistence is None or async_persistence is None or database_manager is None:
            raise RuntimeError("Core services must be initialized before GameBundle")

        normalized_environment = normalize_environment(config.logging.environment)

        # Movement and exploration
        logger.debug("Initializing gameplay services...")
        from server.game.movement_service import MovementService
        from server.services.exploration_service import ExplorationService

        self.exploration_service = ExplorationService(database_manager=database_manager)
        from server.game.instance_manager import InstanceManager

        instance_manager = InstanceManager(
            room_cache=async_persistence._room_cache,  # pylint: disable=protected-access  # Reason: InstanceManager needs shared room cache reference for template lookup
            event_bus=event_bus,
        )
        async_persistence.set_instance_manager(instance_manager)
        self.instance_manager = instance_manager
        self.movement_service = MovementService(
            event_bus=event_bus,
            async_persistence=async_persistence,
            exploration_service=self.exploration_service,
            instance_manager=instance_manager,
        )
        from server.game.follow_service import FollowService
        from server.services.player_position_service import PlayerPositionService

        connection_manager = getattr(container, "connection_manager", None)
        alias_storage = getattr(container, "alias_storage", None)
        player_position_service = PlayerPositionService(
            async_persistence,
            connection_manager,
            alias_storage,
        )
        self.follow_service = FollowService(
            event_bus=event_bus,
            movement_service=self.movement_service,
            user_manager=None,  # Set below after user_manager is created
            connection_manager=connection_manager,
            async_persistence=async_persistence,
            player_position_service=player_position_service,
        )
        from server.game.party_service import PartyService

        self.party_service = PartyService(
            event_bus=event_bus,
            connection_manager=connection_manager,
            async_persistence=async_persistence,
        )
        logger.info("Exploration, movement, follow and party services initialized")

        # Temporal services
        logger.debug("Initializing temporal services...")
        from server.services.holiday_service import HolidayService
        from server.services.schedule_service import ScheduleService
        from server.time.time_service import get_mythos_chronicle

        holidays_path, schedules_dir = get_calendar_paths_for_environment(normalized_environment)
        self.holiday_service = HolidayService(
            chronicle=get_mythos_chronicle(),
            data_path=holidays_path,
            environment=normalized_environment,
            async_persistence=async_persistence,
        )
        self.schedule_service = ScheduleService(
            schedule_dir=schedules_dir,
            environment=normalized_environment,
            async_persistence=async_persistence,
        )
        logger.info(
            "Temporal schedule and holiday services initialized",
            holiday_count=len(self.holiday_service.collection.holidays),
            schedule_entries=self.schedule_service.entry_count if self.schedule_service else 0,
        )

        from server.time.tick_scheduler import MythosTickScheduler

        holiday_service = self.holiday_service

        def _resolve_hourly_holidays(mythos_dt: datetime) -> list[str]:
            if not holiday_service:
                return []
            try:
                active = holiday_service.refresh_active(mythos_dt)
                return [entry.name for entry in active]
            except (ValueError, TypeError, AttributeError, RuntimeError) as exc:
                logger.warning("Failed to resolve holiday window for tick scheduler", error=str(exc))
                return []

        self.mythos_tick_scheduler = MythosTickScheduler(
            chronicle=get_mythos_chronicle(),
            event_bus=event_bus,
            task_registry=task_registry,
            holiday_resolver=_resolve_hourly_holidays,
        )
        logger.info("Mythos tick scheduler prepared")

        # Game services
        logger.debug("Initializing game services...")
        from server.game.player_service import PlayerService
        from server.game.room_service import RoomService
        from server.services.user_manager import UserManager

        self.player_service = PlayerService(
            persistence=persistence,
            instance_manager=self.instance_manager,
        )
        self.room_service = RoomService(persistence=persistence)

        user_management_dir = get_environment_data_dir(normalized_environment) / "user_management"
        self.user_manager = UserManager(data_dir=user_management_dir)
        if self.follow_service is not None:
            self.follow_service._user_manager = self.user_manager  # pylint: disable=protected-access  # Reason: FollowService requires UserManager set after bundle init order
        if nats_message_handler is not None:
            nats_message_handler.user_manager = self.user_manager
            nats_message_handler.party_service = self.party_service

        from server.services.container_service import ContainerService

        self.container_service = ContainerService(persistence=persistence)
        from server.game.skill_service import SkillService
        from server.persistence.repositories.player_skill_repository import PlayerSkillRepository
        from server.persistence.repositories.skill_repository import SkillRepository
        from server.persistence.repositories.skill_use_log_repository import SkillUseLogRepository

        self.skill_service = SkillService(
            skill_repository=SkillRepository(),
            player_skill_repository=PlayerSkillRepository(),
            skill_use_log_repository=SkillUseLogRepository(),
            persistence=async_persistence,
        )

        async def _skill_improvement_on_level_up(player_id: Any, new_level: int) -> None:
            await self.skill_service.run_improvement_rolls(player_id, new_level)

        from server.game.level_service import LevelService

        self.level_service = LevelService(
            async_persistence=async_persistence,
            level_up_hook=_skill_improvement_on_level_up,
        )
        logger.info("Container, level and skill services initialized")
        logger.info("Game services initialized")

        # Item services
        await self._initialize_item_services(container)
        if self.item_prototype_registry and self.player_service:
            self.player_service.set_item_prototype_registry(self.item_prototype_registry)

        # Caching
        logger.debug("Initializing caching services...")
        try:
            from server.caching.cache_service import ProfessionCacheService, RoomCacheService

            self.room_cache_service = RoomCacheService(persistence)
            self.profession_cache_service = ProfessionCacheService(persistence)
            logger.info("Caching services initialized")
        except RuntimeError as e:
            logger.warning("Caching services initialization failed - will use persistence directly", error=str(e))
            self.room_cache_service = None
            self.profession_cache_service = None

    async def _initialize_item_services(self, container: ApplicationContainer) -> None:  # pylint: disable=too-many-locals
        """Load item prototypes from PostgreSQL and create item factory."""
        from sqlalchemy import select
        from sqlalchemy.exc import SQLAlchemyError

        from server.game.items.item_factory import ItemFactory
        from server.game.items.models import ItemPrototypeModel
        from server.game.items.prototype_registry import PrototypeRegistry
        from server.models.item import ItemPrototype

        database_manager = container.database_manager
        if not database_manager:
            logger.warning("Database manager not initialized; item services will remain unavailable")
            self.item_prototype_registry = None
            self.item_factory = None
            return

        prototypes: dict[str, ItemPrototypeModel] = {}
        invalid_entries: list[dict[str, Any]] = []

        try:
            session_maker = database_manager.get_session_maker()

            async with session_maker() as session:
                result = await session.execute(select(ItemPrototype))
                item_prototypes = result.scalars().all()

                for db_prototype in item_prototypes:
                    payload = {
                        "prototype_id": db_prototype.prototype_id,
                        "name": db_prototype.name,
                        "short_description": db_prototype.short_description,
                        "long_description": db_prototype.long_description,
                        "item_type": db_prototype.item_type,
                        "weight": float(db_prototype.weight) if db_prototype.weight is not None else 0.0,
                        "base_value": int(db_prototype.base_value) if db_prototype.base_value is not None else 0,
                        "durability": int(db_prototype.durability) if db_prototype.durability is not None else None,
                        "flags": decode_json_column(db_prototype.flags, list),
                        "wear_slots": decode_json_column(db_prototype.wear_slots, list),
                        "stacking_rules": decode_json_column(db_prototype.stacking_rules, dict),
                        "usage_restrictions": decode_json_column(db_prototype.usage_restrictions, dict),
                        "effect_components": decode_json_column(db_prototype.effect_components, list),
                        "metadata": decode_json_column(db_prototype.metadata_payload, dict),
                        "tags": decode_json_column(db_prototype.tags, list),
                    }

                    try:
                        prototype = ItemPrototypeModel.model_validate(payload)
                        prototypes[prototype.prototype_id] = prototype
                    except ValidationError as exc:
                        logger.warning(
                            "Invalid item prototype skipped during initialization",
                            prototype_id=payload.get("prototype_id"),
                            error=str(exc),
                        )
                        invalid_entries.append({"prototype_id": payload.get("prototype_id"), "error": str(exc)})

            registry = PrototypeRegistry(prototypes, invalid_entries)
            self.item_prototype_registry = registry
            self.item_factory = ItemFactory(registry)

            logger.info(
                "Item services initialized from PostgreSQL",
                prototype_count=len(prototypes),
                invalid_count=len(invalid_entries),
            )
        except SQLAlchemyError as exc:
            logger.error(
                "Failed to load item prototypes from PostgreSQL database",
                error=str(exc),
                error_type=type(exc).__name__,
            )
            self.item_prototype_registry = None
            self.item_factory = None
