# test_user_manager.py

> 122 nodes · cohesion 0.03

## Key Concepts

- **TargetResolutionService** (52 connections) — `server/services/target_resolution_service.py`
- **test_target_resolution_service.py** (42 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **asyncio** (21 connections)
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **._gather_room_target_matches()** (8 connections) — `server/services/target_resolution_service.py`
- **._search_npcs_in_room()** (8 connections) — `server/services/target_resolution_service.py`
- **PersistenceProtocol** (7 connections) — `server/services/target_resolution_service.py`
- **UUID** (7 connections)
- **._match_npcs_by_name()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_phantoms_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_players_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **._get_player_from_persistence()** (6 connections) — `server/services/target_resolution_service.py`
- **._load_npc_ids_with_room_fallback()** (6 connections) — `server/services/target_resolution_service.py`
- **._validate_player_and_room()** (6 connections) — `server/services/target_resolution_service.py`
- **.get_room_by_id()** (5 connections) — `server/services/target_resolution_service.py`
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- **Player** (5 connections)
- **._add_disambiguation_suffixes()** (5 connections) — `server/services/target_resolution_service.py`
- **._build_target_result()** (5 connections) — `server/services/target_resolution_service.py`
- **._fetch_players_in_room()** (5 connections) — `server/services/target_resolution_service.py`
- **._get_npc_instance()** (5 connections) — `server/services/target_resolution_service.py`
- **._get_npcs_from_lifecycle_manager()** (5 connections) — `server/services/target_resolution_service.py`
- **.get_player_by_id()** (4 connections) — `server/services/target_resolution_service.py`
- **.get_players_in_room()** (4 connections) — `server/services/target_resolution_service.py`
- **.__init__()** (4 connections) — `server/services/target_resolution_service.py`
- *... and 97 more nodes in this community*

## Relationships

- [PlayerPositionService](PlayerPositionService.md) (15 shared connections)
- [RoomService](RoomService.md) (8 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (6 shared connections)
- [test_event_bus_lifecycle.py](test_event_bus_lifecycle.py.md) (3 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (3 shared connections)
- [MemoryThresholdMonitor](MemoryThresholdMonitor.md) (2 shared connections)
- [.claude/hooks/record_edited_file.py](claude-hooks-record_edited_file.py.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)
- [command_parser.py](command_parser.py.md) (2 shared connections)
- [BaseEvent](BaseEvent.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (1 shared connections)

## Source Files

- `server/services/target_resolution_service.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 219 (91%)
- INFERRED: 21 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*