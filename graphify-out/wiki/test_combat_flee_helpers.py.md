# test_combat_flee_helpers.py

> 70 nodes

## Key Concepts

- **test_combat_flee_helpers.py** (28 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **combat_flee.py** (22 connections) — `server/commands/combat_flee.py`
- **_FleeCommandHandlerLike** (16 connections) — `server/commands/combat_flee.py`
- **_resolve_flee_preconditions()** (15 connections) — `server/commands/combat_flee.py`
- **_validate_flee_combat_and_room()** (12 connections) — `server/commands/combat_flee.py`
- **FleePreconditionError** (10 connections) — `server/commands/combat_helpers.py`
- **_PlayerForFlee** (8 connections) — `server/commands/combat_flee.py`
- **_ensure_flee_standing()** (8 connections) — `server/commands/combat_flee.py`
- **_get_flee_player_uuid()** (8 connections) — `server/commands/combat_flee.py`
- **run_handle_flee_command()** (8 connections) — `server/commands/combat_flee.py`
- **_get_flee_room_id()** (7 connections) — `server/commands/combat_flee.py`
- **combat_helpers.py** (7 connections) — `server/commands/combat_helpers.py`
- **test_validate_flee_combat_and_room_success()** (6 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **asyncio** (6 connections)
- **test_resolve_flee_preconditions_player_error()** (5 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_validate_flee_combat_and_room_no_movement_service()** (5 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **_PlayerPositionServiceLike** (4 connections) — `server/commands/combat_flee.py`
- **_participant()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_ensure_flee_standing_when_already_standing()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_ensure_flee_standing_when_sitting()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_validate_flee_combat_and_room_no_combat_service()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **UUID** (4 connections)
- **.check_and_interrupt_rest()** (3 connections) — `server/commands/combat_flee.py`
- **.combat_service()** (3 connections) — `server/commands/combat_flee.py`
- **.get_player_and_room()** (3 connections) — `server/commands/combat_flee.py`
- *... and 45 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (8 shared connections)
- [CombatService](CombatService.md) (7 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (5 shared connections)
- [combat_loader.py](combat_loader.py.md) (4 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (1 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (1 shared connections)
- [server/models/game.py](server-models-game.py.md) (1 shared connections)

## Source Files

- `server/commands/combat_flee.py`
- `server/commands/combat_helpers.py`
- `server/tests/unit/commands/test_combat_flee_helpers.py`

## Audit Trail

- EXTRACTED: 142 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*