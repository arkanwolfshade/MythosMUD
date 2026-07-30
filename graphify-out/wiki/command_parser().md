# command parser()

> 23 nodes

## Key Concepts

- **Alias** (52 connections) — `server/models/alias.py`
- **sample_alias()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **sample_alias2()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_add_alias_updates_existing()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_add_alias_case_insensitive()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **.__repr__()** (2 connections) — `server/models/alias.py`
- **.__eq__()** (2 connections) — `server/models/alias.py`
- **.update_timestamp()** (2 connections) — `server/models/alias.py`
- **.is_reserved_command()** (2 connections) — `server/models/alias.py`
- **.validate_name()** (2 connections) — `server/models/alias.py`
- **.get_expanded_command()** (2 connections) — `server/models/alias.py`
- **BaseModel** (1 connections)
- **Alias model for command aliases.      Stores player command aliases for quick ac** (1 connections) — `server/models/alias.py`
- **String representation of the alias.** (1 connections) — `server/models/alias.py`
- **Check equality based on name and command.** (1 connections) — `server/models/alias.py`
- **Update the updated_at timestamp to current time.** (1 connections) — `server/models/alias.py`
- **Check if the alias name conflicts with a reserved command.** (1 connections) — `server/models/alias.py`
- **Validate the alias name is not empty.** (1 connections) — `server/models/alias.py`
- **Get the expanded command with optional arguments appended.** (1 connections) — `server/models/alias.py`
- **Create a sample alias for testing.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Create another sample alias for testing.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test add_alias updates existing alias.** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Test add_alias is case-insensitive for alias names.** (1 connections) — `server/tests/unit/test_alias_storage.py`

## Relationships

- [test npc instance service](test_npc_instance_service.md) (10 shared connections)
- [test alias storage](test_alias_storage.md) (6 shared connections)
- [Any](Any.md) (5 shared connections)
- [Player](Player.md) (2 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [Test validate chat message fields](Test_validate_chat_message_fields.md) (1 shared connections)
- [test_room_service_init](test_room_service_init.md) (1 shared connections)
- [test_load_player_mutes_file_not_exists](test_load_player_mutes_file_not_exists.md) (1 shared connections)
- [Test handle npc died event](Test_handle_npc_died_event.md) (1 shared connections)
- [test_unmute_player_not_found](test_unmute_player_not_found.md) (1 shared connections)
- [test_normalize_to_uuid_invalid](test_normalize_to_uuid_invalid.md) (1 shared connections)
- [Test unsubscribe from subzone handles](Test_unsubscribe_from_subzone_handles.md) (1 shared connections)

## Source Files

- `server/models/alias.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 84 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*