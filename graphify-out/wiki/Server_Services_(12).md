# Server Services (12)

> 100 nodes

## Key Concepts

- **TargetResolutionService** (53 connections) — `server/services/target_resolution_service.py`
- **test_target_resolution_service.py** (27 connections) — `server/tests/unit/services/test_target_resolution_service.py`
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
- **.get_player_by_id()** (5 connections) — `server/services/target_resolution_service.py`
- **Player** (5 connections)
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- **._build_target_result()** (5 connections) — `server/services/target_resolution_service.py`
- **._fetch_players_in_room()** (5 connections) — `server/services/target_resolution_service.py`
- **._add_disambiguation_suffixes()** (5 connections) — `server/services/target_resolution_service.py`
- **._get_npcs_from_lifecycle_manager()** (5 connections) — `server/services/target_resolution_service.py`
- **.get_players_in_room()** (4 connections) — `server/services/target_resolution_service.py`
- **.__init__()** (4 connections) — `server/services/target_resolution_service.py`
- **._validate_room_exists_async()** (4 connections) — `server/services/target_resolution_service.py`
- **._npc_ids_in_room_from_active_map()** (4 connections) — `server/services/target_resolution_service.py`
- *... and 75 more nodes in this community*

## Relationships

- [Server Commands (8)](Server_Commands_%288%29.md) (10 shared connections)
- [Server Game (4)](Server_Game_%284%29.md) (8 shared connections)
- [Server Commands](Server_Commands.md) (8 shared connections)
- [Server Game (2)](Server_Game_%282%29.md) (8 shared connections)
- [Docs Examples](Docs_Examples.md) (3 shared connections)
- [Server Npc (3)](Server_Npc_%283%29.md) (3 shared connections)
- [Server Services (6)](Server_Services_%286%29.md) (2 shared connections)
- [Server Services (9)](Server_Services_%289%29.md) (1 shared connections)
- [Server Services (28)](Server_Services_%2828%29.md) (1 shared connections)
- [Server Api (3)](Server_Api_%283%29.md) (1 shared connections)
- [Server Commands (24)](Server_Commands_%2824%29.md) (1 shared connections)
- [Server Commands (38)](Server_Commands_%2838%29.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 313 (94%)
- INFERRED: 20 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*