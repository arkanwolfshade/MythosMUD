# Lucidity State Models

> 9 nodes · cohesion 0.03

## Key Concepts

- **Tier** (14 connections) — `server/services/lucidity_helpers.py`
- **Tier** (9 connections) — `server/services/lucidity_service.py`
- **UUID** (6 connections) — `server/services/lucidity_event_dispatcher.py`
- **UUID** (6 connections) — `server/services/lucidity_trigger_handlers.py`
- **UUID** (5 connections) — `server/services/lucidity_helpers.py`
- **datetime** (4 connections) — `server/services/lucidity_helpers.py`
- **LiabilityStackEntry** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **LiabilityStackEntry** (3 connections) — `server/services/lucidity_helpers.py`
- **LiabilityStackEntry** (2 connections) — `server/services/lucidity_event_dispatcher.py`

## Relationships

- [Services Lucidity Repository](Services_Lucidity_Repository.md) (2 shared connections)
- [Player Death Service Tests](Player_Death_Service_Tests.md) (1 shared connections)
- [Lucidity Event Dispatcher](Lucidity_Event_Dispatcher.md) (1 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Audit Trail

- EXTRACTED: 31 (58%)
- INFERRED: 22 (42%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*