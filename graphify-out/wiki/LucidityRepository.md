# LucidityRepository

> 78 nodes · cohesion 0.04

## Key Concepts

- **test_command_admin.py** (42 connections) — `server/tests/unit/models/test_command_admin.py`
- **SummonCommand** (20 connections) — `server/models/command_admin.py`
- **TeleportCommand** (18 connections) — `server/models/command_admin.py`
- **ShutdownCommand** (11 connections) — `server/models/command_admin.py`
- **.validate_direction_field()** (5 connections) — `server/models/command_admin.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_admin.py`
- **field_validator** (4 connections)
- **.validate_prototype_id()** (4 connections) — `server/models/command_admin.py`
- **.validate_player_name_field()** (4 connections) — `server/models/command_admin.py`
- **test_teleport_command_validate_direction_valid()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_teleport_command_with_direction()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
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
- *... and 53 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (26 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (5 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (3 shared connections)
- [test_look_item_helpers.py](test_look_item_helpers.py.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (2 shared connections)

## Source Files

- `server/models/command_admin.py`
- `server/tests/unit/models/test_command_admin.py`

## Audit Trail

- EXTRACTED: 138 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*