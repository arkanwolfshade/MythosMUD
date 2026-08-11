# NPC Services Bundle

> 46 nodes

## Key Concepts

- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **._search_npcs_in_room()** (8 connections) — `server/services/target_resolution_service.py`
- **PersistenceProtocol** (7 connections) — `server/services/target_resolution_service.py`
- **._gather_room_target_matches()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_players_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **._match_npcs_by_name()** (7 connections) — `server/services/target_resolution_service.py`
- **UUID** (6 connections)
- **.get_room_by_id()** (6 connections) — `server/services/target_resolution_service.py`
- **._get_player_from_persistence()** (6 connections) — `server/services/target_resolution_service.py`
- **._validate_player_and_room()** (6 connections) — `server/services/target_resolution_service.py`
- **._load_npc_ids_with_room_fallback()** (6 connections) — `server/services/target_resolution_service.py`
- **.get_player_by_id()** (5 connections) — `server/services/target_resolution_service.py`
- **Player** (5 connections)
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- **._fetch_players_in_room()** (5 connections) — `server/services/target_resolution_service.py`
- **._add_disambiguation_suffixes()** (5 connections) — `server/services/target_resolution_service.py`
- **._get_npcs_from_lifecycle_manager()** (5 connections) — `server/services/target_resolution_service.py`
- **.get_players_in_room()** (4 connections) — `server/services/target_resolution_service.py`
- **.__init__()** (4 connections) — `server/services/target_resolution_service.py`
- **._validate_room_exists_async()** (4 connections) — `server/services/target_resolution_service.py`
- **._npc_ids_in_room_from_active_map()** (4 connections) — `server/services/target_resolution_service.py`
- **._clean_target_name()** (3 connections) — `server/services/target_resolution_service.py`
- **._validate_room_exists()** (3 connections) — `server/services/target_resolution_service.py`
- **._normalize_name_for_matching()** (3 connections) — `server/services/target_resolution_service.py`
- **Protocol** (2 connections)
- *... and 21 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (25 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (5 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (3 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (1 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (1 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (1 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (1 shared connections)

## Source Files

- `server/services/target_resolution_service.py`

## Audit Trail

- EXTRACTED: 140 (92%)
- INFERRED: 13 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*