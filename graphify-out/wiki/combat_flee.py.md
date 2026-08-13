# combat_flee.py

> 39 nodes

## Key Concepts

- **combat_flee.py** (22 connections) — `server/commands/combat_flee.py`
- **_FleeCommandHandlerLike** (17 connections) — `server/commands/combat_flee.py`
- **_resolve_flee_preconditions()** (14 connections) — `server/commands/combat_flee.py`
- **_PlayerForFlee** (11 connections) — `server/commands/combat_flee.py`
- **FleePreconditionError** (11 connections) — `server/commands/combat_helpers.py`
- **_ensure_flee_standing()** (8 connections) — `server/commands/combat_flee.py`
- **_get_flee_player_uuid()** (8 connections) — `server/commands/combat_flee.py`
- **_PlayerPositionServiceLike** (7 connections) — `server/commands/combat_flee.py`
- **run_handle_flee_command()** (5 connections) — `server/commands/combat_flee.py`
- **UUID** (4 connections)
- **.check_and_interrupt_rest()** (3 connections) — `server/commands/combat_flee.py`
- **.combat_service()** (3 connections) — `server/commands/combat_flee.py`
- **.get_player_and_room()** (3 connections) — `server/commands/combat_flee.py`
- **AppWithState** (3 connections)
- **Protocol** (3 connections)
- **.get_room_data()** (2 connections) — `server/commands/combat_flee.py`
- **.movement_service()** (2 connections) — `server/commands/combat_flee.py`
- **.player_position_service()** (2 connections) — `server/commands/combat_flee.py`
- **.get_stats()** (2 connections) — `server/commands/combat_flee.py`
- **.change_position()** (2 connections) — `server/commands/combat_flee.py`
- **.__init__()** (1 connections) — `server/commands/combat_helpers.py`
- **Exception** (1 connections)
- **Flee command flow: preconditions and execution. Extracted from combat.py to…** (1 connections) — `server/commands/combat_flee.py`
- **Resolve player_id to UUID; return (uuid, None) or (None, error_dict).** (1 connections) — `server/commands/combat_flee.py`
- **Resolve player, player_id, combat, and room_id for flee. Returns (player,…** (1 connections) — `server/commands/combat_flee.py`
- *... and 14 more nodes in this community*

## Relationships

- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (17 shared connections)
- [get_logger](get_logger.md) (16 shared connections)
- [combat_helpers.py](combat_helpers.py.md) (2 shared connections)
- [combat_flee_handler.py](combat_flee_handler.py.md) (2 shared connections)

## Source Files

- `server/commands/combat_flee.py`
- `server/commands/combat_helpers.py`

## Audit Trail

- EXTRACTED: 85 (90%)
- INFERRED: 9 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*