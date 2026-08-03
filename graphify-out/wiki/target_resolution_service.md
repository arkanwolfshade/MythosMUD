# target resolution service

> 102 nodes

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
- *... and 77 more nodes in this community*

## Relationships

- [Magic Spell Service](Magic_Spell_Service.md) (7 shared connections)
- [NATS Messaging](NATS_Messaging.md) (7 shared connections)
- [combat commands handler](combat_commands_handler.md) (7 shared connections)
- [spell game magic](spell_game_magic.md) (6 shared connections)
- [NPC Combat](NPC_Combat.md) (5 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (4 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (3 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (2 shared connections)
- [calendar models rationale](calendar_models_rationale.md) (2 shared connections)
- [Item Instances](Item_Instances.md) (1 shared connections)
- [combat services rationale](combat_services_rationale.md) (1 shared connections)
- [Player Stats](Player_Stats.md) (1 shared connections)

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