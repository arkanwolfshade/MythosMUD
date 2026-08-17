# server schemas shared target metadata

> 125 nodes

## Key Concepts

- **TargetResolutionService** (50 connections) — `server/services/target_resolution_service.py`
- **test_target_resolution_service.py** (41 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **asyncio** (21 connections)
- **TargetMetadata** (14 connections) — `server/schemas/shared/target_metadata.py`
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **._search_npcs_in_room()** (8 connections) — `server/services/target_resolution_service.py`
- **PersistenceProtocol** (7 connections) — `server/services/target_resolution_service.py`
- **._gather_room_target_matches()** (7 connections) — `server/services/target_resolution_service.py`
- **._match_npcs_by_name()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_players_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **.get_room_by_id()** (6 connections) — `server/services/target_resolution_service.py`
- **._get_player_from_persistence()** (6 connections) — `server/services/target_resolution_service.py`
- **._load_npc_ids_with_room_fallback()** (6 connections) — `server/services/target_resolution_service.py`
- **._validate_player_and_room()** (6 connections) — `server/services/target_resolution_service.py`
- **UUID** (6 connections)
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- **.get_player_by_id()** (5 connections) — `server/services/target_resolution_service.py`
- **._add_disambiguation_suffixes()** (5 connections) — `server/services/target_resolution_service.py`
- **._build_target_result()** (5 connections) — `server/services/target_resolution_service.py`
- **._fetch_players_in_room()** (5 connections) — `server/services/target_resolution_service.py`
- **._get_npc_instance()** (5 connections) — `server/services/target_resolution_service.py`
- **._get_npcs_from_lifecycle_manager()** (5 connections) — `server/services/target_resolution_service.py`
- **test_add_disambiguation_suffixes()** (5 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_build_target_result_disambiguation_suffix_match()** (5 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_build_target_result_single_match()** (5 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- *... and 100 more nodes in this community*

## Relationships

- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (11 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (8 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (7 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (5 shared connections)
- [server commands party commands](server_commands_party_commands.md) (3 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (3 shared connections)
- [server app lifespan magic](server_app_lifespan_magic.md) (2 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (2 shared connections)
- [server commands follow commands](server_commands_follow_commands.md) (2 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (2 shared connections)

## Source Files

- `server/schemas/shared/target_metadata.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 216 (86%)
- INFERRED: 34 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*