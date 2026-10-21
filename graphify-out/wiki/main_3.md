# main

> 12 nodes · cohesion 0.18

## Key Concepts

- **._connect_nats()** (7 connections) — `server/container/bundles/realtime.py`
- **._setup_nats_dependent_services()** (7 connections) — `server/container/bundles/realtime.py`
- **._handle_nats_connect_error()** (5 connections) — `server/container/bundles/realtime.py`
- **._handle_nats_connect_false()** (4 connections) — `server/container/bundles/realtime.py`
- **._raise_if_e2e_nats_required()** (4 connections) — `server/container/bundles/realtime.py`
- **Any** (2 connections)
- **BaseException** (1 connections)
- **Attach event publisher and message handler when NATS is available.** (1 connections) — `server/container/bundles/realtime.py`
- **Raise RuntimeError when e2e requires live NATS; no-op for other environments.** (1 connections) — `server/container/bundles/realtime.py`
- **Convert connect failures into hard error (e2e) or soft log (other envs).** (1 connections) — `server/container/bundles/realtime.py`
- **Handle connect() returning False; raise for e2e, soft-warn otherwise.** (1 connections) — `server/container/bundles/realtime.py`
- **Connect to NATS if enabled and not unit_test. Returns NATSService or None.…** (1 connections) — `server/container/bundles/realtime.py`

## Relationships

- [test_message_handlers.py](test_message_handlers.py.md) (7 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (1 shared connections)
- [MythosMUD Code Quality Targets for AI](MythosMUD_Code_Quality_Targets_for_AI.md) (1 shared connections)
- [deque](deque.md) (1 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (1 shared connections)

## Source Files

- `server/container/bundles/realtime.py`

## Audit Trail

- EXTRACTED: 22 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*