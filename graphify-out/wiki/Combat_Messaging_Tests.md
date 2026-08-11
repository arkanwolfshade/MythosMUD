# Combat Messaging Tests

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

- [Archive Effects System](Archive_Effects_System.md) (7 shared connections)
- [Admin Status Commands](Admin_Status_Commands.md) (7 shared connections)
- [Container Open Events](Container_Open_Events.md) (3 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (3 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)
- [Cursor Skills Harden](Cursor_Skills_Harden.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`

## Audit Trail

- EXTRACTED: 82 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*