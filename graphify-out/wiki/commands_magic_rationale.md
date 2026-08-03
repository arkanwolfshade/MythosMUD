# commands magic rationale

> 12 nodes

## Key Concepts

- **test_magic_commands.py** (49 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **mock_magic_service()** (2 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **mock_player()** (2 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **mock_chat_service()** (2 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **test_handle_cast_command_success()** (2 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **test_handle_spells_command_no_player()** (2 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Unit tests for magic commands.  Tests the /cast, /spells, /spell, /learn, and /s** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Create a mock magic service.** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Create a mock player (healthy by default for cast/combat checks).** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Create a mock chat service.** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Test cast command success.** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Test spells command when player is not found.** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`

## Relationships

- [commands admin mute](commands_admin_mute.md) (7 shared connections)
- [character creation service](character_creation_service.md) (5 shared connections)
- [services ascii map](services_ascii_map.md) (2 shared connections)
- [persistence constants rationale](persistence_constants_rationale.md) (1 shared connections)
- [cache caching lru](cache_caching_lru.md) (1 shared connections)
- [commands admin shutdown](commands_admin_shutdown.md) (1 shared connections)
- [admin shutdown commands](admin_shutdown_commands.md) (1 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (1 shared connections)
- [schemas items item](schemas_items_item.md) (1 shared connections)
- [schemas room schema](schemas_room_schema.md) (1 shared connections)
- [combat npc services](combat_npc_services.md) (1 shared connections)
- [room build realtime](room_build_realtime.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_magic_commands.py`

## Audit Trail

- EXTRACTED: 65 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*