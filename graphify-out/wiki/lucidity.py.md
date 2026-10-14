# lucidity.py

> 84 nodes

## Key Concepts

- **lucidity.py** (37 connections) — `server/models/lucidity.py`
- **test_lucidity_models.py** (28 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **LucidityCooldown** (27 connections) — `server/models/lucidity.py`
- **LucidityAdjustmentLog** (20 connections) — `server/models/lucidity.py`
- **test_active_lucidity_timed_recovery.py** (18 connections) — `server/tests/unit/services/test_active_lucidity_timed_recovery.py`
- **_service()** (15 connections) — `server/tests/unit/services/test_active_lucidity_timed_recovery.py`
- **Ledger** (13 connections) — `server/tests/unit/services/test_active_lucidity_timed_recovery.py`
- **test_apply_timed_recovery_refuses_during_cooldown()** (9 connections) — `server/tests/unit/services/test_active_lucidity_timed_recovery.py`
- **_utc_now()** (8 connections) — `server/models/lucidity.py`
- **test_apply_timed_recovery_applies_gain_and_sets_cooldown()** (7 connections) — `server/tests/unit/services/test_active_lucidity_timed_recovery.py`
- **test_folk_tonic_is_no_longer_a_recovery_action()** (7 connections) — `server/tests/unit/services/test_active_lucidity_timed_recovery.py`
- **test_lucidity_utils.py** (7 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **LucidityActionCode** (6 connections) — `server/models/lucidity.py`
- **test_perform_recovery_action_still_uses_its_profile_through_the_shared_path()** (6 connections) — `server/tests/unit/services/test_active_lucidity_timed_recovery.py`
- **datetime** (6 connections)
- **MonkeyPatch** (6 connections)
- **.set_cooldown()** (5 connections) — `server/tests/unit/services/test_active_lucidity_timed_recovery.py`
- **test_apply_timed_recovery_allows_an_expired_cooldown()** (5 connections) — `server/tests/unit/services/test_active_lucidity_timed_recovery.py`
- **asyncio** (5 connections)
- **.apply_lucidity_adjustment()** (4 connections) — `server/tests/unit/services/test_active_lucidity_timed_recovery.py`
- **.get_cooldown()** (4 connections) — `server/tests/unit/services/test_active_lucidity_timed_recovery.py`
- **Base** (4 connections)
- **UUID** (4 connections)
- **test_lucidity_adjustment_log_creation()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_lucidity_adjustment_log_default_metadata()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- *... and 59 more nodes in this community*

## Relationships

- [LucidityService](LucidityService.md) (22 shared connections)
- [LucidityRepository](LucidityRepository.md) (18 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [active_lucidity_service.py](active_lucidity_service.py.md) (4 shared connections)
- [debrief_command.py](debrief_command.py.md) (3 shared connections)
- [Player](Player.md) (3 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (3 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (2 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (2 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (2 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (2 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/tests/unit/models/test_lucidity_models.py`
- `server/tests/unit/models/test_lucidity_utils.py`
- `server/tests/unit/services/test_active_lucidity_timed_recovery.py`

## Audit Trail

- EXTRACTED: 201 (92%)
- INFERRED: 18 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*