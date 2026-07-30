# test npc instance service

> 20 nodes

## Key Concepts

- **test_alias.py** (29 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_repr()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_equality_same_name_and_command()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_equality_with_non_alias()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_hash_usable_in_set()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_is_reserved_command_true()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_is_reserved_command_false()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_validate_name_whitespace_only()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_get_expanded_command_no_args()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_model_dump_timestamps_isoformat()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **Unit tests for the Alias model.  Tests the Alias model methods including validat** (1 connections) — `server/tests/unit/models/test_alias.py`
- **Test __repr__ returns expected string format.** (1 connections) — `server/tests/unit/models/test_alias.py`
- **Test __eq__ returns True for aliases with same name and command.** (1 connections) — `server/tests/unit/models/test_alias.py`
- **Test __eq__ returns False when comparing with non-Alias object.** (1 connections) — `server/tests/unit/models/test_alias.py`
- **Test __hash__ allows aliases to be used in sets.** (1 connections) — `server/tests/unit/models/test_alias.py`
- **Test is_reserved_command returns True for reserved command names.** (1 connections) — `server/tests/unit/models/test_alias.py`
- **Test is_reserved_command returns False for non-reserved names.** (1 connections) — `server/tests/unit/models/test_alias.py`
- **Test validate_name returns False for whitespace-only name.** (1 connections) — `server/tests/unit/models/test_alias.py`
- **Test get_expanded_command returns command as-is when no args.** (1 connections) — `server/tests/unit/models/test_alias.py`
- **Test model_dump returns timestamps in ISO format with Z suffix.** (1 connections) — `server/tests/unit/models/test_alias.py`

## Relationships

- [command parser()](command_parser%28%29.md) (10 shared connections)
- [test alias storage](test_alias_storage.md) (1 shared connections)
- [test_load_player_mutes_file_not_exists](test_load_player_mutes_file_not_exists.md) (1 shared connections)
- [Test handle npc died event](Test_handle_npc_died_event.md) (1 shared connections)
- [test_unmute_player_not_found](test_unmute_player_not_found.md) (1 shared connections)
- [test_normalize_to_uuid_invalid](test_normalize_to_uuid_invalid.md) (1 shared connections)
- [Test unsubscribe from subzone handles](Test_unsubscribe_from_subzone_handles.md) (1 shared connections)
- [Test validate event message delegates](Test_validate_event_message_delegates.md) (1 shared connections)
- [test_is_channel_muted_true](test_is_channel_muted_true.md) (1 shared connections)
- [test_create_pose_command](test_create_pose_command.md) (1 shared connections)
- [test_create_spells_command](test_create_spells_command.md) (1 shared connections)
- [test_is_admin_sync_false](test_is_admin_sync_false.md) (1 shared connections)

## Source Files

- `server/tests/unit/models/test_alias.py`

## Audit Trail

- EXTRACTED: 66 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*