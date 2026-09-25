"""
Inventory WebSocket event emission.

Pushes the player's current inventory/equipped state to their own connection
after a mutation, so a graphical inventory panel can stay in sync without
polling the 'inventory' text command. Mirrors the container.* event helpers
in container_websocket_events.py.
"""

from __future__ import annotations

from typing import Protocol, cast
from uuid import UUID

from ..realtime.envelope import build_event
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class _InventoryOwner(Protocol):
    """Minimal shape emit_inventory_updated needs from a player."""

    def get_inventory(self) -> list[dict[str, object]]:
        """Return the player's carried inventory stacks."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body (not just a docstring) for a non-None Protocol return type

    def get_equipped_items(self) -> dict[str, object]:
        """Return the player's equipped-slot items."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body (not just a docstring) for a non-None Protocol return type


class _ConnectionManagerLike(Protocol):
    """Minimal shape emit_inventory_updated needs from a connection manager.

    sequence_counter is required so this satisfies build_event's own
    _SupportsEventSequence protocol.
    """

    sequence_counter: int

    async def send_personal_message(self, player_id: UUID, event: dict[str, object]) -> dict[str, object]:
        """Send event to a single player; returns delivery status."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body (not just a docstring) for a non-None Protocol return type


async def emit_inventory_updated(
    connection_manager: object,
    player_id: UUID,
    player: _InventoryOwner,
) -> None:
    """
    Emit inventory_updated to the player personally.

    connection_manager is typed as object (matching the command layer's own
    duck-typed style, e.g. inventory_command_helpers.build_and_broadcast_inventory_event)
    since callers pass it through untyped from command handler plumbing.

    Best-effort: emission failures are logged and swallowed so they never fail
    the command that triggered the mutation.
    """
    if connection_manager is None:
        return
    try:
        cm = cast(_ConnectionManagerLike, connection_manager)
        event_data: dict[str, object] = {
            "inventory": player.get_inventory(),
            "equipped": player.get_equipped_items(),
        }
        event = build_event(
            event_type="inventory_updated",
            data=event_data,
            player_id=player_id,
            connection_manager=cm,
        )
        _ = await cm.send_personal_message(player_id, event)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event emission errors unpredictable, must not fail the triggering command
        logger.warning(
            "Failed to emit inventory_updated event",
            error=str(e),
            player_id=str(player_id),
        )
