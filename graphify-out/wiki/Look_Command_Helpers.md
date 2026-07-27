# Look Command Helpers

> 201 nodes · cohesion 0.02

## Key Concepts

- **is_player_in_login_grace_period()** (52 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **test_websocket_room_updates.py** (31 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **websocket_room_updates.py** (29 connections) — `server/realtime/websocket_room_updates.py`
- **is_player_in_grace_period()** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **look_room.py** (24 connections) — `server/commands/look_room.py`
- **broadcast_room_update()** (23 connections) — `server/realtime/websocket_room_updates.py`
- **login_grace_period.py** (22 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period.py** (22 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **get_login_grace_period_remaining()** (21 connections) — `server/realtime/login_grace_period.py`
- **game_state_provider.py** (20 connections) — `server/realtime/integration/game_state_provider.py`
- **test_login_grace_period_visual_indicator.py** (20 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **look_player.py** (19 connections) — `server/commands/look_player.py`
- **test_login_grace_period_flow.py** (17 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **npc_combat_grace.py** (13 connections) — `server/services/npc_combat_grace.py`
- **player_occupant_processor.py** (12 connections) — `server/realtime/player_occupant_processor.py`
- **_grace_period_expiration_handler()** (11 connections) — `server/realtime/login_grace_period.py`
- **get_npc_occupants_from_lifecycle_manager()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **get_player_occupants()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **test_combat_grace_period.py** (10 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **get_npc_occupants_fallback()** (9 connections) — `server/realtime/websocket_room_updates.py`
- **UUID** (9 connections) — `server/realtime/login_grace_period.py`
- **Any** (8 connections) — `server/realtime/login_grace_period.py`
- *... and 176 more nodes in this community*

## Relationships

- [[Disconnect Grace Period]] (18 shared connections)
- [[NPC Admin API]] (16 shared connections)
- [[Room Look Formatting]] (14 shared connections)
- [[Look Player Command]] (11 shared connections)
- [[Room Occupant Events]] (10 shared connections)
- [[NPC Occupant Processor]] (10 shared connections)
- [[Combat Player Broadcasts]] (8 shared connections)
- [[Game State Provider]] (8 shared connections)
- [[Game Tick Processing]] (8 shared connections)
- [[Room Drop Renderer]] (7 shared connections)
- [[Player Respawn Events]] (7 shared connections)
- [[Players API Endpoints]] (7 shared connections)

## Source Files

- `server/commands/look_player.py`
- `server/commands/look_room.py`
- `server/config/__init__.py`
- `server/realtime/disconnect_grace_period.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/login_grace_period.py`
- `server/realtime/player_occupant_processor.py`
- `server/realtime/websocket_room_updates.py`
- `server/services/npc_combat_grace.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`

## Audit Trail

- EXTRACTED: 874 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
