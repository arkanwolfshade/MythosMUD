# Combat Flee Command

> 68 nodes · cohesion 0.05

## Key Concepts

- **test_combat_flee_helpers.py** (23 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **combat_flee.py** (17 connections) — `server/commands/combat_flee.py`
- **_FleeCommandHandlerLike** (17 connections) — `server/commands/combat_flee.py`
- **FleePreconditionError** (17 connections) — `server/commands/combat_helpers.py`
- **_resolve_flee_preconditions()** (16 connections) — `server/commands/combat_flee.py`
- **_validate_flee_combat_and_room()** (12 connections) — `server/commands/combat_flee.py`
- **_PlayerForFlee** (11 connections) — `server/commands/combat_flee.py`
- **_ensure_flee_standing()** (10 connections) — `server/commands/combat_flee.py`
- **_get_flee_player_uuid()** (8 connections) — `server/commands/combat_flee.py`
- **_get_flee_room_id()** (8 connections) — `server/commands/combat_flee.py`
- **_PlayerPositionServiceLike** (7 connections) — `server/commands/combat_flee.py`
- **UUID** (7 connections) — `server/commands/combat_flee.py`
- **run_handle_flee_command()** (6 connections) — `server/commands/combat_flee.py`
- **AppWithState** (6 connections) — `server/commands/combat_flee.py`
- **_participant()** (5 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_validate_flee_combat_and_room_success()** (5 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **CombatInstance** (5 connections) — `server/commands/combat_flee.py`
- **.check_and_interrupt_rest()** (4 connections) — `server/commands/combat_flee.py`
- **.get_player_and_room()** (4 connections) — `server/commands/combat_flee.py`
- **test_validate_flee_combat_and_room_no_movement_service()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **CombatService** (4 connections) — `server/commands/combat_flee.py`
- **.combat_service()** (3 connections) — `server/commands/combat_flee.py`
- **.get_room_data()** (3 connections) — `server/commands/combat_flee.py`
- **.get_stats()** (3 connections) — `server/commands/combat_flee.py`
- **.change_position()** (3 connections) — `server/commands/combat_flee.py`
- *... and 43 more nodes in this community*

## Relationships

- [[Combat Command Handler]] (9 shared connections)
- [[Combat Taunt Tests]] (9 shared connections)
- [[Combat Service Bundle]] (8 shared connections)
- [[Player Combat XP]] (3 shared connections)
- [[Combat Command Helpers]] (2 shared connections)
- [[Database Manager Tests]] (1 shared connections)
- [[Combat Domain Events]] (1 shared connections)
- [[Player Domain Model]] (1 shared connections)

## Source Files

- `server/commands/combat_flee.py`
- `server/commands/combat_helpers.py`
- `server/tests/unit/commands/test_combat_flee_helpers.py`

## Audit Trail

- EXTRACTED: 239 (88%)
- INFERRED: 33 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
