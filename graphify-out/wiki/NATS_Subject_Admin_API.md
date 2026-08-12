# NATS Subject Admin API

> 16 nodes

## Key Concepts

- **validate_prototypes.py** (8 connections) — `server/scripts/validate_prototypes.py`
- **.load_from_path()** (7 connections) — `server/game/items/prototype_registry.py`
- **._record_validation_failure()** (6 connections) — `server/game/items/prototype_registry.py`
- **._load_one_prototype()** (6 connections) — `server/game/items/prototype_registry.py`
- **.get()** (6 connections) — `server/game/items/prototype_registry.py`
- **Any** (4 connections)
- **Path** (3 connections)
- **.invalid_entries()** (3 connections) — `server/game/items/prototype_registry.py`
- **parse_arguments()** (3 connections) — `server/scripts/validate_prototypes.py`
- **main()** (3 connections) — `server/scripts/validate_prototypes.py`
- **ValidationError** (1 connections)
- **Load prototypes from a directory of JSON files.** (1 connections) — `server/game/items/prototype_registry.py`
- **Get a prototype by ID.          Args:             prototype_id: The ID of the** (1 connections) — `server/game/items/prototype_registry.py`
- **Get all invalid entries that failed validation.          Returns:** (1 connections) — `server/game/items/prototype_registry.py`
- **Namespace** (1 connections)
- **CLI entrypoint for validating MythosMUD item prototype definitions.** (1 connections) — `server/scripts/validate_prototypes.py`

## Relationships

- [NATS Retry Handler](NATS_Retry_Handler.md) (13 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (1 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (1 shared connections)

## Source Files

- `server/game/items/prototype_registry.py`
- `server/scripts/validate_prototypes.py`

## Audit Trail

- EXTRACTED: 54 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*