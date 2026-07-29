# . handle nats unavailable()

> 8 nodes

## Key Concepts

- **.initialize_nats_combat()** (7 connections) — `server/container/bundles/combat.py`
- **._validate_nats_combat_prerequisites()** (4 connections) — `server/container/bundles/combat.py`
- **._start_nats_message_handler()** (4 connections) — `server/container/bundles/combat.py`
- **._handle_nats_unavailable()** (3 connections) — `server/container/bundles/combat.py`
- **Raise if prerequisites for NATS combat are missing.** (1 connections) — `server/container/bundles/combat.py`
- **Start NATS message handler if available. Logs and swallows errors.** (1 connections) — `server/container/bundles/combat.py`
- **Handle case when NATS is not connected. Raises in prod, sets combat_service to N** (1 connections) — `server/container/bundles/combat.py`
- **Initialize NATS-dependent combat service and start NATS message handler.** (1 connections) — `server/container/bundles/combat.py`

## Relationships

- [.initialize()](initialize%28%29.md) (4 shared connections)
- [.shutdown()](shutdown%28%29.md) (3 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (1 shared connections)

## Source Files

- `server/container/bundles/combat.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*