"""
Statistics and reporting helpers for connection manager.

This module provides helper functions for retrieving statistics
and reporting information from the connection manager.
"""

from typing import Any, cast

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def get_player_presence_info_impl(player_id: Any, manager: Any) -> dict[str, Any]:
    """Get detailed presence information for a player."""
    if player_id not in manager.online_players:
        return {
            "player_id": player_id,
            "is_online": False,
            "connection_types": [],
            "total_connections": 0,
            "websocket_connections": 0,
            "connected_at": None,
            "last_seen": None,
        }

    player_info = manager.online_players[player_id]
    websocket_count = len(manager.player_websockets.get(player_id, []))

    return {
        "player_id": player_id,
        "is_online": True,
        "connection_types": list(player_info.get("connection_types", set())),
        "total_connections": player_info.get("total_connections", 0),
        "websocket_connections": websocket_count,
        "connected_at": player_info.get("connected_at"),
        "last_seen": manager.last_seen.get(player_id),
        "player_name": player_info.get("player_name"),
        "current_room_id": player_info.get("current_room_id"),
        "level": player_info.get("level"),
    }


def validate_player_presence_impl(player_id: Any, manager: Any) -> dict[str, Any]:
    """Validate player presence and clean up any inconsistencies."""
    validation_results: dict[str, Any] = {
        "player_id": player_id,
        "is_consistent": True,
        "issues_found": [],
        "actions_taken": [],
    }

    try:
        is_in_online = player_id in manager.online_players
        has_websocket = manager.has_websocket_connection(player_id)
        has_any_connections = has_websocket

        if is_in_online and not has_any_connections:
            validation_results["is_consistent"] = False
            validation_results["issues_found"].append("Player marked as online but has no connections")
            del manager.online_players[player_id]
            validation_results["actions_taken"].append("Removed from online_players")

        elif not is_in_online and has_any_connections:
            validation_results["is_consistent"] = False
            validation_results["issues_found"].append("Player has connections but not marked as online")
            validation_results["actions_taken"].append("Logged inconsistency - should be handled by connection methods")

        if is_in_online:
            player_info = manager.online_players[player_id]
            recorded_count = player_info.get("total_connections", 0)
            actual_count = len(manager.player_websockets.get(player_id, []))

            if recorded_count != actual_count:
                validation_results["is_consistent"] = False
                validation_results["issues_found"].append(
                    f"Connection count mismatch: recorded={recorded_count}, actual={actual_count}"
                )
                player_info["total_connections"] = actual_count
                validation_results["actions_taken"].append("Updated connection count")

    except (AttributeError, ValueError, TypeError) as e:
        validation_results["is_consistent"] = False
        validation_results["issues_found"].append(f"Error during validation: {e}")

    return validation_results


def get_presence_statistics_impl(manager: Any) -> dict[str, Any]:
    """Get presence tracking statistics."""
    total_online = len(manager.online_players)
    total_websockets = sum(len(conns) for conns in manager.player_websockets.values())
    total_connections = total_websockets

    websocket_only = 0
    for player_id in manager.online_players:
        if manager.has_websocket_connection(player_id):
            websocket_only += 1

    return {
        "total_online_players": total_online,
        "total_connections": total_connections,
        "websocket_connections": total_websockets,
        "connection_distribution": {
            "websocket_only": websocket_only,
        },
        "average_connections_per_player": total_connections / total_online if total_online > 0 else 0,
    }


def get_online_player_by_display_name_impl(display_name: str, manager: Any) -> dict[str, Any] | None:
    """Get online player information by display name."""
    display_name_lower = display_name.lower()

    for player_id, player_info in manager.online_players.items():
        if player_info.get("player_name", "").lower() == display_name_lower:
            logger.debug("Found online player", display_name=display_name, player_id=player_id)
            result: dict[str, Any] = cast(dict[str, Any], player_info)
            return result

    logger.debug("Online player not found", display_name=display_name)
    return None


def get_session_stats_impl(manager: Any) -> dict[str, Any]:
    """Get session management statistics."""
    return {
        "total_sessions": len(manager.session_connections),
        "total_players_with_sessions": len(manager.player_sessions),
        "sessions_with_connections": len([s for s in manager.session_connections.values() if s]),
        "average_connections_per_session": (
            sum(len(conns) for conns in manager.session_connections.values()) / len(manager.session_connections)
            if manager.session_connections
            else 0
        ),
    }
