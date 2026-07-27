# Admin Command Models

> 68 nodes · cohesion 0.05

## Key Concepts

- **test_command_admin.py** (40 connections) — `server/tests/unit/models/test_command_admin.py`
- **SummonCommand** (21 connections) — `server/models/command_admin.py`
- **TeleportCommand** (18 connections) — `server/models/command_admin.py`
- **GotoCommand** (13 connections) — `server/models/command_admin.py`
- **NPCCommand** (13 connections) — `server/models/command_admin.py`
- **ShutdownCommand** (12 connections) — `server/models/command_admin.py`
- **Test ShutdownCommand can have args.** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **Test SummonCommand validates valid prototype_id.** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_goto_command_player_name_max_length()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_goto_command_player_name_min_length()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_goto_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_goto_command_validate_player_name_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_subcommand_max_length()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_subcommand_min_length()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_with_args()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_with_subcommand()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_shutdown_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_shutdown_command_with_args()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_shutdown_command_with_cancel()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_shutdown_command_with_multiple_args()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_prototype_id_max_length()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_prototype_id_min_length()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_quantity_default()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_quantity_valid_range()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- *... and 43 more nodes in this community*

## Relationships

- [[Base Command Models]] (26 shared connections)
- [[Exploration Command Models]] (7 shared connections)
- [[Moderation Command Models]] (4 shared connections)
- [[Alias Command Models]] (1 shared connections)

## Source Files

- `server/models/command_admin.py`
- `server/tests/unit/models/test_command_admin.py`

## Audit Trail

- EXTRACTED: 239 (94%)
- INFERRED: 15 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
