# EventBus

> 89 nodes

## Key Concepts

- **test_look_player.py** (33 connections) — `server/tests/unit/commands/test_look_player.py`
- **look_player.py** (26 connections) — `server/commands/look_player.py`
- **_format_player_look_display()** (22 connections) — `server/commands/look_player.py`
- **_select_target_player()** (17 connections) — `server/commands/look_player.py`
- **asyncio** (13 connections)
- **test_look_player_helpers.py** (12 connections) — `server/tests/unit/commands/test_look_player_helpers.py`
- **_handle_player_look()** (11 connections) — `server/commands/look_player.py`
- **_try_lookup_player_implicit()** (10 connections) — `server/commands/look_player.py`
- **_find_matching_players()** (9 connections) — `server/commands/look_player.py`
- **_get_players_in_room()** (9 connections) — `server/commands/look_player.py`
- **Any** (8 connections)
- **_apply_grace_period_labels()** (6 connections) — `server/commands/look_player.py`
- **_player_id_uuid()** (4 connections) — `server/commands/look_player.py`
- **test_find_matching_players_no_match()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_find_matching_players_success()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_empty()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_invalid_uuid()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_non_iterable()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_success()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_handle_player_look_multiple_matches()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_handle_player_look_not_found()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_handle_player_look_success()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_handle_player_look_with_instance_number()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_try_lookup_player_implicit_multiple_matches()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_try_lookup_player_implicit_not_found()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- *... and 64 more nodes in this community*

## Relationships

- [NPCCombatUUIDMapping](NPCCombatUUIDMapping.md) (7 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (6 shared connections)
- [.claude/hooks/record_edited_file.py](claude-hooks-record_edited_file.py.md) (4 shared connections)
- [character-cleanup.ts](character-cleanup.ts.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (1 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (1 shared connections)
- [test_manager.py](test_manager.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/commands/look_player.py`
- `server/tests/unit/commands/test_look_player.py`
- `server/tests/unit/commands/test_look_player_helpers.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 183 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*