# Flee Command Tests

> 127 nodes · cohesion 0.02

## Key Concepts

- **TargetResolutionService** (53 connections) — `server/services/target_resolution_service.py`
- **target_resolution_service.py** (27 connections) — `server/services/target_resolution_service.py`
- **test_target_resolution_service.py** (27 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **TargetMetadata** (12 connections) — `server/schemas/shared/target_metadata.py`
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **._search_npcs_in_room()** (8 connections) — `server/services/target_resolution_service.py`
- **PersistenceProtocol** (7 connections) — `server/services/target_resolution_service.py`
- **._gather_room_target_matches()** (7 connections) — `server/services/target_resolution_service.py`
- **._match_npcs_by_name()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_players_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **.get_room_by_id()** (6 connections) — `server/services/target_resolution_service.py`
- **UUID** (6 connections)
- **._get_player_from_persistence()** (6 connections) — `server/services/target_resolution_service.py`
- **._load_npc_ids_with_room_fallback()** (6 connections) — `server/services/target_resolution_service.py`
- **._validate_player_and_room()** (6 connections) — `server/services/target_resolution_service.py`
- **target_metadata.py** (5 connections) — `server/schemas/shared/target_metadata.py`
- **.get_player_by_id()** (5 connections) — `server/services/target_resolution_service.py`
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- **Player** (5 connections)
- **._add_disambiguation_suffixes()** (5 connections) — `server/services/target_resolution_service.py`
- **._build_target_result()** (5 connections) — `server/services/target_resolution_service.py`
- **._fetch_players_in_room()** (5 connections) — `server/services/target_resolution_service.py`
- **._get_npc_instance()** (5 connections) — `server/services/target_resolution_service.py`
- **._get_npcs_from_lifecycle_manager()** (5 connections) — `server/services/target_resolution_service.py`
- *... and 102 more nodes in this community*

## Relationships

- [Combat Command Handler](Combat_Command_Handler.md) (25 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (17 shared connections)
- [Room Planning Archive](Room_Planning_Archive.md) (7 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (6 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (6 shared connections)
- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (5 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (3 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (2 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (2 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (2 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (2 shared connections)
- [Character Creation API](Character_Creation_API.md) (2 shared connections)

## Source Files

- `server/schemas/shared/target_metadata.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 411 (94%)
- INFERRED: 25 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*