# Commands Npc Admin

> 6 nodes

## Key Concepts

- **FleePreconditionError** (12 connections) — `server/commands/combat_helpers.py`
- **test_resolve_flee_preconditions_player_error()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **Exception** (1 connections)
- **.__init__()** (1 connections) — `server/commands/combat_helpers.py`
- **Raised when flee preconditions fail; carries the error dict to return to the cli** (1 connections) — `server/commands/combat_helpers.py`
- **FleePreconditionError wraps get_player_and_room error.** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`

## Relationships

- [Investigations Sessions Session](Investigations_Sessions_Session.md) (4 shared connections)
- [Combat Taunt Tests](Combat_Taunt_Tests.md) (2 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (1 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (1 shared connections)
- [Commands Inventory Display](Commands_Inventory_Display.md) (1 shared connections)
- [Quest Instance Repository](Quest_Instance_Repository.md) (1 shared connections)

## Source Files

- `server/commands/combat_helpers.py`
- `server/tests/unit/commands/test_combat_flee_helpers.py`

## Audit Trail

- EXTRACTED: 15 (75%)
- INFERRED: 5 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*