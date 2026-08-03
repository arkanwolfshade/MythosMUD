# target resolution service

> 46 nodes

## Key Concepts

- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **._search_npcs_in_room()** (8 connections) — `server/services/target_resolution_service.py`
- **PersistenceProtocol** (7 connections) — `server/services/target_resolution_service.py`
- **._gather_room_target_matches()** (7 connections) — `server/services/target_resolution_service.py`
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
- **._get_npcs_from_lifecycle_manager()** (5 connections) — `server/services/target_resolution_service.py`
- **._get_npc_instance()** (5 connections) — `server/services/target_resolution_service.py`
- **.get_players_in_room()** (4 connections) — `server/services/target_resolution_service.py`
- **.__init__()** (4 connections) — `server/services/target_resolution_service.py`
- **._validate_room_exists_async()** (4 connections) — `server/services/target_resolution_service.py`
- **._npc_ids_in_room_from_active_map()** (4 connections) — `server/services/target_resolution_service.py`
- **.resolve_player_name()** (3 connections) — `server/services/target_resolution_service.py`
- **._clean_target_name()** (3 connections) — `server/services/target_resolution_service.py`
- **._validate_room_exists()** (3 connections) — `server/services/target_resolution_service.py`
- **._normalize_name_for_matching()** (3 connections) — `server/services/target_resolution_service.py`
- **Protocol** (2 connections)
- *... and 21 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (27 shared connections)
- [spell game magic](spell_game_magic.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)
- [AppRouter main AppRouter()](AppRouter_main_AppRouter%28%29.md) (2 shared connections)
- [command factories exploration](command_factories_exploration.md) (1 shared connections)
- [profession game service](profession_game_service.md) (1 shared connections)
- [event events serialization](event_events_serialization.md) (1 shared connections)

## Source Files

- `server/services/target_resolution_service.py`

## Audit Trail

- EXTRACTED: 136 (91%)
- INFERRED: 13 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*