# commands npc admin

> 47 nodes

## Key Concepts

- **get_npc_instance_service()** (79 connections) — `server/services/npc_instance_service.py`
- **router.py** (30 connections) — `server/commands/npc_admin/router.py`
- **__init__.py** (24 connections) — `server/commands/npc_admin/__init__.py`
- **npc_admin_commands.py** (21 connections) — `server/commands/npc_admin_commands.py`
- **_build_subcommand_map()** (20 connections) — `server/commands/npc_admin/router.py`
- **handle_npc_command()** (16 connections) — `server/commands/npc_admin/router.py`
- **behavior.py** (11 connections) — `server/commands/npc_admin/behavior.py`
- **monitoring.py** (11 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_move_command()** (10 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_stats_command()** (10 connections) — `server/commands/npc_admin/instance.py`
- **handle_npc_behavior_command()** (9 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_react_command()** (9 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_stop_command()** (9 connections) — `server/commands/npc_admin/behavior.py`
- **handle_npc_population_command()** (9 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_zone_command()** (9 connections) — `server/commands/npc_admin/monitoring.py`
- **handle_npc_status_command()** (9 connections) — `server/commands/npc_admin/monitoring.py`
- **validate_npc_admin_permission()** (9 connections) — `server/commands/npc_admin/router.py`
- **_resolve_npc_command_player()** (5 connections) — `server/commands/npc_admin/router.py`
- **Any** (5 connections)
- **_extract_npc_subcommand()** (5 connections) — `server/commands/npc_admin/router.py`
- **_invoke_npc_handler()** (5 connections) — `server/commands/npc_admin/router.py`
- **_get_npc_help()** (4 connections) — `server/commands/npc_admin/router.py`
- **Any** (3 connections)
- **Any** (3 connections)
- **test_get_npc_instance_service_success()** (3 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- *... and 22 more nodes in this community*

## Relationships

- [commands admin mute](commands_admin_mute.md) (18 shared connections)
- [calendar schemas validate](calendar_schemas_validate.md) (17 shared connections)
- [commands rescue rationale](commands_rescue_rationale.md) (16 shared connections)
- [nats services metrics](nats_services_metrics.md) (13 shared connections)
- [admin auth service](admin_auth_service.md) (10 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (9 shared connections)
- [command inventory factories](command_inventory_factories.md) (7 shared connections)
- [occupants npc commands](occupants_npc_commands.md) (5 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (5 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (4 shared connections)
- [room websocket updates](room_websocket_updates.md) (4 shared connections)
- [npc look commands](npc_look_commands.md) (3 shared connections)

## Source Files

- `server/commands/npc_admin/__init__.py`
- `server/commands/npc_admin/behavior.py`
- `server/commands/npc_admin/instance.py`
- `server/commands/npc_admin/monitoring.py`
- `server/commands/npc_admin/router.py`
- `server/commands/npc_admin_commands.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 313 (89%)
- INFERRED: 37 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*