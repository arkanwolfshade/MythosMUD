# Test Target Resolution Service

> 143 nodes

## Key Concepts

- **TargetResolutionService** (51 connections) — `server/services/target_resolution_service.py`
- **test_target_resolution_service.py** (43 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **target_resolution_service.py** (29 connections) — `server/services/target_resolution_service.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **asyncio** (21 connections)
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **TargetMetadata** (15 connections) — `server/schemas/shared/target_metadata.py`
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **._gather_room_target_matches()** (8 connections) — `server/services/target_resolution_service.py`
- **._search_npcs_in_room()** (8 connections) — `server/services/target_resolution_service.py`
- **PersistenceProtocol** (7 connections) — `server/services/target_resolution_service.py`
- **._match_npcs_by_name()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_phantoms_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_players_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **UUID** (7 connections)
- **.get_room_by_id()** (6 connections) — `server/services/target_resolution_service.py`
- **._get_player_from_persistence()** (6 connections) — `server/services/target_resolution_service.py`
- **._load_npc_ids_with_room_fallback()** (6 connections) — `server/services/target_resolution_service.py`
- **._validate_player_and_room()** (6 connections) — `server/services/target_resolution_service.py`
- **target_metadata.py** (6 connections) — `server/schemas/shared/target_metadata.py`
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- **._add_disambiguation_suffixes()** (5 connections) — `server/services/target_resolution_service.py`
- **._build_target_result()** (5 connections) — `server/services/target_resolution_service.py`
- **._fetch_players_in_room()** (5 connections) — `server/services/target_resolution_service.py`
- **._get_npc_instance()** (5 connections) — `server/services/target_resolution_service.py`
- *... and 118 more nodes in this community*

## Relationships

- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (26 shared connections)
- [Test Combat Handler](Test_Combat_Handler.md) (17 shared connections)
- [Lifespan Magic](Lifespan_Magic.md) (10 shared connections)
- [Test Party Commands](Test_Party_Commands.md) (5 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (5 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (4 shared connections)
- [Test Player Schemas](Test_Player_Schemas.md) (3 shared connections)
- [Test Follow Commands](Test_Follow_Commands.md) (3 shared connections)
- [Test Teach Command](Test_Teach_Command.md) (3 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (3 shared connections)
- [Test Spell](Test_Spell.md) (3 shared connections)
- [Npc Base](Npc_Base.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`
- `server/schemas/shared/target_metadata.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 302 (92%)
- INFERRED: 26 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*