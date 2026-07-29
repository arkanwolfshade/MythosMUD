# PlayerRespawnEventHandler

> 49 nodes

## Key Concepts

- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn.py`
- **UUID** (11 connections)
- **.get_player_data_for_respawn()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._prepare_room_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_fallback_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._send_room_occupants_after_respawn()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._enrich_room_data_with_occupant_names()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_current_lucidity()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.update_connection_manager_position()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_delirium_respawn()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._position_from_stats()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._convert_npc_ids_to_names()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._get_npc_name_from_lifecycle_manager()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._merge_player_lists()** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **BoundLogger** (1 connections)
- *... and 24 more nodes in this community*

## Relationships

- [Any](Any.md) (8 shared connections)
- [. init ()](_init_%28%29.md) (4 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (4 shared connections)
- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (4 shared connections)
- [.apply dp change()](apply_dp_change%28%29.md) (4 shared connections)
- [Player](Player.md) (3 shared connections)
- [test player event handlers respawn](test_player_event_handlers_respawn.md) (3 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [TypedDict](TypedDict.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)
- [main()](main%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn.py`

## Audit Trail

- EXTRACTED: 206 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*