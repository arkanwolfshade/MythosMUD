# combat services messaging

> 4 nodes

## Key Concepts

- **TestNPCSessionMaker** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_session_maker()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test NPC session maker functions.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **Test get_npc_session_maker() returns session maker.** (1 connections) — `server/tests/unit/infrastructure/test_npc_database.py`

## Relationships

- [player effects endpoints](player_effects_endpoints.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 8 (89%)
- INFERRED: 1 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*