# .state

> 19 nodes

## Key Concepts

- **.state()** (37 connections) — `server/realtime/connection_state_machine.py`
- **.app()** (33 connections) — `server/commands/look_helpers.py`
- **_websocket_unified_command_result()** (11 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_explore_command()** (9 connections) — `server/commands/exploration_commands.py`
- **_get_ground_services()** (6 connections) — `server/commands/rescue_commands.py`
- **test_exploration_commands.py** (6 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **_app_state_container_service()** (5 connections) — `server/commands/container_helpers_inventory_ops.py`
- **test_handle_explore_command()** (4 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **test_handle_explore_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **asyncio** (2 connections)
- **Any** (1 connections)
- **Handle exploration requests by returning a simple message. This lightweight…** (1 connections) — `server/commands/exploration_commands.py`
- **FastAPI/Starlette application (or duck-typed equivalent).** (1 connections) — `server/commands/look_helpers.py`
- **Get persistence and registry from request. Returns (persistence, registry).** (1 connections) — `server/commands/rescue_commands.py`
- **Current FSM state as a single State. Uses python-statemachine 3.x configuration…** (1 connections) — `server/realtime/connection_state_machine.py`
- **Build request context, run process_command_unified, attach room_state when…** (1 connections) — `server/realtime/websocket_handler_commands.py`
- **Unit tests for exploration command handlers. Tests the exploration command…** (1 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **Test handle_explore_command() explores area.** (1 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **Test handle_explore_command() handles missing persistence.** (1 connections) — `server/tests/unit/commands/test_exploration_commands.py`

## Relationships

- [AliasStorage](AliasStorage.md) (6 shared connections)
- [real_time.py](real_time.py.md) (4 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (4 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (4 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (4 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (3 shared connections)
- [communication_commands_flows.py](communication_commands_flows.py.md) (3 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (3 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (3 shared connections)
- [GameStateProvider](GameStateProvider.md) (3 shared connections)
- [test_admin_summon_command.py](test_admin_summon_command.py.md) (2 shared connections)
- [combat_loader.py](combat_loader.py.md) (2 shared connections)

## Source Files

- `server/commands/container_helpers_inventory_ops.py`
- `server/commands/exploration_commands.py`
- `server/commands/look_helpers.py`
- `server/commands/rescue_commands.py`
- `server/realtime/connection_state_machine.py`
- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/commands/test_exploration_commands.py`

## Audit Trail

- EXTRACTED: 37 (36%)
- INFERRED: 65 (64%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*