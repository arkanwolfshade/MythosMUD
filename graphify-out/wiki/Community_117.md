# Community 117

> 90 nodes

## Key Concepts

- **LucidityService** (79 connections) — `server/services/lucidity_service.py`
- **test_lucidity_service.py** (25 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **asyncio** (16 connections)
- **UUID** (12 connections)
- **player_lucidity** (9 connections) — `db/schema.sql`
- **._calculate_max_lcd()** (8 connections) — `server/services/lucidity_service.py`
- **._finalize_lucidity_adjustment()** (8 connections) — `server/services/lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (8 connections) — `server/services/lucidity_service.py`
- **.apply_lucidity_adjustment()** (7 connections) — `server/services/lucidity_service.py`
- **._add_liabilities_for_adjustment()** (5 connections) — `server/services/lucidity_service.py`
- **._apply_delta_to_record()** (5 connections) — `server/services/lucidity_service.py`
- **.set_cooldown()** (5 connections) — `server/services/lucidity_service.py`
- **test_apply_lucidity_adjustment_adds_liability_on_large_drop()** (5 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **test_apply_lucidity_adjustment_clears_phantoms_on_tier_improvement()** (5 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **test_apply_lucidity_adjustment_keeps_phantoms_within_eligible_tiers()** (5 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **test_apply_lucidity_adjustment_writes_through_the_tier_cache()** (5 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **.add_liability()** (4 connections) — `server/services/lucidity_service.py`
- **.get_cooldown()** (4 connections) — `server/services/lucidity_service.py`
- **._get_player_from_record_inspect()** (4 connections) — `server/services/lucidity_service.py`
- **.get_player_lucidity()** (4 connections) — `server/services/lucidity_service.py`
- **.increment_exposure_state()** (4 connections) — `server/services/lucidity_service.py`
- **._max_lcd_from_stats()** (4 connections) — `server/services/lucidity_service.py`
- **test_add_liability_increments_stack()** (4 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **test_add_liability_new_entry()** (4 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **test_apply_lucidity_adjustment_clamps_to_max()** (4 connections) — `server/tests/unit/services/test_lucidity_service.py`
- *... and 65 more nodes in this community*

## Relationships

- [Catatonia Status Checks](Catatonia_Status_Checks.md) (12 shared connections)
- [Community 348](Community_348.md) (4 shared connections)
- [Community 289](Community_289.md) (4 shared connections)
- [Community 38](Community_38.md) (4 shared connections)
- [Community 36](Community_36.md) (4 shared connections)
- [Community 29](Community_29.md) (3 shared connections)
- [Community 150](Community_150.md) (3 shared connections)
- [Community 382](Community_382.md) (3 shared connections)
- [Community 738](Community_738.md) (3 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (3 shared connections)
- [Community 217](Community_217.md) (3 shared connections)
- [Community 103](Community_103.md) (2 shared connections)

## Source Files

- `db/schema.sql`
- `server/services/lucidity_service.py`
- `server/tests/unit/services/test_lucidity_service.py`

## Audit Trail

- EXTRACTED: 179 (85%)
- INFERRED: 31 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*