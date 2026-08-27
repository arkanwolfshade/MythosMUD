# test_combat_integration_base.py

> 32 nodes

## Key Concepts

- **test_position_commands.py** (13 connections) — `server/tests/unit/commands/test_position_commands.py`
- **_handle_position_change()** (12 connections) — `server/commands/position_commands.py`
- **handle_stand_command()** (10 connections) — `server/commands/position_commands.py`
- **SupportsConnectionManager** (9 connections) — `server/services/player_position_service.py`
- **handle_lie_command()** (9 connections) — `server/commands/position_commands.py`
- **SupportsPlayerPersistence** (8 connections) — `server/services/player_position_service.py`
- **handle_sit_command()** (8 connections) — `server/commands/position_commands.py`
- **_get_position_command_services()** (6 connections) — `server/commands/position_commands.py`
- **Request** (5 connections)
- **asyncio** (5 connections)
- **_broadcast_posture_change()** (4 connections) — `server/commands/position_commands.py`
- **_build_posture_change_event()** (4 connections) — `server/commands/position_commands.py`
- **.__init__()** (4 connections) — `server/services/player_position_service.py`
- **test_handle_ground_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_lie_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_sit_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_stand_already_standing_still_sends_player_update()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_stand_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **.get_online_player_by_display_name()** (2 connections) — `server/services/player_position_service.py`
- **Protocol** (2 connections)
- **Shared entry point for posture-changing commands.** (1 connections) — `server/commands/position_commands.py`
- **Handle /stand command.** (1 connections) — `server/commands/position_commands.py`
- **Handle /lie command (accepts optional 'down').** (1 connections) — `server/commands/position_commands.py`
- **Persistence surface required for posture updates.** (1 connections) — `server/services/player_position_service.py`
- **Live presence surface used to mirror posture into online player records.** (1 connections) — `server/services/player_position_service.py`
- *... and 7 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (10 shared connections)
- [pytest.md](pytest.md.md) (7 shared connections)
- [CombatParticipant](CombatParticipant.md) (5 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [LogAnalyzer](LogAnalyzer.md) (2 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (2 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (1 shared connections)
- [lint_sql_guardrails.py](lint_sql_guardrails.py.md) (1 shared connections)

## Source Files

- `server/commands/position_commands.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_position_commands.py`

## Audit Trail

- EXTRACTED: 82 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*