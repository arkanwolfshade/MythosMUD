# Look Command Helpers

> 109 nodes

## Key Concepts

- **TargetResolutionService** (53 connections) — `server/services/target_resolution_service.py`
- **TargetResolutionResult** (39 connections) — `server/schemas/shared/target_resolution.py`
- **test_target_resolution_service.py** (27 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **_NpcWithLife** (17 connections) — `server/commands/combat_handler.py`
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **PersistenceProtocol** (7 connections) — `server/services/target_resolution_service.py`
- **._gather_room_target_matches()** (7 connections) — `server/services/target_resolution_service.py`
- **._validate_combat_target_match()** (6 connections) — `server/commands/combat_handler.py`
- **UUID** (6 connections)
- **.get_room_by_id()** (6 connections) — `server/services/target_resolution_service.py`
- **._get_player_from_persistence()** (6 connections) — `server/services/target_resolution_service.py`
- **._validate_player_and_room()** (6 connections) — `server/services/target_resolution_service.py`
- **._load_npc_ids_with_room_fallback()** (6 connections) — `server/services/target_resolution_service.py`
- **.resolve_combat_target()** (5 connections) — `server/commands/combat_handler.py`
- **.get_player_by_id()** (5 connections) — `server/services/target_resolution_service.py`
- **Player** (5 connections)
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- **._build_target_result()** (5 connections) — `server/services/target_resolution_service.py`
- **._fetch_players_in_room()** (5 connections) — `server/services/target_resolution_service.py`
- **._get_npcs_from_lifecycle_manager()** (5 connections) — `server/services/target_resolution_service.py`
- **.get_players_in_room()** (4 connections) — `server/services/target_resolution_service.py`
- **.__init__()** (4 connections) — `server/services/target_resolution_service.py`
- **._validate_room_exists_async()** (4 connections) — `server/services/target_resolution_service.py`
- **._npc_ids_in_room_from_active_map()** (4 connections) — `server/services/target_resolution_service.py`
- **test_resolve_target_player_no_room_id()** (4 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- *... and 84 more nodes in this community*

## Relationships

- [Player Respawn Service](Player_Respawn_Service.md) (27 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (15 shared connections)
- [Client Event Store](Client_Event_Store.md) (11 shared connections)
- [Player Event Handler Tests](Player_Event_Handler_Tests.md) (7 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (7 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (4 shared connections)
- [Character Info Panel Fix](Character_Info_Panel_Fix.md) (3 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (2 shared connections)
- [Cursor Skills Harden](Cursor_Skills_Harden.md) (2 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (1 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 338 (88%)
- INFERRED: 44 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*