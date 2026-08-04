# command commands validation

> 5 nodes

## Key Concepts

- **._initialize_item_services()** (10 connections) — `server/container/bundles/game.py`
- **._handle_item_prototypes_db_error()** (4 connections) — `server/container/bundles/game.py`
- **Exception** (1 connections)
- **On SQLAlchemyError: log, optionally warn about schema/DDL, and clear item regist** (1 connections) — `server/container/bundles/game.py`
- **Load item prototypes from PostgreSQL and create item factory.** (1 connections) — `server/container/bundles/game.py`

## Relationships

- [nats services service](nats_services_service.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)
- [dead letter realtime](dead_letter_realtime.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [npc spawn validator](npc_spawn_validator.md) (1 shared connections)
- [connection cleaner realtime](connection_cleaner_realtime.md) (1 shared connections)
- [combat npc mixin](combat_npc_mixin.md) (1 shared connections)
- [uuid npc combat](uuid_npc_combat.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`

## Audit Trail

- EXTRACTED: 16 (94%)
- INFERRED: 1 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*