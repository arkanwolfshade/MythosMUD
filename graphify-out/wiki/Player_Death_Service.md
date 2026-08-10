# Player Death Service

> 22 nodes

## Key Concepts

- **position_commands.py** (21 connections) — `server/commands/position_commands.py`
- **_handle_position_change()** (12 connections) — `server/commands/position_commands.py`
- **test_position_commands.py** (11 connections) — `server/tests/unit/commands/test_position_commands.py`
- **handle_stand_command()** (10 connections) — `server/commands/position_commands.py`
- **handle_lie_command()** (10 connections) — `server/commands/position_commands.py`
- **handle_sit_command()** (9 connections) — `server/commands/position_commands.py`
- **Any** (6 connections)
- **_broadcast_posture_change()** (4 connections) — `server/commands/position_commands.py`
- **_get_position_command_services()** (3 connections) — `server/commands/position_commands.py`
- **test_handle_sit_command()** (3 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_stand_command()** (3 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_lie_command()** (3 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_ground_command()** (3 connections) — `server/tests/unit/commands/test_position_commands.py`
- **Command handlers for posture adjustments within MythosMUD.  According to margina** (1 connections) — `server/commands/position_commands.py`
- **Shared entry point for posture-changing commands.** (1 connections) — `server/commands/position_commands.py`
- **Handle /stand command.** (1 connections) — `server/commands/position_commands.py`
- **Handle /lie command (accepts optional 'down').** (1 connections) — `server/commands/position_commands.py`
- **Unit tests for position command handlers.  Tests the sit, stand, lie, and ground** (1 connections) — `server/tests/unit/commands/test_position_commands.py`
- **Test handle_sit_command() changes player position to sitting.** (1 connections) — `server/tests/unit/commands/test_position_commands.py`
- **Test handle_stand_command() changes player position to standing.** (1 connections) — `server/tests/unit/commands/test_position_commands.py`
- **Test handle_lie_command() changes player position to lying.** (1 connections) — `server/tests/unit/commands/test_position_commands.py`
- **Test handle_ground_command() helps catatonic player.** (1 connections) — `server/tests/unit/commands/test_position_commands.py`

## Relationships

- [Client Event Store](Client_Event_Store.md) (20 shared connections)
- [Realtime Npc Event](Realtime_Npc_Event.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Follow Service Tests](Follow_Service_Tests.md) (3 shared connections)
- [NPC Event Handler Tests](NPC_Event_Handler_Tests.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)

## Source Files

- `server/commands/position_commands.py`
- `server/tests/unit/commands/test_position_commands.py`

## Audit Trail

- EXTRACTED: 103 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*