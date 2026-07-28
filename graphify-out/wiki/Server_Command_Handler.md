# Server Command Handler

> 29 nodes

## Key Concepts

- **catatonia_check.py** (25 connections) — `server/command_handler/catatonia_check.py`
- **test_command_validation.py** (22 connections) — `server/tests/unit/commands/test_command_validation.py`
- **check_catatonia_block()** (17 connections) — `server/command_handler/catatonia_check.py`
- **_load_player_for_catatonia_check()** (11 connections) — `server/command_handler/catatonia_check.py`
- **_is_catatonic()** (10 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_registry()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_query_lucidity_record()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_database()** (9 connections) — `server/command_handler/catatonia_check.py`
- **UUID** (8 connections)
- **_fetch_lucidity_record()** (8 connections) — `server/command_handler/catatonia_check.py`
- **_registry_player_id_value()** (7 connections) — `server/command_handler/catatonia_check.py`
- **_PersistenceGetPlayerByName** (6 connections) — `server/command_handler/catatonia_check.py`
- **_convert_player_id_to_uuid()** (4 connections) — `server/command_handler/catatonia_check.py`
- **CommandExecutionRequest** (3 connections)
- **.get_player_by_name()** (2 connections) — `server/command_handler/catatonia_check.py`
- **AsyncSession** (2 connections)
- **Protocol** (1 connections)
- **Catatonia Checking Logic for MythosMUD.  This module handles checking whether** (1 connections) — `server/command_handler/catatonia_check.py`
- **Minimal persistence surface used by catatonia load path.** (1 connections) — `server/command_handler/catatonia_check.py`
- **Load player for catatonia check, using cache if available.** (1 connections) — `server/command_handler/catatonia_check.py`
- **Normalize player_id for CatatoniaRegistry.is_catatonic (uuid.UUID | str).** (1 connections) — `server/command_handler/catatonia_check.py`
- **Check catatonia status via registry.** (1 connections) — `server/command_handler/catatonia_check.py`
- **Check if player is catatonic based on lucidity record.** (1 connections) — `server/command_handler/catatonia_check.py`
- **Fetch lucidity record from database session.** (1 connections) — `server/command_handler/catatonia_check.py`
- **Query lucidity record from database with error handling.** (1 connections) — `server/command_handler/catatonia_check.py`
- *... and 4 more nodes in this community*

## Relationships

- [Server Commands (31)](Server_Commands_%2831%29.md) (20 shared connections)
- [Server Commands (3)](Server_Commands_%283%29.md) (15 shared connections)
- [Server Commands (5)](Server_Commands_%285%29.md) (5 shared connections)
- [Server Services](Server_Services.md) (5 shared connections)
- [Server Utils (19)](Server_Utils_%2819%29.md) (5 shared connections)
- [Server Admin](Server_Admin.md) (3 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Services (30)](Server_Services_%2830%29.md) (1 shared connections)
- [Server Commands (83)](Server_Commands_%2883%29.md) (1 shared connections)

## Source Files

- `server/command_handler/catatonia_check.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 159 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*