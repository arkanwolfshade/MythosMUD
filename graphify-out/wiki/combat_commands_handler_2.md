# combat commands handler

> 70 nodes

## Key Concepts

- **TargetResolutionResult** (39 connections) — `server/schemas/shared/target_resolution.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppStatePersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppWithPersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_CmdType** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_as_app_with_state()** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_player()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_no_current_room()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_room()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_success()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_rejects_non_npc()** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_rejects_dead_npc()** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_no_persistence_on_app()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_failure_message()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_target_resolution_result_success()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **test_target_resolution_result_disambiguation()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **test_get_single_match()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **test_get_single_match_none()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **test_get_disambiguation_list()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **test_get_disambiguation_list_empty()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **.get_single_match()** (3 connections) — `server/schemas/shared/target_resolution.py`
- **test_extract_combat_command_data_string_type()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_extract_combat_command_data_enum_value()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_validate_target_name_empty()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- *... and 45 more nodes in this community*

## Relationships

- [spell game magic](spell_game_magic.md) (14 shared connections)
- [NPC Combat](NPC_Combat.md) (11 shared connections)
- [combat commands handler](combat_commands_handler.md) (9 shared connections)
- [calendar models rationale](calendar_models_rationale.md) (9 shared connections)
- [target resolution service](target_resolution_service.md) (6 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (5 shared connections)
- [NATS Messaging](NATS_Messaging.md) (3 shared connections)
- [Item Instances](Item_Instances.md) (3 shared connections)
- [npc population stats](npc_population_stats.md) (1 shared connections)

## Source Files

- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/schemas/test_target_resolution.py`

## Audit Trail

- EXTRACTED: 251 (91%)
- INFERRED: 24 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*