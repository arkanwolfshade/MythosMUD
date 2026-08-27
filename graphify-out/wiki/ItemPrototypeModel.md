# ItemPrototypeModel

> 40 nodes

## Key Concepts

- **CombatCommandHandler** (45 connections) — `server/commands/combat_handler.py`
- **.__init__()** (9 connections) — `server/commands/combat_handler.py`
- **.handle_attack_command()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_taunt_command()** (5 connections) — `server/commands/combat_handler.py`
- **.combat_service()** (4 connections) — `server/commands/combat_handler.py`
- **.extract_combat_command_data()** (4 connections) — `server/commands/combat_handler.py`
- **.handle_flee_command()** (4 connections) — `server/commands/combat_handler.py`
- **test_combat_command_handler_extras_optional()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **Any** (4 connections)
- **.get_npc_instance()** (3 connections) — `server/commands/combat_handler.py`
- **.get_room_data()** (3 connections) — `server/commands/combat_handler.py`
- **.movement_service()** (3 connections) — `server/commands/combat_handler.py`
- **.player_position_service()** (3 connections) — `server/commands/combat_handler.py`
- **.room_forbids_combat()** (3 connections) — `server/commands/combat_handler.py`
- **.validate_combat_action()** (3 connections) — `server/commands/combat_handler.py`
- **.validate_target_name()** (3 connections) — `server/commands/combat_handler.py`
- **test_combat_command_handler_requires_async_persistence()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **AliasStorage** (3 connections)
- **PlayerCombatService** (1 connections)
- **Combat service for command modules.** (1 connections) — `server/commands/combat_handler.py`
- **Movement service for command modules.** (1 connections) — `server/commands/combat_handler.py`
- **Player position service for command modules.** (1 connections) — `server/commands/combat_handler.py`
- **Extract command type and target name from command_data. Public API.** (1 connections) — `server/commands/combat_handler.py`
- **Validate that target name is provided. Public API.** (1 connections) — `server/commands/combat_handler.py`
- **True if the room has no_combat attribute set. Public API.** (1 connections) — `server/commands/combat_handler.py`
- *... and 15 more nodes in this community*

## Relationships

- [test_dependency_analysis.py](test_dependency_analysis.py.md) (8 shared connections)
- [test_container_query_helpers_async.py](test_container_query_helpers_async.py.md) (6 shared connections)
- [establish_websocket_connection](establish_websocket_connection.md) (4 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (4 shared connections)
- [Test Value Distribution Chart](Test_Value_Distribution_Chart.md) (3 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (3 shared connections)
- [MythosMUDError](MythosMUDError.md) (3 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (2 shared connections)
- [NATSError](NATSError.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [PopulationStats](PopulationStats.md) (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/tests/unit/commands/test_combat_handler.py`

## Audit Trail

- EXTRACTED: 74 (83%)
- INFERRED: 15 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*