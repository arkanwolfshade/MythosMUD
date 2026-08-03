# emote game service

> 29 nodes

## Key Concepts

- **player_disconnect_handlers.py** (27 connections) — `server/realtime/player_disconnect_handlers.py`
- **_cleanup_player_references()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **age_off_disconnected_sessions()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **_remove_player_from_online_tracking()** (10 connections) — `server/realtime/player_disconnect_handlers.py`
- **UUID** (7 connections)
- **_get_session_maps_for_age_off()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **_purge_expired_sessions_from_maps()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **_session_ids_past_age_off()** (3 connections) — `server/realtime/player_disconnect_handlers.py`
- **test_remove_player_from_online_tracking()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_remove_player_from_online_tracking_not_in_online_players()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_cleanup_player_references()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_cleanup_player_references_partial_cleanup()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_cleanup_player_references_marks_session_for_aging()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_age_off_disconnected_sessions_removes_expired()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_age_off_disconnected_sessions_keeps_recent()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **Player disconnect handling functions.  This module handles broadcasting discon** (1 connections) — `server/realtime/player_disconnect_handlers.py`
- **Remove player from online tracking and room presence.      Args:         keys** (1 connections) — `server/realtime/player_disconnect_handlers.py`
- **Clean up all remaining player references.      Args:         player_id: The p** (1 connections) — `server/realtime/player_disconnect_handlers.py`
- **Return typed session maps for age-off, or None if the manager is not ready.** (1 connections) — `server/realtime/player_disconnect_handlers.py`
- **Session ids whose disconnect timestamp is older than SESSION_AGE_OFF_SECONDS.** (1 connections) — `server/realtime/player_disconnect_handlers.py`
- **Remove expired session ids from disconnect_times, connections, and player_sessio** (1 connections) — `server/realtime/player_disconnect_handlers.py`
- **Remove sessions that have been disconnected for more than SESSION_AGE_OFF_SECOND** (1 connections) — `server/realtime/player_disconnect_handlers.py`
- **Test _remove_player_from_online_tracking removes player.** (1 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **Test _remove_player_from_online_tracking handles player not in online_players.** (1 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **Test _cleanup_player_references cleans up all references.** (1 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- *... and 4 more nodes in this community*

## Relationships

- [player disconnect handlers](player_disconnect_handlers.md) (16 shared connections)
- [look helpers commands](look_helpers_commands.md) (5 shared connections)
- [player presence tracker](player_presence_tracker.md) (5 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [container service services](container_service_services.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (2 shared connections)
- [help content websocket](help_content_websocket.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [room models instance](room_models_instance.md) (1 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)

## Source Files

- `server/realtime/player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`

## Audit Trail

- EXTRACTED: 107 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*