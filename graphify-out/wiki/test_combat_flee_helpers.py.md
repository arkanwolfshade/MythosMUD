# test_combat_flee_helpers.py

> 75 nodes

## Key Concepts

- **test_combat_flee_helpers.py** (27 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **combat_flee.py** (22 connections) — `server/commands/combat_flee.py`
- **AppWithState** (17 connections) — `server/commands/combat_app_protocols.py`
- **_FleeCommandHandlerLike** (17 connections) — `server/commands/combat_flee.py`
- **_resolve_flee_preconditions()** (14 connections) — `server/commands/combat_flee.py`
- **_validate_flee_combat_and_room()** (12 connections) — `server/commands/combat_flee.py`
- **_PlayerForFlee** (11 connections) — `server/commands/combat_flee.py`
- **FleePreconditionError** (11 connections) — `server/commands/combat_helpers.py`
- **_ensure_flee_standing()** (8 connections) — `server/commands/combat_flee.py`
- **_get_flee_player_uuid()** (8 connections) — `server/commands/combat_flee.py`
- **_PlayerPositionServiceLike** (7 connections) — `server/commands/combat_flee.py`
- **_get_flee_room_id()** (7 connections) — `server/commands/combat_flee.py`
- **combat_helpers.py** (7 connections) — `server/commands/combat_helpers.py`
- **test_validate_flee_combat_and_room_success()** (6 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **combat_app_protocols.py** (6 connections) — `server/commands/combat_app_protocols.py`
- **asyncio** (6 connections)
- **run_handle_flee_command()** (5 connections) — `server/commands/combat_flee.py`
- **test_validate_flee_combat_and_room_no_movement_service()** (5 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **_participant()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_ensure_flee_standing_when_already_standing()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_ensure_flee_standing_when_sitting()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_resolve_flee_preconditions_player_error()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_validate_flee_combat_and_room_no_combat_service()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **UUID** (4 connections)
- **.check_and_interrupt_rest()** (3 connections) — `server/commands/combat_flee.py`
- *... and 50 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (16 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (9 shared connections)
- [CombatInstance](CombatInstance.md) (8 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)
- [format_combat_status](format_combat_status.md) (2 shared connections)
- [server/models/game.py](server-models-game.py.md) (2 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_flee.py`
- `server/commands/combat_helpers.py`
- `server/tests/unit/commands/test_combat_flee_helpers.py`

## Audit Trail

- EXTRACTED: 151 (90%)
- INFERRED: 16 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*