# monitoring dashboard rationale

> 49 nodes

## Key Concepts

- **test_admin_commands_helpers.py** (20 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **notify_player_of_teleport()** (18 connections) — `server/commands/admin_teleport_utils.py`
- **test_admin_teleport_utils.py** (18 connections) — `server/tests/unit/commands/test_admin_teleport_utils.py`
- **broadcast_teleport_effects()** (17 connections) — `server/commands/admin_teleport_utils.py`
- **get_online_player_by_display_name()** (16 connections) — `server/commands/admin_teleport_utils.py`
- **create_teleport_effect_message()** (16 connections) — `server/commands/admin_teleport_utils.py`
- **admin_teleport_utils.py** (14 connections) — `server/commands/admin_teleport_utils.py`
- **Any** (3 connections)
- **test_create_teleport_effect_message_teleport_departure()** (3 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **test_create_teleport_effect_message_teleport_departure_with_direction()** (3 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **test_create_teleport_effect_message_teleport_arrival()** (3 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **test_create_teleport_effect_message_teleport_arrival_with_direction()** (3 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **test_create_teleport_effect_message_goto_departure()** (3 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **test_create_teleport_effect_message_goto_arrival()** (3 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **test_create_teleport_effect_message_goto_arrival_with_direction()** (3 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **test_create_teleport_effect_message_unknown_type()** (3 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **test_direction_opposites()** (2 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **test_get_online_player_by_display_name_no_manager()** (2 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **test_get_online_player_by_display_name_found()** (2 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **test_broadcast_teleport_effects()** (2 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **test_notify_player_of_teleport_custom_message()** (2 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **test_get_online_player_no_connection_manager()** (2 connections) — `server/tests/unit/commands/test_admin_teleport_utils.py`
- **test_get_online_player_found()** (2 connections) — `server/tests/unit/commands/test_admin_teleport_utils.py`
- **test_create_teleport_effect_message()** (2 connections) — `server/tests/unit/commands/test_admin_teleport_utils.py`
- **test_create_teleport_effect_message_fallback()** (2 connections) — `server/tests/unit/commands/test_admin_teleport_utils.py`
- *... and 24 more nodes in this community*

## Relationships

- [npc service services](npc_service_services.md) (15 shared connections)
- [player respawn event](player_respawn_event.md) (5 shared connections)
- [combat services messaging](combat_services_messaging.md) (4 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)

## Source Files

- `server/commands/admin_teleport_utils.py`
- `server/tests/unit/commands/test_admin_commands_helpers.py`
- `server/tests/unit/commands/test_admin_teleport_utils.py`

## Audit Trail

- EXTRACTED: 196 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*