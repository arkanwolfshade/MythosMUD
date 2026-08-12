# Investigations Sessions Session

> 8 nodes

## Key Concepts

- **_get_flee_room_id()** (8 connections) — `server/commands/combat_flee.py`
- **.get_room_data()** (3 connections) — `server/commands/combat_flee.py`
- **test_get_flee_room_id_unknown_room()** (3 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_get_flee_room_id_no_exits()** (3 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **Room record for exit graph checks.** (1 connections) — `server/commands/combat_flee.py`
- **Ensure room exists and has exits; return (room_id, None) or (None, error_dict).** (1 connections) — `server/commands/combat_flee.py`
- **Missing room data yields unknown room.** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **Room with empty exits blocks flee.** (1 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`

## Relationships

- [Combat Taunt Tests](Combat_Taunt_Tests.md) (3 shared connections)
- [Commands Inventory Display](Commands_Inventory_Display.md) (2 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)

## Source Files

- `server/commands/combat_flee.py`
- `server/tests/unit/commands/test_combat_flee_helpers.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*