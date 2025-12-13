"""
Combat cleanup and management logic.

Handles combat cleanup, tracking, and end-of-combat operations.
"""

from datetime import UTC, datetime, timedelta

from server.logging.enhanced_logging_config import get_logger
from server.models.combat import CombatInstance
from server.services.nats_exceptions import NATSError

logger = get_logger(__name__)


class CombatCleanupHandler:
    """Handles combat cleanup and tracking operations."""

    def __init__(self, combat_service):
        """
        Initialize the cleanup handler.

        Args:
            combat_service: Reference to the parent CombatService
        """
        self._combat_service = combat_service

    def cleanup_combat_tracking(self, combat: CombatInstance) -> None:
        """Remove combat from tracking dictionaries."""
        active_combats = getattr(self._combat_service, "_active_combats", {})
        player_combats = getattr(self._combat_service, "_player_combats", {})
        npc_combats = getattr(self._combat_service, "_npc_combats", {})

        for participant_id in combat.participants.keys():
            player_combats.pop(participant_id, None)
            npc_combats.pop(participant_id, None)
        active_combats.pop(combat.combat_id, None)

    def check_connection_state(self, room_id: str) -> None:
        """Check connection state before publishing combat ended event."""
        try:
            from ..container import ApplicationContainer

            container = ApplicationContainer.get_instance()
            connection_manager = getattr(container, "connection_manager", None) if container else None
            if connection_manager is not None:
                canonical_room_id = connection_manager.canonical_room_id(room_id) or room_id
                room_subscribers = connection_manager.room_subscriptions.get(canonical_room_id, set())
                logger.debug(
                    "Connection state check before combat ended event",
                    room_id=room_id,
                    canonical_room_id=canonical_room_id,
                    connected_players_count=len(room_subscribers),
                    connected_player_ids=list(room_subscribers),
                )
        except (
            ImportError,
            AttributeError,
            ValueError,
            TypeError,
            RuntimeError,
            NATSError,
            ConnectionError,
            KeyError,
        ) as conn_check_error:
            logger.warning(
                "Could not check connection state before combat ended event",
                error=str(conn_check_error),
                room_id=room_id,
            )

    async def cleanup_stale_combats(self, combat_timeout_minutes: int) -> int:
        """
        Clean up combats that have been inactive for too long.

        Args:
            combat_timeout_minutes: Timeout in minutes for inactive combats

        Returns:
            Number of combats cleaned up
        """
        cutoff_time = datetime.now(UTC) - timedelta(minutes=combat_timeout_minutes)
        active_combats = getattr(self._combat_service, "_active_combats", {})
        stale_combats = []

        for combat_id, combat in active_combats.items():
            if combat.last_activity < cutoff_time:
                stale_combats.append(combat_id)

        end_combat_method = getattr(self._combat_service, "end_combat", None)
        if end_combat_method:
            for combat_id in stale_combats:
                await end_combat_method(combat_id, "Combat timeout - no activity")
                logger.info("Cleaned up stale combat", combat_id=combat_id)

        return len(stale_combats)
