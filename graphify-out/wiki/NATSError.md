# NATSError

> 132 nodes

## Key Concepts

- **TargetResolutionService** (51 connections) — `server/services/target_resolution_service.py`
- **test_target_resolution_service.py** (41 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **TargetType** (39 connections) — `server/schemas/shared/target_resolution.py`
- **asyncio** (21 connections)
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **._gather_room_target_matches()** (8 connections) — `server/services/target_resolution_service.py`
- **._search_npcs_in_room()** (8 connections) — `server/services/target_resolution_service.py`
- **PersistenceProtocol** (7 connections) — `server/services/target_resolution_service.py`
- **UUID** (7 connections)
- **._get_player_from_persistence()** (6 connections) — `server/services/target_resolution_service.py`
- **._match_npcs_by_name()** (6 connections) — `server/services/target_resolution_service.py`
- **._search_phantoms_in_room()** (6 connections) — `server/services/target_resolution_service.py`
- **._search_players_in_room()** (6 connections) — `server/services/target_resolution_service.py`
- **._validate_player_and_room()** (6 connections) — `server/services/target_resolution_service.py`
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- **.get_player_by_id()** (5 connections) — `server/services/target_resolution_service.py`
- **.get_room_by_id()** (5 connections) — `server/services/target_resolution_service.py`
- **._add_disambiguation_suffixes()** (5 connections) — `server/services/target_resolution_service.py`
- **._build_target_result()** (5 connections) — `server/services/target_resolution_service.py`
- **._fetch_players_in_room()** (5 connections) — `server/services/target_resolution_service.py`
- **._load_npc_ids_with_room_fallback()** (5 connections) — `server/services/target_resolution_service.py`
- **Player** (5 connections)
- **.get_players_in_room()** (4 connections) — `server/services/target_resolution_service.py`
- **._get_npc_instance()** (4 connections) — `server/services/target_resolution_service.py`
- **._get_npcs_from_lifecycle_manager()** (4 connections) — `server/services/target_resolution_service.py`
- *... and 107 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (14 shared connections)
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) (8 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (8 shared connections)
- [TestErrorHandlers](TestErrorHandlers.md) (5 shared connections)
- [Any](Any.md) (5 shared connections)
- [eventHandlers/types.ts](eventHandlers-types.ts.md) (4 shared connections)
- [migrate_rooms.py](migrate_rooms.py.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [SkillService](SkillService.md) (2 shared connections)
- [inventory_get_command.py](inventory_get_command.py.md) (2 shared connections)

## Source Files

- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 251 (91%)
- INFERRED: 25 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*