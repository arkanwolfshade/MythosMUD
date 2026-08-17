# asyncio

> 19 nodes

## Key Concepts

- **asyncio** (21 connections)
- **test_get_npc_instance_not_found()** (4 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_resolve_target_persistence_no_methods()** (4 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_resolve_target_string_player_id()** (4 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_search_npcs_in_room_no_match()** (4 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_search_players_in_room_no_match()** (4 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_resolve_target_multiple_matches()** (3 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_resolve_target_no_matches()** (3 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_resolve_target_sync_get_player_by_id()** (3 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_validate_room_exists_async()** (3 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Test _search_players_in_room() with no matching players.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Test _search_npcs_in_room() with no matching NPCs.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Test _get_npc_instance() when NPC not found.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Test resolve_target() with string player_id.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Test resolve_target() handles sync get_player_by_id.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Test resolve_target() when no matches found.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Test resolve_target() with multiple matches requires disambiguation.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Async get_room_by_id validates room presence.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Test resolve_target() when persistence has no get methods.** (1 connections) — `server/tests/unit/services/test_target_resolution_service.py`

## Relationships

- [test_target_resolution_service.py](test_target_resolution_service.py.md) (9 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (5 shared connections)
- [test_resolve_target_empty_target_name](test_resolve_target_empty_target_name.md) (1 shared connections)
- [test_resolve_target_no_persistence_methods](test_resolve_target_no_persistence_methods.md) (1 shared connections)
- [test_resolve_target_no_room](test_resolve_target_no_room.md) (1 shared connections)
- [test_resolve_target_player_no_room_id](test_resolve_target_player_no_room_id.md) (1 shared connections)
- [test_resolve_target_player_not_found](test_resolve_target_player_not_found.md) (1 shared connections)
- [test_resolve_target_single_match](test_resolve_target_single_match.md) (1 shared connections)
- [test_resolve_target_uses_get_player_fallback](test_resolve_target_uses_get_player_fallback.md) (1 shared connections)
- [test_resolve_target_whitespace_target_name](test_resolve_target_whitespace_target_name.md) (1 shared connections)
- [test_resolve_target_with_disambiguation_suffix](test_resolve_target_with_disambiguation_suffix.md) (1 shared connections)
- [test_search_npcs_in_room_empty_list](test_search_npcs_in_room_empty_list.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 39 (89%)
- INFERRED: 5 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*