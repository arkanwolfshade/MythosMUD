# Community 45

> 133 nodes

## Key Concepts

- **TargetResolutionService** (45 connections) — `server/services/target_resolution_service.py`
- **test_target_resolution_service.py** (42 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **asyncio** (21 connections)
- **TargetMetadata** (15 connections) — `server/schemas/shared/target_metadata.py`
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **._gather_room_target_matches()** (8 connections) — `server/services/target_resolution_service.py`
- **._search_npcs_in_room()** (8 connections) — `server/services/target_resolution_service.py`
- **PersistenceProtocol** (7 connections) — `server/services/target_resolution_service.py`
- **._match_npcs_by_name()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_phantoms_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_players_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **UUID** (7 connections)
- **._get_player_from_persistence()** (6 connections) — `server/services/target_resolution_service.py`
- **._load_npc_ids_with_room_fallback()** (6 connections) — `server/services/target_resolution_service.py`
- **._validate_player_and_room()** (6 connections) — `server/services/target_resolution_service.py`
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_targeting.py`
- **.get_room_by_id()** (5 connections) — `server/services/target_resolution_service.py`
- **._add_disambiguation_suffixes()** (5 connections) — `server/services/target_resolution_service.py`
- **._build_target_result()** (5 connections) — `server/services/target_resolution_service.py`
- **._fetch_players_in_room()** (5 connections) — `server/services/target_resolution_service.py`
- **._get_npc_instance()** (5 connections) — `server/services/target_resolution_service.py`
- **._get_npcs_from_lifecycle_manager()** (5 connections) — `server/services/target_resolution_service.py`
- **test_add_disambiguation_suffixes()** (5 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_build_target_result_disambiguation_suffix_match()** (5 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- *... and 108 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (14 shared connections)
- [Magic & Tick Services](Magic_&_Tick_Services.md) (14 shared connections)
- [Community 187](Community_187.md) (8 shared connections)
- [Magic Service Lifespan](Magic_Service_Lifespan.md) (4 shared connections)
- [Community 523](Community_523.md) (2 shared connections)
- [NPC Behavior Engine](NPC_Behavior_Engine.md) (2 shared connections)
- [Community 227](Community_227.md) (1 shared connections)
- [Community 753](Community_753.md) (1 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (1 shared connections)
- [Community 82](Community_82.md) (1 shared connections)
- [Character Creation & Professions](Character_Creation_&_Professions.md) (1 shared connections)
- [Community 1072](Community_1072.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`
- `server/schemas/shared/target_metadata.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 233 (91%)
- INFERRED: 24 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*