"""
NPC Idle Movement Handler for MythosMUD.

This module provides idle movement functionality for NPCs, allowing them to
wander within their subzone boundaries when not engaged in combat or other
activities.

As documented in the Pnakotic Manuscripts, proper idle movement patterns
are essential for maintaining the illusion of a living, breathing world
while respecting the territorial boundaries that keep entities in their
designated domains.
"""

from __future__ import annotations

import random
import time
import uuid
from collections.abc import Mapping
from typing import TYPE_CHECKING, cast

from structlog.stdlib import BoundLogger

from ..structured_logging.enhanced_logging_config import get_logger
from .movement_integration import NPCMovementIntegration

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer
    from ..events import EventBus

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))


def _npc_id_str(npc: object) -> str:
    raw: object | None = cast(object | None, getattr(npc, "npc_id", None))
    if raw is None:
        return "unknown"
    if isinstance(raw, str):
        return raw
    return str(raw)


def _cfg_bool(config: Mapping[str, object], key: str, default: bool = False) -> bool:
    if key not in config:
        return default
    raw = config[key]
    if isinstance(raw, bool):
        return raw
    if isinstance(raw, (int, float)):
        return bool(raw)
    return default


def _cfg_float(config: Mapping[str, object], key: str, default: float) -> float:
    raw = config.get(key, default)
    if isinstance(raw, bool):
        return default
    if isinstance(raw, (int, float)):
        return float(raw)
    return default


def _npc_alive_and_active(npc: object) -> bool:
    alive = getattr(npc, "is_alive", True)
    active = getattr(npc, "is_active", True)
    return bool(alive) and bool(active)


def _passes_movement_probability(config: Mapping[str, object], npc: object) -> bool:
    movement_probability = _cfg_float(config, "idle_movement_probability", 0.25)
    if random.random() > movement_probability:  # nosec B311: game mechanics, not crypto
        logger.debug(
            "Movement probability check failed",
            npc_id=_npc_id_str(npc),
            probability=movement_probability,
        )
        return False
    return True


def _resolve_spawn_room(npc_instance: object, npc_definition: object, current_room_id: str) -> str:
    spawn = getattr(npc_instance, "spawn_room_id", None)
    if isinstance(spawn, str) and spawn:
        return spawn
    room = getattr(npc_definition, "room_id", current_room_id)
    return room if isinstance(room, str) else current_room_id


class IdleMovementHandler:
    """
    Handler for NPC idle movement logic.

    This class manages the decision-making and execution of idle movement
    for NPCs, including probability checks, exit selection, and subzone
    boundary validation.
    """

    persistence: AsyncPersistenceLayer
    movement_integration: NPCMovementIntegration

    def __init__(
        self,
        event_bus: EventBus | None = None,
        persistence: AsyncPersistenceLayer | None = None,
    ) -> None:
        """
        Initialize the idle movement handler.

        Args:
            event_bus: Optional EventBus instance for movement events
            persistence: Optional persistence layer instance
        """
        if persistence is None:
            raise ValueError("persistence (async_persistence) is required for IdleMovementHandler")
        self.persistence = persistence
        self.movement_integration = NPCMovementIntegration(event_bus, self.persistence)
        logger.debug("Idle movement handler initialized")

    def _should_idle_move_inner(
        self,
        npc_instance: object,
        behavior_config: Mapping[str, object],
        _current_time: float,
    ) -> bool:
        """Core gating for idle movement (interval handled by scheduler)."""
        if not _cfg_bool(behavior_config, "idle_movement_enabled", False):
            logger.debug("Idle movement disabled for NPC", npc_id=_npc_id_str(npc_instance))
            return False
        if self._is_npc_in_combat(npc_instance):
            logger.debug("NPC in combat, skipping idle movement", npc_id=_npc_id_str(npc_instance))
            return False
        if not _npc_alive_and_active(npc_instance):
            logger.debug("NPC not alive or active", npc_id=_npc_id_str(npc_instance))
            return False
        return _passes_movement_probability(behavior_config, npc_instance)

    def should_idle_move(
        self,
        npc_instance: object,
        _npc_definition: object,  # pylint: disable=unused-argument  # reserved for future definition-based behavior
        behavior_config: Mapping[str, object],
        current_time: float | None = None,
    ) -> bool:
        """
        Determine if an NPC should attempt idle movement.

        Checks multiple conditions:
        - Idle movement must be enabled in behavior_config
        - NPC must not be in combat
        - Movement probability check must pass
        - Minimum interval since last movement must have elapsed

        Args:
            npc_instance: The NPC instance to check
            npc_definition: The NPC definition containing subzone info
            behavior_config: Behavior configuration dictionary
            current_time: Current timestamp (defaults to time.time())

        Returns:
            bool: True if NPC should attempt movement, False otherwise
        """
        try:
            ct = time.time() if current_time is None else current_time
            return self._should_idle_move_inner(npc_instance, behavior_config, ct)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error("Error checking if NPC should idle move", npc_id=_npc_id_str(npc_instance), error=str(e))
            return False

    def _check_npc_combat_via_uuid(self, npc_id: str, combat_service: object) -> bool:
        """
        Check if NPC is in combat via UUID lookup.

        Args:
            npc_id: NPC ID (string or UUID)
            combat_service: Combat service instance

        Returns:
            True if NPC is in combat
        """
        combats_raw = getattr(combat_service, "_npc_combats", None)
        if not isinstance(combats_raw, Mapping):
            return False
        combats: Mapping[object, object] = cast(Mapping[object, object], combats_raw)
        try:
            npc_uuid = uuid.UUID(npc_id)
        except ValueError:
            return False
        return npc_uuid in combats

    def _check_npc_combat_via_string_mapping(self, npc_id: str, combat_service: object) -> bool:
        """
        Check if NPC is in combat via string ID mapping.

        Args:
            npc_id: NPC ID as string
            combat_service: Combat service instance

        Returns:
            True if NPC is in combat
        """
        integration: object | None = cast(
            object | None, getattr(combat_service, "_npc_combat_integration_service", None)
        )
        if integration is None:
            return False
        mapping_raw = getattr(integration, "_uuid_to_string_id_mapping", None)
        if not isinstance(mapping_raw, Mapping):
            return False
        mapping: Mapping[object, object] = cast(Mapping[object, object], mapping_raw)
        combats = getattr(combat_service, "_npc_combats", None)
        if not isinstance(combats, Mapping):
            return False
        combats_map: Mapping[object, object] = cast(Mapping[object, object], combats)
        for uuid_key, string_id_obj in mapping.items():
            if isinstance(string_id_obj, str) and string_id_obj == npc_id and uuid_key in combats_map:
                return True
        return False

    def _npc_registered_in_combat(self, npc_id: str, combat_service: object) -> bool:
        return self._check_npc_combat_via_uuid(npc_id, combat_service) or self._check_npc_combat_via_string_mapping(
            npc_id, combat_service
        )

    def _is_npc_in_combat(self, npc_instance: object) -> bool:
        """
        Check if an NPC is currently in combat.

        Args:
            npc_instance: The NPC instance to check

        Returns:
            bool: True if NPC is in combat, False otherwise
        """
        try:
            npc_id_raw: object | None = cast(object | None, getattr(npc_instance, "npc_id", None))
            if npc_id_raw is None:
                return False
            if isinstance(npc_id_raw, str):
                npc_id = npc_id_raw
            else:
                coerced: object = npc_id_raw
                npc_id = str(coerced)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.debug("Error reading NPC id for combat check", error=str(e))
            return False

        try:
            from ..services.combat_service import get_combat_service

            combat_service = get_combat_service()
            if not combat_service:
                return False
            return self._npc_registered_in_combat(npc_id, combat_service)
        except (ImportError, AttributeError, RuntimeError):
            logger.debug("Combat service not available for combat check")
            return False
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.debug("Error checking NPC combat state", error=str(e))
            return False

    def get_valid_exits(
        self,
        current_room_id: str,
        npc_definition: object,
        _behavior_config: Mapping[str, object],  # pylint: disable=unused-argument  # reserved for future exit filtering
    ) -> dict[str, str]:
        """
        Get exits from current room that stay within subzone boundaries.

        Args:
            current_room_id: ID of the current room
            npc_definition: NPC definition containing subzone information
            behavior_config: Behavior configuration dictionary

        Returns:
            dict[str, str]: Dictionary of direction -> room_id mappings for valid exits
        """
        try:
            all_exits = self.movement_integration.get_available_exits(current_room_id)
            if not all_exits:
                logger.debug("No exits available from room", room_id=current_room_id)
                return {}

            sub_raw: object | None = cast(object | None, getattr(npc_definition, "sub_zone_id", None))
            if not isinstance(sub_raw, str) or not sub_raw:
                defn_id: object = cast(object, getattr(npc_definition, "id", "unknown"))
                defn_id_str = defn_id if isinstance(defn_id, str) else str(defn_id)
                logger.warning("NPC definition missing sub_zone_id", npc_id=defn_id_str)
                return {}

            npc_sub_zone_id: str = sub_raw

            valid_exits: dict[str, str] = {}
            for direction, target_room_id in all_exits.items():
                if self.movement_integration.validate_subzone_boundary(npc_sub_zone_id, target_room_id):
                    valid_exits[direction] = target_room_id
                else:
                    logger.debug(
                        "Exit filtered out due to subzone boundary",
                        direction=direction,
                        target_room_id=target_room_id,
                        npc_sub_zone_id=npc_sub_zone_id,
                    )

            return valid_exits

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error("Error getting valid exits", room_id=current_room_id, error=str(e))
            return {}

    def _calculate_exit_weight(self, target_distance: int, spawn_distance: int) -> float:
        """
        Calculate weight for an exit based on distance from spawn.

        Args:
            target_distance: Distance from target room to spawn
            spawn_distance: Distance from current room to spawn

        Returns:
            Weight value (higher = better)
        """
        distance_diff = target_distance - spawn_distance
        if distance_diff < 0:
            return 1.0
        if not distance_diff:
            return 0.75
        if distance_diff == 1:
            return 0.5
        return 0.25

    def _calculate_exit_weights(
        self, valid_exits: dict[str, str], current_room_id: str, spawn_room_id: str
    ) -> list[tuple[str, str, float]]:
        """
        Calculate weights for all exits.

        Args:
            valid_exits: Dictionary of direction -> room_id mappings
            current_room_id: Current room ID
            spawn_room_id: Spawn room ID

        Returns:
            List of (direction, room_id, weight) tuples
        """
        exit_weights: list[tuple[str, str, float]] = []
        spawn_distance = self._calculate_distance_to_room(current_room_id, spawn_room_id)

        for direction, target_room_id in valid_exits.items():
            target_distance = self._calculate_distance_to_room(target_room_id, spawn_room_id)
            weight = self._calculate_exit_weight(target_distance, spawn_distance)
            exit_weights.append((direction, target_room_id, weight))

        return exit_weights

    def _select_weighted_exit(
        self, exit_weights: list[tuple[str, str, float]], valid_exits: dict[str, str]
    ) -> tuple[str, str] | None:
        """
        Select exit based on weighted probabilities.

        Args:
            exit_weights: List of (direction, room_id, weight) tuples
            valid_exits: Dictionary of direction -> room_id mappings

        Returns:
            (direction, room_id) tuple if selected, None otherwise
        """
        if not exit_weights:
            return None

        total_weight = sum(weight for _, _, weight in exit_weights)
        if not total_weight:
            direction = random.choice(list(valid_exits.keys()))  # nosec B311: game mechanics, not crypto
            return (direction, valid_exits[direction])

        rand = random.random() * total_weight  # nosec B311: game mechanics, not crypto
        cumulative = 0.0
        for direction, room_id, weight in exit_weights:
            cumulative += weight
            if rand <= cumulative:
                return (direction, room_id)

        direction, room_id, _ = exit_weights[-1]
        return (direction, room_id)

    def select_exit(
        self,
        valid_exits: dict[str, str],
        spawn_room_id: str,
        current_room_id: str,
        behavior_config: Mapping[str, object],
    ) -> tuple[str, str] | None:
        """
        Select an exit using weighted random selection favoring exits closer to spawn room.

        Args:
            valid_exits: Dictionary of direction -> room_id mappings
            spawn_room_id: ID of the NPC's spawn room
            current_room_id: ID of the current room
            behavior_config: Behavior configuration dictionary

        Returns:
            tuple[str, str] | None: (direction, room_id) tuple if exit selected, None otherwise
        """
        try:
            if not valid_exits:
                return None

            if len(valid_exits) == 1:
                direction, room_id = next(iter(valid_exits.items()))
                return (direction, room_id)

            weighted_home = _cfg_bool(behavior_config, "idle_movement_weighted_home", True)

            if not weighted_home:
                direction = random.choice(list(valid_exits.keys()))  # nosec B311: game mechanics, not crypto
                return (direction, valid_exits[direction])

            exit_weights = self._calculate_exit_weights(valid_exits, current_room_id, spawn_room_id)
            return self._select_weighted_exit(exit_weights, valid_exits)

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error("Error selecting exit", error=str(e))
            return None

    def _calculate_distance_to_room(self, from_room_id: str, to_room_id: str) -> int:
        """
        Calculate approximate distance between two rooms.

        This is a simplified distance calculation that counts the minimum
        number of room hops needed. For now, it uses a simple heuristic
        based on room ID similarity or performs a basic path search.

        Args:
            from_room_id: Starting room ID
            to_room_id: Target room ID

        Returns:
            int: Approximate distance in room hops (0 if same room, higher for further rooms)
        """
        try:
            if from_room_id == to_room_id:
                return 0

            # Simple heuristic: if rooms are in same subzone, use room ID similarity
            # For more accurate distance, we'd need to do BFS pathfinding
            # For now, we'll use a simple approach: check if rooms share common prefixes
            from_parts = from_room_id.split("_")
            to_parts = to_room_id.split("_")

            # If rooms share the same subzone (first 3 parts: plane_zone_subzone)
            if len(from_parts) >= 3 and len(to_parts) >= 3:
                if from_parts[:3] == to_parts[:3]:
                    # Same subzone - estimate distance based on room name differences
                    # This is a heuristic; for accurate distance, use BFS
                    return abs(len(from_parts) - len(to_parts)) + 1

            # Different subzones or invalid format - return high distance
            return 999

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.debug("Error calculating room distance", error=str(e))
            return 999

    def _log_idle_move_outcome(
        self,
        success: bool,
        npc_instance: object,
        current_room_id: str,
        target_room_id: str,
        direction: str,
    ) -> None:
        nid = _npc_id_str(npc_instance)
        if success:
            logger.info(
                "NPC idle movement executed",
                npc_id=nid,
                from_room=current_room_id,
                to_room=target_room_id,
                direction=direction,
            )
        else:
            logger.warning(
                "NPC idle movement failed",
                npc_id=nid,
                from_room=current_room_id,
                to_room=target_room_id,
            )

    def _try_idle_room_change(
        self,
        npc_instance: object,
        current_room_id: str,
        target_room_id: str,
        direction: str,
    ) -> bool:
        success = self.movement_integration.move_npc_to_room(_npc_id_str(npc_instance), current_room_id, target_room_id)
        self._log_idle_move_outcome(success, npc_instance, current_room_id, target_room_id, direction)
        return success

    def execute_idle_movement(
        self,
        npc_instance: object,
        npc_definition: object,
        behavior_config: Mapping[str, object],
    ) -> bool:
        """
        Execute idle movement for an NPC.

        This method orchestrates the full idle movement process:
        1. Check if movement should occur
        2. Get valid exits within subzone
        3. Select an exit using weighted selection
        4. Execute the movement

        Args:
            npc_instance: The NPC instance to move
            npc_definition: The NPC definition
            behavior_config: Behavior configuration dictionary

        Returns:
            bool: True if movement was executed successfully, False otherwise
        """
        try:
            if not self.should_idle_move(npc_instance, npc_definition, behavior_config):
                return False

            current_room_id = getattr(npc_instance, "current_room", None)
            if not isinstance(current_room_id, str) or not current_room_id:
                logger.warning("NPC has no current room", npc_id=_npc_id_str(npc_instance))
                return False

            spawn_room_id = _resolve_spawn_room(npc_instance, npc_definition, current_room_id)

            valid_exits = self.get_valid_exits(current_room_id, npc_definition, behavior_config)
            if not valid_exits:
                logger.debug("No valid exits for idle movement", npc_id=_npc_id_str(npc_instance))
                return False

            exit_selection = self.select_exit(valid_exits, spawn_room_id, current_room_id, behavior_config)
            if not exit_selection:
                logger.debug("No exit selected for idle movement", npc_id=_npc_id_str(npc_instance))
                return False

            direction, target_room_id = exit_selection
            return self._try_idle_room_change(npc_instance, current_room_id, target_room_id, direction)

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error("Error executing idle movement", npc_id=_npc_id_str(npc_instance), error=str(e))
            return False
