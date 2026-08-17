# AliasStorage

> 531 nodes

## Key Concepts

- **AliasStorage** (264 connections) — `server/alias_storage.py`
- **command_service.py** (108 connections) — `server/commands/command_service.py`
- **alias_storage.py** (75 connections) — `server/alias_storage.py`
- **command_handler_unified.py** (55 connections) — `server/command_handler_unified.py`
- **magic_service.py** (48 connections) — `server/game/magic/magic_service.py`
- **spell_effects.py** (48 connections) — `server/game/magic/spell_effects.py`
- **.state()** (37 connections) — `server/realtime/connection_state_machine.py`
- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.app()** (34 connections) — `server/commands/look_helpers.py`
- **admin_commands.py** (33 connections) — `server/commands/admin_commands.py`
- **rescue_commands.py** (33 connections) — `server/commands/rescue_commands.py`
- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **MagicCommandHandler** (30 connections) — `server/commands/magic_commands.py`
- **admin_mute_commands.py** (29 connections) — `server/commands/admin_mute_commands.py`
- **server/commands/__init__.py** (29 connections) — `server/commands/__init__.py`
- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **rest_command.py** (28 connections) — `server/commands/rest_command.py`
- **TauntCommandHandler** (27 connections) — `server/commands/combat_taunt.py`
- **handle_ground_command()** (27 connections) — `server/commands/rescue_commands.py`
- **WebSocketRequestContext** (26 connections) — `server/realtime/request_context.py`
- **processing.py** (26 connections) — `server/command_handler/processing.py`
- **debrief_command.py** (26 connections) — `server/commands/debrief_command.py`
- **magic_commands.py** (26 connections) — `server/commands/magic_commands.py`
- **test_debrief_command.py** (26 connections) — `server/tests/unit/commands/test_debrief_command.py`
- *... and 506 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (119 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (42 shared connections)
- [TestHelperFunctions](TestHelperFunctions.md) (39 shared connections)
- [DatabaseError](DatabaseError.md) (38 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (37 shared connections)
- [test_alias_storage.py](test_alias_storage.py.md) (33 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (32 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (32 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (29 shared connections)
- [asyncio](asyncio.md) (27 shared connections)
- [TargetMatch](TargetMatch.md) (26 shared connections)
- [build_event](build_event.md) (25 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/app/lifespan_magic.py`
- `server/command_handler/__init__.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/catatonia_check.py`
- `server/command_handler/command_execution_request.py`
- `server/command_handler/command_input.py`
- `server/command_handler/processing.py`
- `server/command_handler_unified.py`
- `server/commands/__init__.py`
- `server/commands/admin_commands.py`
- `server/commands/admin_mute_commands.py`
- `server/commands/alias_commands.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_taunt.py`
- `server/commands/command_service.py`
- `server/commands/debrief_command.py`
- `server/commands/exploration_commands.py`
- `server/commands/help_commands.py`
- `server/commands/inventory_commands.py`

## Audit Trail

- EXTRACTED: 1856 (86%)
- INFERRED: 314 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*