# Community 138

> 86 nodes

## Key Concepts

- **LucidityService** (85 connections) — `server/services/lucidity_service.py`
- **test_lucidity_service.py** (27 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **asyncio** (16 connections)
- **._prepare_sanitarium_respawn()** (13 connections) — `server/services/player_respawn_service.py`
- **encode_liabilities()** (12 connections) — `server/services/lucidity_helpers.py`
- **UUID** (12 connections)
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **._apply_sanitarium_liability_update()** (11 connections) — `server/services/player_respawn_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **._calculate_max_lcd()** (8 connections) — `server/services/lucidity_service.py`
- **._add_liabilities_for_adjustment()** (6 connections) — `server/services/lucidity_service.py`
- **.add_liability()** (6 connections) — `server/services/lucidity_service.py`
- **.clear_liability()** (5 connections) — `server/services/lucidity_service.py`
- **._max_lcd_from_stats()** (5 connections) — `server/services/lucidity_service.py`
- **.set_cooldown()** (5 connections) — `server/services/lucidity_service.py`
- **test_add_liability_increments_stack()** (5 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **test_apply_lucidity_adjustment_clears_phantoms_on_tier_improvement()** (5 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **test_apply_lucidity_adjustment_keeps_phantoms_within_eligible_tiers()** (5 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **test_apply_lucidity_adjustment_writes_through_the_tier_cache()** (5 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **test_clear_liability_decrements_stack()** (5 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **test_clear_liability_remove_all()** (5 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **.get_cooldown()** (4 connections) — `server/services/lucidity_service.py`
- **._get_player_from_record_inspect()** (4 connections) — `server/services/lucidity_service.py`
- **.get_player_lucidity()** (4 connections) — `server/services/lucidity_service.py`
- **mock_lucidity_record()** (4 connections) — `server/tests/unit/services/test_lucidity_service.py`
- *... and 61 more nodes in this community*

## Relationships

- [Community 207](Community_207.md) (22 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (14 shared connections)
- [Community 347](Community_347.md) (10 shared connections)
- [Community 245](Community_245.md) (7 shared connections)
- [Community 336](Community_336.md) (5 shared connections)
- [Combat Instance Turns](Combat_Instance_Turns.md) (3 shared connections)
- [Community 177](Community_177.md) (3 shared connections)
- [Community 166](Community_166.md) (3 shared connections)
- [Community 206](Community_206.md) (3 shared connections)
- [Community 130](Community_130.md) (2 shared connections)
- [Community 156](Community_156.md) (2 shared connections)
- [Community 136](Community_136.md) (2 shared connections)

## Source Files

- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_lucidity_service.py`

## Audit Trail

- EXTRACTED: 198 (83%)
- INFERRED: 41 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*