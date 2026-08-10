# NPC Services Bundle

> 138 nodes

## Key Concepts

- **TargetResolutionService** (53 connections) — `server/services/target_resolution_service.py`
- **TargetResolutionResult** (39 connections) — `server/schemas/shared/target_resolution.py`
- **target_resolution_service.py** (27 connections) — `server/services/target_resolution_service.py`
- **test_target_resolution_service.py** (27 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **TargetMetadata** (12 connections) — `server/schemas/shared/target_metadata.py`
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
- **.__init__()** (5 connections) — `server/game/magic/spell_targeting.py`
- **target_metadata.py** (5 connections) — `server/schemas/shared/target_metadata.py`
- **.get_player_by_id()** (5 connections) — `server/services/target_resolution_service.py`
- **Player** (5 connections)
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- **._build_target_result()** (5 connections) — `server/services/target_resolution_service.py`
- **._fetch_players_in_room()** (5 connections) — `server/services/target_resolution_service.py`
- **._add_disambiguation_suffixes()** (5 connections) — `server/services/target_resolution_service.py`
- *... and 113 more nodes in this community*

## Relationships

- [Combat Attack Service](Combat_Attack_Service.md) (20 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (13 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (10 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (7 shared connections)
- [Player Position Service](Player_Position_Service.md) (7 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (7 shared connections)
- [Player Event Handler Tests](Player_Event_Handler_Tests.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [Cursor Skills Harden](Cursor_Skills_Harden.md) (4 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (3 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 459 (93%)
- INFERRED: 34 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*