# Cursor Skills Critique

> 4 nodes

## Key Concepts

- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **._load_from_database()** (4 connections) — `server/services/holiday_service.py`
- **Path** (2 connections)
- **Load holidays from PostgreSQL database.** (1 connections) — `server/services/holiday_service.py`

## Relationships

- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Spell Effects Tests](Spell_Effects_Tests.md) (2 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (2 shared connections)
- [Exploration Command Factory](Exploration_Command_Factory.md) (1 shared connections)

## Source Files

- `server/services/holiday_service.py`

## Audit Trail

- EXTRACTED: 14 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*