# test_dependency_analysis.py

> 38 nodes

## Key Concepts

- **combat_loader.py** (26 connections) — `server/commands/combat_loader.py`
- **test_combat_loader.py** (23 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **get_combat_command_handler()** (22 connections) — `server/commands/combat_loader.py`
- **commands/combat.py** (19 connections) — `server/commands/combat.py`
- **_app_from_request()** (12 connections) — `server/commands/combat_loader.py`
- **CombatCommandHandlerExtras** (9 connections) — `server/commands/combat_handler.py`
- **handle_kick_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_attack_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_flee_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_taunt_command()** (8 connections) — `server/commands/combat_loader.py`
- **_mock_app_with_container()** (8 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **asyncio** (6 connections)
- **test_handle_attack_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_flee_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_kick_command_sets_type()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_punch_command_sets_type()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_strike_command_sets_type()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_taunt_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_get_combat_command_handler_creates_singleton()** (3 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **reset_combat_handler()** (2 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_app_from_request_none()** (2 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_app_from_request_returns_app()** (2 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_get_combat_command_handler_requires_app()** (2 connections) — `server/tests/unit/commands/test_combat_loader.py`
- *... and 13 more nodes in this community*

## Relationships

- [ItemPrototypeModel](ItemPrototypeModel.md) (8 shared connections)
- [CombatParticipant](CombatParticipant.md) (7 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (6 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)
- [test_container_query_helpers_async.py](test_container_query_helpers_async.py.md) (3 shared connections)
- [analyze_log_file](analyze_log_file.md) (3 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [PopulationStats](PopulationStats.md) (2 shared connections)
- [CombatInstance](CombatInstance.md) (2 shared connections)
- [waitForMessage](waitForMessage.md) (2 shared connections)
- [MythosMUDError](MythosMUDError.md) (2 shared connections)
- [establish_websocket_connection](establish_websocket_connection.md) (1 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/tests/unit/commands/test_combat_loader.py`

## Audit Trail

- EXTRACTED: 117 (86%)
- INFERRED: 19 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*