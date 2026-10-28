# command_parser.py

> 327 nodes · cohesion 0.01

## Key Concepts

- **AliasStorage** (248 connections) — `server/alias_storage.py`
- **command_error()** (227 connections) — `server/commands/command_results.py`
- **command_service.py** (115 connections) — `server/commands/command_service.py`
- **alias_storage.py** (81 connections) — `server/alias_storage.py`
- **get_npc_instance_service()** (78 connections) — `server/services/npc_instance_service.py`
- **command_results.py** (60 connections) — `server/commands/command_results.py`
- **admin_commands.py** (42 connections) — `server/commands/admin_commands.py`
- **admin_mute_commands.py** (32 connections) — `server/commands/admin_mute_commands.py`
- **router.py** (32 connections) — `server/commands/npc_admin/router.py`
- **combat_loader.py** (30 connections) — `server/commands/combat_loader.py`
- **server/commands/__init__.py** (29 connections) — `server/commands/__init__.py`
- **admin_global_mute_commands.py** (26 connections) — `server/commands/admin_global_mute_commands.py`
- **get_combat_command_handler()** (26 connections) — `server/commands/combat_loader.py`
- **get_mythos_chronicle()** (26 connections) — `server/time/time_service.py`
- **npc_admin/__init__.py** (25 connections) — `server/commands/npc_admin/__init__.py`
- **instance.py** (25 connections) — `server/commands/npc_admin/instance.py`
- **commands/combat.py** (23 connections) — `server/commands/combat.py`
- **npc_admin_commands.py** (22 connections) — `server/commands/npc_admin_commands.py`
- **test_combat_loader.py** (22 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **_build_subcommand_map()** (20 connections) — `server/commands/npc_admin/router.py`
- **handle_mute_command()** (19 connections) — `server/commands/admin_mute_commands.py`
- **definition.py** (19 connections) — `server/commands/npc_admin/definition.py`
- **test_alias_storage.py** (19 connections) — `server/tests/unit/test_alias_storage.py`
- **handle_npc_command()** (18 connections) — `server/commands/npc_admin/router.py`
- **system_commands.py** (18 connections) — `server/commands/system_commands.py`
- *... and 302 more nodes in this community*

## Relationships

- [.resolve_combat_target](resolve_combat_target.md) (53 shared connections)
- [MagicCommandHandler](MagicCommandHandler.md) (44 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (40 shared connections)
- [Room](Room.md) (39 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (31 shared connections)
- [asyncio](asyncio.md) (27 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (21 shared connections)
- [PlayerStateCommandFactory](PlayerStateCommandFactory.md) (20 shared connections)
- [CORSConfig](CORSConfig.md) (19 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (18 shared connections)
- [test_help_docs.py](test_help_docs.py.md) (18 shared connections)
- [test_command_communication.py](test_command_communication.py.md) (17 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/commands/__init__.py`
- `server/commands/admin_commands.py`
- `server/commands/admin_global_mute_commands.py`
- `server/commands/admin_mute_commands.py`
- `server/commands/alias_commands.py`
- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/commands/command_results.py`
- `server/commands/command_service.py`
- `server/commands/exploration_commands.py`
- `server/commands/inventory_commands.py`
- `server/commands/npc_admin/__init__.py`
- `server/commands/npc_admin/behavior.py`
- `server/commands/npc_admin/definition.py`
- `server/commands/npc_admin/instance.py`
- `server/commands/npc_admin/monitoring.py`
- `server/commands/npc_admin/router.py`
- `server/commands/npc_admin/test_occupants.py`

## Audit Trail

- EXTRACTED: 1519 (89%)
- INFERRED: 187 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*