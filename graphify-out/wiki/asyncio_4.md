# asyncio

> 56 nodes · cohesion 0.05

## Key Concepts

- **UUID** (18 connections)
- **.send_initial_game_state()** (15 connections) — `server/realtime/integration/game_state_provider.py`
- **Any** (12 connections)
- **._process_occupants_with_grace_periods()** (10 connections) — `server/realtime/integration/game_state_provider.py`
- **.connection_manager()** (10 connections) — `server/realtime/nats_message_handler.py`
- **._get_player_data_for_client()** (9 connections) — `server/realtime/integration/game_state_provider.py`
- **._apply_grace_period_suffixes()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_room_uuids_to_names()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._build_client_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._convert_player_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_fallback_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_following_for_client()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **Player** (6 connections)
- **._get_lucidity_for_client()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_player()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_room_data_with_conversion()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_npcs_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_players_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.__init__()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **._resolve_player_service()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_player_by_id()** (3 connections) — `server/realtime/integration/game_state_provider.py`
- *... and 31 more nodes in this community*

## Relationships

- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (22 shared connections)
- [ChatLogger](ChatLogger.md) (7 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (4 shared connections)
- [alias_storage.py](alias_storage.py.md) (4 shared connections)
- [test_look_npc_helpers.py](test_look_npc_helpers.py.md) (2 shared connections)
- [security.ts](security.ts.md) (2 shared connections)
- [test_async_persistence_room_cache.py](test_async_persistence_room_cache.py.md) (1 shared connections)
- [ItemFactory](ItemFactory.md) (1 shared connections)
- [command_parser.py](command_parser.py.md) (1 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (1 shared connections)
- [required](required.md) (1 shared connections)
- [.publish_with_pool](publish_with_pool.md) (1 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 119 (89%)
- INFERRED: 15 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*