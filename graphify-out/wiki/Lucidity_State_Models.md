# Lucidity State Models

> 60 nodes · cohesion 0.08

## Key Concepts

- **LucidityService** (98 connections) — `server/services/lucidity_service.py`
- **LucidityRepository** (25 connections) — `server/services/lucidity_repository.py`
- **CatatoniaObserverProtocol** (24 connections) — `server/services/lucidity_helpers.py`
- **UUID** (20 connections) — `server/services/lucidity_service.py`
- **LucidityAdjustmentFinalizeContext** (15 connections) — `server/services/lucidity_helpers.py`
- **LucidityChangeEventContext** (15 connections) — `server/services/lucidity_helpers.py`
- **LucidityUpdateResult** (15 connections) — `server/services/lucidity_helpers.py`
- **Tier** (14 connections) — `server/services/lucidity_helpers.py`
- **PlayerLucidity** (11 connections) — `server/services/lucidity_service.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **LucidityAdjustmentFinalizeContext** (9 connections) — `server/services/lucidity_service.py`
- **LucidityChangeEventContext** (9 connections) — `server/services/lucidity_service.py`
- **datetime** (9 connections) — `server/services/lucidity_service.py`
- **LucidityCooldown** (9 connections) — `server/services/lucidity_service.py`
- **LucidityUpdateResult** (9 connections) — `server/services/lucidity_service.py`
- **Tier** (9 connections) — `server/services/lucidity_service.py`
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **AsyncSession** (8 connections) — `server/services/lucidity_service.py`
- **LucidityExposureState** (8 connections) — `server/services/lucidity_service.py`
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- **._calculate_max_lcd()** (7 connections) — `server/services/lucidity_service.py`
- **._add_liabilities_for_adjustment()** (6 connections) — `server/services/lucidity_service.py`
- **.add_liability()** (6 connections) — `server/services/lucidity_service.py`
- **.set_cooldown()** (5 connections) — `server/services/lucidity_service.py`
- *... and 35 more nodes in this community*

## Relationships

- [[Lucidity Rescue Helpers]] (36 shared connections)
- [[Active Lucidity Service]] (20 shared connections)
- [[Lucidity Event Dispatcher]] (13 shared connections)
- [[Services Lucidity Repository]] (8 shared connections)
- [[Services Rescue Service]] (8 shared connections)
- [[Player Respawn Service]] (8 shared connections)
- [[Combat Taunt Tests]] (7 shared connections)
- [[Services Hallucination Frequency]] (6 shared connections)
- [[Services Player Respawn]] (5 shared connections)
- [[Services Service Lucidity]] (5 shared connections)
- [[Combat Service Bundle]] (4 shared connections)
- [[Lucidity Database Models]] (3 shared connections)

## Source Files

- `server/services/lucidity_helpers.py`
- `server/services/lucidity_repository.py`
- `server/services/lucidity_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`

## Audit Trail

- EXTRACTED: 240 (55%)
- INFERRED: 193 (45%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
