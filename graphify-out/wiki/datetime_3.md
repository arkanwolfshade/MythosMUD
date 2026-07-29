# datetime

> 40 nodes

## Key Concepts

- **LucidityService** (78 connections) — `server/services/lucidity_service.py`
- **UUID** (14 connections)
- **test_lucidity_service.py** (11 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **._calculate_max_lcd()** (8 connections) — `server/services/lucidity_service.py`
- **Tier** (6 connections)
- **._add_liabilities_for_adjustment()** (6 connections) — `server/services/lucidity_service.py`
- **.add_liability()** (6 connections) — `server/services/lucidity_service.py`
- **.__init__()** (5 connections) — `server/services/active_lucidity_service.py`
- **worsened_tier()** (5 connections) — `server/services/lucidity_helpers.py`
- **.set_cooldown()** (5 connections) — `server/services/lucidity_service.py`
- **._default_liability_picker()** (5 connections) — `server/services/lucidity_service.py`
- **._get_player_from_record_inspect()** (4 connections) — `server/services/lucidity_service.py`
- **._max_lcd_from_stats()** (4 connections) — `server/services/lucidity_service.py`
- **.get_player_lucidity()** (4 connections) — `server/services/lucidity_service.py`
- **datetime** (3 connections)
- **.clear_hallucination_timers()** (3 connections) — `server/services/lucidity_service.py`
- **mock_lucidity_record()** (3 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **test_apply_lucidity_adjustment_positive_delta()** (3 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **test_apply_lucidity_adjustment_negative_delta()** (3 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **test_apply_lucidity_adjustment_clamps_to_max()** (3 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **test_apply_lucidity_adjustment_clamps_to_min()** (3 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **datetime** (2 connections)
- **mock_session()** (2 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **Test applying positive lucidity adjustment.** (2 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **Test that lucidity adjustment clamps to maximum value.** (2 connections) — `server/tests/unit/services/test_lucidity_service.py`
- *... and 15 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (28 shared connections)
- [LiabilityStackEntry](LiabilityStackEntry.md) (22 shared connections)
- [Any](Any.md) (15 shared connections)
- [HallucinationFrequencyService](HallucinationFrequencyService.md) (5 shared connections)
- [.initialize()](initialize%28%29.md) (3 shared connections)
- [admin setlucidity command](admin_setlucidity_command.md) (3 shared connections)
- [combat](combat.md) (3 shared connections)
- [AsyncSessionFactory](AsyncSessionFactory.md) (3 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [rescue commands](rescue_commands.md) (2 shared connections)
- [message formatters](message_formatters.md) (2 shared connections)
- [. call ()](_call_%28%29.md) (2 shared connections)

## Source Files

- `server/services/active_lucidity_service.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/tests/unit/services/test_lucidity_service.py`

## Audit Trail

- EXTRACTED: 177 (86%)
- INFERRED: 28 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*