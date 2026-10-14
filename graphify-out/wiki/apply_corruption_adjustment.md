# .apply_corruption_adjustment

> 17 nodes

## Key Concepts

- **.apply_corruption_adjustment()** (13 connections) — `server/services/corruption_service.py`
- **.perform_recovery_action()** (10 connections) — `server/services/corruption_service.py`
- **.get_cooldown_expiry()** (7 connections) — `server/services/corruption_service.py`
- **UUID** (7 connections)
- **._notify_tier_crossing()** (6 connections) — `server/services/corruption_service.py`
- **CorruptionActionError** (5 connections) — `server/services/corruption_service.py`
- **._send_corruption_update_event()** (5 connections) — `server/services/corruption_service.py`
- **.get_player_by_id()** (3 connections) — `server/services/corruption_service.py`
- **datetime** (2 connections)
- **CorruptionTier** (1 connections)
- **RuntimeError** (1 connections)
- **Apply a corruption delta, clamp it, log it, update the tier cache, notify on…** (1 connections) — `server/services/corruption_service.py`
- **Push the new corruption value to the client. Client reads it via the existing…** (1 connections) — `server/services/corruption_service.py`
- **Deliver a personal system message exactly once per tier crossing.** (1 connections) — `server/services/corruption_service.py`
- **Fetch the cooldown expiry for a recovery action, or None if not on cooldown.** (1 connections) — `server/services/corruption_service.py`
- **Perform a corruption recovery rite (e.g. `/cleanse`) and enforce its cooldown.** (1 connections) — `server/services/corruption_service.py`
- **Base error for corruption action operations.** (1 connections) — `server/services/corruption_service.py`

## Relationships

- [get_logger](get_logger.md) (8 shared connections)
- [CorruptionService](CorruptionService.md) (5 shared connections)
- [CorruptionRepository](CorruptionRepository.md) (3 shared connections)
- [handle_cleanse_command](handle_cleanse_command.md) (2 shared connections)
- [test_passive_corruption_flux_service.py](test_passive_corruption_flux_service.py.md) (2 shared connections)
- [cleanse_command.py](cleanse_command.py.md) (1 shared connections)
- [log_and_raise_enhanced](log_and_raise_enhanced.md) (1 shared connections)
- [coerce_int](coerce_int.md) (1 shared connections)
- [LucidityService](LucidityService.md) (1 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (1 shared connections)
- [magic_service.py](magic_service.py.md) (1 shared connections)

## Source Files

- `server/services/corruption_service.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*