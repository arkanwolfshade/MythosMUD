# admin commands setstat

> 21 nodes

## Key Concepts

- **admin_setstat_command.py** (28 connections) — `server/commands/admin_setstat_command.py`
- **Any** (7 connections)
- **_calculate_stat_warnings()** (6 connections) — `server/commands/admin_setstat_command.py`
- **_parse_set_stat_args()** (5 connections) — `server/commands/admin_setstat_command.py`
- **_notify_player_stat_change()** (5 connections) — `server/commands/admin_setstat_command.py`
- **_resolve_admin_services_and_permissions()** (5 connections) — `server/commands/admin_setstat_command.py`
- **_warning_for_cap_stat()** (4 connections) — `server/commands/admin_setstat_command.py`
- **_get_app_or_error()** (4 connections) — `server/commands/admin_setstat_command.py`
- **_parse_value_from_args()** (3 connections) — `server/commands/admin_setstat_command.py`
- **_validate_set_stat_inputs()** (3 connections) — `server/commands/admin_setstat_command.py`
- **_warning_for_stat_range()** (3 connections) — `server/commands/admin_setstat_command.py`
- **Admin command to set player statistics.  This module provides the handler for th** (1 connections) — `server/commands/admin_setstat_command.py`
- **Parse value from args[2] when value_input is None and args has at least 3 elemen** (1 connections) — `server/commands/admin_setstat_command.py`
- **Parse stat name, target player, and value from command data.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Validate stat name and value inputs.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Return warning message if value exceeds DP or MP calculated maximum; else empty** (1 connections) — `server/commands/admin_setstat_command.py`
- **Return warning message if value is outside normal range for stat; else empty str** (1 connections) — `server/commands/admin_setstat_command.py`
- **Calculate warnings for stat values that exceed maximums or normal ranges.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Notify target player of stat change and send player update event.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Resolve required services and check admin permissions.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Return (app, None) if request has app, else (None, error_dict).** (1 connections) — `server/commands/admin_setstat_command.py`

## Relationships

- [command processor rationale](command_processor_rationale.md) (7 shared connections)
- [admin command setstat](admin_command_setstat.md) (7 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [combat services turn](combat_services_turn.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [npc populate databases](npc_populate_databases.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`

## Audit Trail

- EXTRACTED: 82 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*