# Realtime Visual Indicator

> 5 nodes

## Key Concepts

- **._initialize_item_services()** (10 connections) — `server/container/bundles/game.py`
- **._handle_item_prototypes_db_error()** (4 connections) — `server/container/bundles/game.py`
- **Exception** (1 connections)
- **On SQLAlchemyError: log, optionally warn about schema/DDL, and clear item regist** (1 connections) — `server/container/bundles/game.py`
- **Load item prototypes from PostgreSQL and create item factory.** (1 connections) — `server/container/bundles/game.py`

## Relationships

- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (4 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Typography Layout Spec](Typography_Layout_Spec.md) (1 shared connections)
- [Command Integration Summary](Command_Integration_Summary.md) (1 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (1 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`

## Audit Trail

- EXTRACTED: 16 (94%)
- INFERRED: 1 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*