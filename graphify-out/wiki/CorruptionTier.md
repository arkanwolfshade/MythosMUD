# CorruptionTier

> 137 nodes

## Key Concepts

- **CorruptionTier** (42 connections) — `server/models/corruption.py`
- **CorruptionService** (42 connections) — `server/services/corruption_service.py`
- **corruption_service.py** (42 connections) — `server/services/corruption_service.py`
- **test_corruption_service.py** (25 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_corruption_reactions.py** (22 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **CorruptionRepository** (18 connections) — `server/services/corruption_repository.py`
- **_async_session_gen()** (14 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_corruption_repository.py** (14 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **.apply_corruption_adjustment()** (13 connections) — `server/services/corruption_service.py`
- **_player()** (13 connections) — `server/tests/unit/services/test_corruption_service.py`
- **corruption_reactions.py** (13 connections) — `server/npc/corruption_reactions.py`
- **asyncio** (13 connections)
- **corruption_tier_cache.py** (12 connections) — `server/services/corruption_tier_cache.py`
- **_MockAsyncSession** (10 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **build_corruption_aware_greeting()** (10 connections) — `server/npc/corruption_reactions.py`
- **.perform_recovery_action()** (10 connections) — `server/services/corruption_service.py`
- **corruption_repository.py** (10 connections) — `server/services/corruption_repository.py`
- **corruption_hostility_scale()** (9 connections) — `server/npc/corruption_reactions.py`
- **_pick_greeting()** (7 connections) — `server/npc/corruption_reactions.py`
- **.get_cooldown_expiry()** (7 connections) — `server/services/corruption_service.py`
- **_reset_cache()** (7 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_get_cooldown_returns_record()** (7 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **test_set_cooldown_updates_existing()** (7 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **test_apply_corruption_adjustment_bypass_permanence_floor_allows_zero()** (7 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_floors_at_1_once_touched()** (7 connections) — `server/tests/unit/services/test_corruption_service.py`
- *... and 112 more nodes in this community*

## Relationships

- [models/player.py](models-player.py.md) (25 shared connections)
- [test_passive_corruption_flux_service.py](test_passive_corruption_flux_service.py.md) (11 shared connections)
- [cleanse_command.py](cleanse_command.py.md) (11 shared connections)
- [format_occupant_display_name](format_occupant_display_name.md) (10 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (9 shared connections)
- [SpellCostsService](SpellCostsService.md) (6 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (5 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (5 shared connections)
- [SpellLearningService](SpellLearningService.md) (4 shared connections)
- [event_types.py](event_types.py.md) (4 shared connections)
- [get_async_session](get_async_session.md) (4 shared connections)

## Source Files

- `server/game/mechanics.py`
- `server/models/corruption.py`
- `server/npc/corruption_reactions.py`
- `server/services/corruption_repository.py`
- `server/services/corruption_service.py`
- `server/services/corruption_tier_cache.py`
- `server/tests/unit/models/test_corruption.py`
- `server/tests/unit/npc/test_corruption_reactions.py`
- `server/tests/unit/services/test_corruption_repository.py`
- `server/tests/unit/services/test_corruption_service.py`

## Audit Trail

- EXTRACTED: 353 (88%)
- INFERRED: 49 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*